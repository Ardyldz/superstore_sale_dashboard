import pandas as pd

# 1. Ham veriyi oku
df = pd.read_csv("train.csv")

# 2. Tarih kolonlarini cevir ve turetilmis alanlar olustur
df["Order_Date"] = pd.to_datetime(df["Order Date"], format="%d/%m/%Y")
df["Ship_Date"] = pd.to_datetime(df["Ship Date"], format="%d/%m/%Y")
df["Shipping_Days"] = (df["Ship_Date"] - df["Order_Date"]).dt.days
df["Order_Year"] = df["Order_Date"].dt.year
df["Order_Month"] = df["Order_Date"].dt.month
df["Order_YearMonth"] = df["Order_Date"].dt.to_period("M").astype(str)

# 3. Eksik posta kodunu (Burlington, VT -> 05401) doldur ve 5 haneye tamamla
df["Postal Code"] = (
    df["Postal Code"]
    .fillna(5401)
    .astype(int)
    .astype(str)
    .str.zfill(5)
)

# 4. Mukerrer kayit varsa temizle
df = df.drop_duplicates()

# 5. Temiz veriyi Excel'e aktar (openpyxl kurulu olmali)
df.to_excel("cleaned_superstore.xlsx", index=False, sheet_name="Clean_Data")
print("Tamamlandi. Satir sayisi:", len(df))

