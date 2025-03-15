import pandas as pd

# Veriyi oku
df = pd.read_csv("HousingData.csv")

print("Öncesi:")
print(df.isnull().sum())  # Eksik veri sayısını göster

# Eğer veri tipi 'object' ise sayısala çevir
for col in df.columns:
    if df[col].dtype == "object":
        df[col] = pd.to_numeric(df[col])  # Sayısal hale getir


# Interpolasyon ile kalan boşlukları doldur (sadece sayısal sütunlara uygula)
df.interpolate(method="linear", inplace=True)

# Hâlâ eksik veri varsa, sütunun medyan değeri ile doldur
df.fillna(df.median(numeric_only=True), inplace=True)

print("\n Sonrası:")
print(df.isnull().sum())  # Eksik veri kaldı mı kontrol et
df.to_csv("Cleaned_HousingData.csv")
