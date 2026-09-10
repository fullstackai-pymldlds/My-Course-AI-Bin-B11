import pandas as pd
import numpy as np

df = pd.read_csv(r"C:\Users\Marium Khan\Documents\GitHub\My-Course-AI-Bin-B11\FINAL ASSESSMENT\Microsoft_stock_spilts.csv")
x = df["Stock Splits"].to_numpy(dtype=float)
print("Splits:",np.sum(x>0))
print("Mean:",np.mean(x))
print("Max:",np.max(x))
