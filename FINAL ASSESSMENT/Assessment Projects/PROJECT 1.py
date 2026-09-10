import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import TimeSeriesSplit, cross_val_score

file = r"C:\Users\Marium Khan\Documents\GitHub\My-Course-AI-Bin-B11\FINAL ASSESSMENT\Microsoft_stock_history.csv"
df = pd.read_csv(file)
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date").dropna(subset=["Close","High","Low","Volume"]).copy()
df["Return"] = np.log(df["Close"]/df["Close"].shift(1))
df["MA20"] = df["Close"].rolling(20).mean()
df["MA50"] = df["Close"].rolling(50).mean()
df["Vol20"] = df["Return"].rolling(20).std()
df["Mom20"] = df["Close"]/df["Close"].shift(20)-1
df["HLRange"] = (df["High"]-df["Low"])/df["Close"]
df["VolumeRatio"] = df["Volume"]/df["Volume"].rolling(20).mean()
up = df["Close"].diff()
down = -up.clip(upper=0)
rs = up.clip(lower=0).rolling(14).mean()/down.rolling(14).mean()
df["RSI"] = 100-100/(1+rs)
df["Target"] = (df["Return"].shift(-1)>0).astype(int)
df = df.dropna()
features = ["Return","MA20","MA50","Vol20","Mom20","HLRange","VolumeRatio","RSI"]
X, y = df[features], df["Target"]
model = RandomForestClassifier(n_estimators=150, random_state=1)
s = cross_val_score(model, X, y, cv=TimeSeriesSplit(5))
model.fit(X,y)
out = pd.Series(model.feature_importances_, index=features).sort_values(ascending=False)
print("Accuracy:", s.mean())
print(out)
sns.barplot(x=out.values, y=out.index, hue=out.index, legend=False)
