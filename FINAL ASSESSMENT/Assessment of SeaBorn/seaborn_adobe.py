import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv(r"C:\Users\Marium Khan\Documents\GitHub\My-Course-AI-Bin-B11\FINAL ASSESSMENT\Adobe (ADBE) From 1986 To Dec-2024.csv")
df["Date"] = pd.to_datetime(df["Date"])
df["Return"] = np.log(df["Close"]/df["Close"].shift(1))
sns.histplot(df["Return"].dropna(), kde=True)
plt.title("ADOBE Return Distribution")
plt.tight_layout()
plt.show()
