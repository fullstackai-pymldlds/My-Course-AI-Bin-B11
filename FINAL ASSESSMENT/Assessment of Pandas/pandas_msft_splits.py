import pandas as pd

df=pd.read_csv(r"C:\Users\Marium Khan\Documents\GitHub\My-Course-AI-Bin-B11\FINAL ASSESSMENT\Microsoft_stock_spilts.csv")
print(df.info())
print(df.describe(include="all"))
