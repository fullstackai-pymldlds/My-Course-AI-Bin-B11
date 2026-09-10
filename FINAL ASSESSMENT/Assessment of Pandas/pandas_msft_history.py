import pandas as pd
import numpy as np

df = pd.read_csv(r"C:\Users\Marium Khan\Documents\GitHub\My-Course-AI-Bin-B11\FINAL ASSESSMENT\Microsoft_stock_history.csv")
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
df = df.dropna(subset=["Close"]).sort_values("Date")
df["Return"] = np.log(df["Close"]/df["Close"].shift(1))
df["MA20"] = df["Close"].rolling(20).mean()
df["Vol20"] = df["Return"].rolling(20).std()
df["Mom20"] = df["Close"]/df["Close"].shift(20)-1
df["HL_Range"] = (df["High"]-df["Low"])/df["Close"]
print(df.describe())
print(df[["Return","MA20","Vol20","Mom20","HL_Range"]].tail())
