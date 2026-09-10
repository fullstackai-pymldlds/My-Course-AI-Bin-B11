import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

file = r"C:\Users\Marium Khan\Documents\GitHub\My-Course-AI-Bin-B11\FINAL ASSESSMENT\Microsoft_stock_history.csv"
df = pd.read_csv(file)
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date").dropna(subset=["Close","Volume"]).copy()
df["Return"] = np.log(df["Close"]/df["Close"].shift(1))
df["Volatility"] = df["Return"].rolling(20).std()
df["Trend"] = df["Close"]/df["Close"].rolling(50).mean()-1
x = df[["Return","Volume","Volatility","Trend"]].dropna()
z = StandardScaler().fit_transform(x)
p = PCA(n_components=2).fit_transform(z)
model = KMeans(n_clusters=4,random_state=1,n_init=10)
df.loc[x.index,"Regime"] = model.fit_predict(z)
mean = df.groupby("Regime")[["Return","Volatility","Trend"]].mean()
print(mean)
print("PCA shape:",p.shape)
print("Latest regime:",int(df["Regime"].dropna().iloc[-1]))
print("Regime counts:")
print(df["Regime"].value_counts().sort_index())
