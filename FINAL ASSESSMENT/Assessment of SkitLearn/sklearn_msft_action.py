import pandas as pd
from sklearn.preprocessing import LabelEncoder

df=pd.read_csv(r"C:\Users\Marium Khan\Documents\GitHub\My-Course-AI-Bin-B11\FINAL ASSESSMENT\Microsoft_stock_action.csv")
for c in df.select_dtypes("object"):
    df[c]=LabelEncoder().fit_transform(df[c].astype(str))
print(df.describe())
