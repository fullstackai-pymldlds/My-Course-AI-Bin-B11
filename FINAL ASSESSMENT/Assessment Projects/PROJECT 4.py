import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier,GradientBoostingClassifier
from sklearn.model_selection import TimeSeriesSplit
try:
 import tensorflow as tf
except ImportError:
 tf = None

df=pd.read_csv(r"C:\Users\Marium Khan\Documents\GitHub\My-Course-AI-Bin-B11\FINAL ASSESSMENT\Microsoft_stock_history.csv").dropna()
df["Return"]=np.log(df["Close"]/df["Close"].shift(1))
df["Mom20"]=df["Close"]/df["Close"].shift(20)-1
df["Vol20"]=df["Return"].rolling(20).std()
df["Target"]=(df["Return"].shift(-1)>0).astype(int); df=df.dropna()
X=df[["Return","Mom20","Vol20"]]; y=df["Target"]; cv=TimeSeriesSplit(5)
def test_model(model):
 p=[]; actual=[]
 for train,test in cv.split(X):
  model.fit(X.iloc[train],y.iloc[train]); p.extend(model.predict_proba(X.iloc[test])[:,1]); actual.extend(test)
 return np.array(p),np.array(actual)
def risk(prob,idx):
 ret=df["Return"].iloc[idx].to_numpy(); strat=np.where(prob>.60,ret,0); curve=np.exp(np.cumsum(strat)); dd=curve/np.maximum.accumulate(curve)-1
 return strat.mean()/strat.std()*np.sqrt(252),dd.min()
for model in [RandomForestClassifier(n_estimators=50,random_state=1),GradientBoostingClassifier(random_state=1)]:
 prob,idx=test_model(model); print(type(model).__name__,"Accuracy:",((prob>.5)==(df["Target"].iloc[idx].to_numpy()==1)).mean()); print("Risk:",risk(prob,idx))
if tf is not None:
 r=df["Return"].to_numpy(); seq=np.array([r[i-60:i] for i in range(60,len(r))]); target=(r[60:]>0).astype(int); cut=int(len(seq)*.8)
 m=tf.keras.Sequential([tf.keras.layers.LSTM(32,input_shape=(60,1)),tf.keras.layers.Dense(1,activation="sigmoid")])
 m.compile(optimizer="adam",loss="binary_crossentropy",metrics=["accuracy"]); m.fit(seq[:cut].reshape(-1,60,1),target[:cut],epochs=3,batch_size=32,verbose=0)
 pr=m.predict(seq[cut:].reshape(-1,60,1),verbose=0).ravel(); idx=np.arange(cut+60,len(df)); print("LSTM Accuracy:",((pr>.5)==target[cut:]).mean()); print("LSTM Risk:",risk(pr,idx))
else: print("LSTM skipped: TensorFlow not installed")
