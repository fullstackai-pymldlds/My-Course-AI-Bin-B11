import pandas as pd
import numpy as np

df = pd.read_csv(r"C:\Users\Marium Khan\Documents\GitHub\My-Course-AI-Bin-B11\FINAL ASSESSMENT\Microsoft_stock_dividends.csv")
x = df["Dividends"].to_numpy(dtype=float)
print("Mean:",np.mean(x))
print("Std:",np.std(x))
print("Median:",np.median(x))
print("Change:",np.diff(x).mean())
