import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import TimeSeriesSplit, cross_val_score
from xgboost import XGBRegressor
try:
 import tensorflow as tf
except ImportError:
 tf = None

df = pd.read_csv(r"C:\Users\Marium Khan\Documents\GitHub\My-Course-AI-Bin-B11\FINAL ASSESSMENT\Microsoft_stock_history.csv")
df["Return"] = np.log(df["Close"]/df["Close"].shift(1))
df["Vol5"] = df["Return"].rolling(5).std()
df["Vol20"] = df["Return"].rolling(20).std()
df["Vol60"] = df["Return"].rolling(60).std()
df["FutureVol20"] = df["Return"].rolling(20).std().shift(-20)
df = df.dropna()
X = df[["Vol5","Vol20","Vol60"]]
y = df["FutureVol20"]
cv = TimeSeriesSplit(5)
models = [RandomForestRegressor(n_estimators=100,random_state=1), XGBRegressor(n_estimators=100,max_depth=3,learning_rate=.05,objective="reg:squarederror",random_state=1)]
for model in models:
 mse = -cross_val_score(model,X,y,cv=cv,scoring="neg_mean_squared_error").mean()
 print(type(model).__name__,"MSE:",mse)
if tf is not None:
 r = df["Return"].to_numpy()
 seq = np.array([r[i-60:i] for i in range(60,len(r)-20)])
 target = np.array([np.std(r[i:i+20]) for i in range(60,len(r)-20)])
 cut = int(len(seq)*.8)
 m = tf.keras.Sequential([tf.keras.layers.LSTM(32,input_shape=(60,1)),tf.keras.layers.Dense(1)])
 m.compile(optimizer="adam",loss="mse")
 m.fit(seq[:cut].reshape(-1,60,1),target[:cut],epochs=3,batch_size=32,verbose=0)
 print("LSTM MSE:",m.evaluate(seq[cut:].reshape(-1,60,1),target[cut:],verbose=0))
else:
 print("LSTM skipped: TensorFlow not installed")
