import pandas as pd
import numpy as np
import keras

df=pd.read_csv(r"C:\Users\Marium Khan\Documents\GitHub\My-Course-AI-Bin-B11\FINAL ASSESSMENT\Microsoft_stock_action.csv")
x=df.select_dtypes("number").fillna(0).to_numpy()
model=tf.keras.Sequential([tf.keras.layers.Dense(8,activation="relu"),tf.keras.layers.Dense(1)])
model.compile(optimizer="adam",loss="mse")
model.fit(x,x[:,0],epochs=2,verbose=0)
print(model.evaluate(x,x[:,0],verbose=0))
