import pandas as pd
import numpy as np
from keras import Sequential
from keras.layers import LSTM, Dense

df = pd.read_csv(r"C:\Users\Marium Khan\Documents\GitHub\My-Course-AI-Bin-B11\FINAL ASSESSMENT\Salesforce (CRM) From 2004 To Dec-2024.csv").dropna(subset=["Close"])
r = np.log(df["Close"].to_numpy()[1:]/df["Close"].to_numpy()[:-1])
X = np.array([r[i-60:i] for i in range(60,len(r))])
y = r[60:]
m = Sequential([LSTM(32,input_shape=(60,1)),Dense(1)])
m.compile(optimizer="adam",loss="mse")
m.fit(X.reshape(-1,60,1),y,epochs=3,batch_size=32,verbose=0)
print("Loss:",m.evaluate(X.reshape(-1,60,1),y,verbose=0))
