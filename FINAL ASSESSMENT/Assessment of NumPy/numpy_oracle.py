import numpy as np
import pandas as pd

df = pd.read_csv(r"C:\Users\Marium Khan\Documents\GitHub\My-Course-AI-Bin-B11\FINAL ASSESSMENT\oracle.csv")
x = pd.to_numeric(df["Close"], errors="coerce").dropna().to_numpy()
r = np.diff(np.log(x))
print("Mean:", np.mean(x))
print("Std:", np.std(x))
print("Min:", np.min(x))
print("Max:", np.max(x))
print("Annual Volatility:", np.std(r)*np.sqrt(252))
print("Median:", np.median(x))
