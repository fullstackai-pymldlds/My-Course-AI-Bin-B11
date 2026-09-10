import pandas as pd
import numpy as np

df = pd.read_csv(r"C:\Users\Marium Khan\Documents\GitHub\My-Course-AI-Bin-B11\FINAL ASSESSMENT\Microsoft_stock_action.csv")
print(df.describe(include="all"))
print("Events:",len(df))
