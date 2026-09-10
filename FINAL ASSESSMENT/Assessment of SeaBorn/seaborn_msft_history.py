import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv(r"C:\Users\Marium Khan\Documents\GitHub\My-Course-AI-Bin-B11\FINAL ASSESSMENT\Microsoft_stock_history.csv")
df["Date"] = pd.to_datetime(df["Date"])
df["Return"] = np.log(df["Close"]/df["Close"].shift(1))
sns.histplot(df["Return"].dropna(), kde=True)
plt.title("MSFT_HISTORY Return Distribution")
plt.tight_layout()
plt.show()
