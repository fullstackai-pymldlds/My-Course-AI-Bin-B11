import pandas as pd
import numpy as np

files={"Adobe":r"C:\Users\Marium Khan\Documents\GitHub\My-Course-AI-Bin-B11\FINAL ASSESSMENT\Adobe (ADBE) From 1986 To Dec-2024.csv","Oracle":r"C:\Users\Marium Khan\Documents\GitHub\My-Course-AI-Bin-B11\FINAL ASSESSMENT\oracle.csv","Salesforce":r"C:\Users\Marium Khan\Documents\GitHub\My-Course-AI-Bin-B11\FINAL ASSESSMENT\Salesforce (CRM) From 2004 To Dec-2024.csv"}
rows=[]
for name,path in files.items():
 df=pd.read_csv(path).sort_values("Date").dropna(subset=["Close","Volume"])
 df["Return"]=df["Close"].pct_change()
 df["Momentum"]=df["Close"]/df["Close"].shift(20)-1
 df["Trend"]=df["Close"]/df["Close"].rolling(50).mean()-1
 df["Volatility"]=df["Return"].rolling(20).std()
 up=df["Close"].diff().clip(lower=0).rolling(14).mean()
 down=(-df["Close"].diff().clip(upper=0)).rolling(14).mean()
 rs=up/down; df["RelativeStrength"]=100-100/(1+rs)
 df["Volume"]=df["Volume"]/df["Volume"].rolling(20).mean()
 r=df.dropna()
 for date,g in r.groupby(pd.to_datetime(r["Date"],utc=True).dt.strftime("%Y-%U")):
  row=g.iloc[-1]; rows.append([date,name,row["Momentum"],row["Trend"],-row["Volatility"],row["RelativeStrength"],row["Volume"]])
out=pd.DataFrame(rows,columns=["Week","Stock","Momentum","Trend","Volatility","RelativeStrength","Volume"])
out=out.groupby("Week").filter(lambda x: len(x)==len(files))
for c in out.columns[2:]: out[c]=out.groupby("Week")[c].rank(pct=True)
out["Score"]=out.iloc[:,2:].mean(axis=1)
print(out.sort_values(["Week","Score"],ascending=[False,False]).head(20))
