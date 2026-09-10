import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv(r"C:\Users\Marium Khan\Documents\GitHub\My-Course-AI-Bin-B11\FINAL ASSESSMENT\oracle.csv")
df["Date"] = pd.to_datetime(df["Date"])
df["Return"] = np.log(df["Close"]/df["Close"].shift(1))
sns.histplot(df["Return"].dropna(), kde=True)
plt.title("ORACLE Return Distribution")
plt.tight_layout()
plt.show()
