import pandas as pd
import numpy as np
import tensorflow as tf

df = pd.read_csv(r"C:\Users\Marium Khan\Documents\GitHub\My-Course-AI-Bin-B11\FINAL ASSESSMENT\Salesforce (CRM) From 2004 To Dec-2024.csv").dropna(subset=["Close"])
x = df["Close"].to_numpy()
r = np.log(x[1:]/x[:-1])
X = np.array([r[i-20:i] for i in range(20,len(r))])
y = r[20:]
m = tf.keras.Sequential([tf.keras.layers.Dense(32,activation="relu"),
                         tf.keras.layers.Dense(16,activation="relu"),
                         tf.keras.layers.Dense(1)])
m.compile(optimizer="adam", loss="mse")
m.fit(X,y,epochs=5,batch_size=32,verbose=0)
print("Loss:", m.evaluate(X,y,verbose=0))
