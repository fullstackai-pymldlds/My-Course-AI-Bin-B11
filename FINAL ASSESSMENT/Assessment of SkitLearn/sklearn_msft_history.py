import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import TimeSeriesSplit, cross_val_score

df = pd.read_csv(r"C:\Users\Marium Khan\Documents\GitHub\My-Course-AI-Bin-B11\FINAL ASSESSMENT\Microsoft_stock_history.csv")
df = df.sort_values("Date").dropna(subset=["Close"]).copy()
df["Return"] = np.log(df["Close"]/df["Close"].shift(1))
df["MA20"] = df["Close"].rolling(20).mean()
df["Vol20"] = df["Return"].rolling(20).std()
df["Mom20"] = df["Close"]/df["Close"].shift(20)-1
df["Target"] = (df["Return"].shift(-1)>0).astype(int)
df = df.dropna()
X = df[["Return","MA20","Vol20","Mom20"]]
y = df["Target"]
cv = TimeSeriesSplit(5)
model = RandomForestClassifier(n_estimators=100, random_state=1)
s = cross_val_score(model, X, y, cv=cv, scoring="accuracy")
model.fit(X,y)
print("Accuracy:", s.mean())
print("Importance:", dict(zip(X.columns, model.feature_importances_)))
