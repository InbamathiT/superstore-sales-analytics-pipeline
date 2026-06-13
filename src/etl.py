import pandas as pd
import os

# Load raw data
df = pd.read_csv("data/raw/Sample - Superstore.csv", encoding="latin1")
print("Shape:", df.shape)
print(df.isnull().sum())
print(df.dtypes)

# Clean column names: remove spaces, trim whitespace
df.columns = df.columns.str.strip().str.replace(" ", "_")

# Convert date columns to proper datetime type
df["Order_Date"] = pd.to_datetime(df["Order_Date"])
df["Ship_Date"]  = pd.to_datetime(df["Ship_Date"])

# Drop rows missing critical fields
df = df.dropna(subset=["Sales", "Profit", "Customer_ID"])

# Fill any remaining nulls with "Unknown"
df = df.fillna("Unknown")

# Add a new calculated column
df["Profit_Margin"] = (df["Profit"] / df["Sales"] * 100).round(2)

# Save cleaned data
os.makedirs("data/clean", exist_ok=True)
df.to_csv("data/clean/superstore_clean.csv", index=False)
print("✓ Clean CSV saved. Rows:", len(df))