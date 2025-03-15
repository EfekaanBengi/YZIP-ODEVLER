import pandas as pd

df = pd.read_csv("HousingData.csv")
print(df)
print(df.isnull().sum())

df2 = df.copy()

df2["CRIM"] = df2["CRIM"].interpolate(method="linear") # Ortalama alır
df2["CRIM"].fillna(method="bfill", inplace=True)  # İlk satırı doldurur
df2["CRIM"].fillna(method="ffill", inplace=True)  # Son satırı doldurur

df2["ZN"] = df2["ZN"].interpolate(method="linear")
df2["ZN"].fillna(method="bfill", inplace=True)  
df2["ZN"].fillna(method="ffill", inplace=True)  

df2["INDUS"] = df2["INDUS"].interpolate(method="linear")
df2["INDUS"].fillna(method="bfill", inplace=True)  
df2["INDUS"].fillna(method="ffill", inplace=True)  

df2["CHAS"] = df2["CHAS"].interpolate(method="linear")
df2["CHAS"].fillna(method="bfill", inplace=True)  
df2["CHAS"].fillna(method="ffill", inplace=True)  

df2["AGE"] = df2["AGE"].interpolate(method="linear")
df2["AGE"].fillna(method="bfill", inplace=True)  
df2["AGE"].fillna(method="ffill", inplace=True)  

df2["LSTAT"] = df2["LSTAT"].interpolate(method="linear") 
df2["LSTAT"].fillna(method="bfill", inplace=True)  
df2["LSTAT"].fillna(method="ffill", inplace=True)  

print(df.isnull().sum())
print(df2.isnull().sum())
df.to_csv("Cleaned_HousingData.csv")

