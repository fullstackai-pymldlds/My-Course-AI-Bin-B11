import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv(r"C:\Users\Marium Khan\Documents\GitHub\My-Course-AI-Bin-B11\FINAL ASSESSMENT\Microsoft_stock_dividends.csv")
sns.histplot(df.select_dtypes("number").iloc[:,0].dropna())
plt.show()
