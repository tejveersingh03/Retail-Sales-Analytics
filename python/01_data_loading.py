# ==========================================================
# Project : Retail Sales Analytics Platform
# Module 1 : Data Loading
# Author : Tejveer Yadav
# ==========================================================

import pandas as pd

print("=" * 60)
print("Retail Sales Analytics Platform")
print("=" * 60)

# Load Dataset
df = pd.read_csv("data/raw/retail_sales_dataset.csv")

print("\n✅ Dataset Loaded Successfully!")

print("\nFirst 5 Rows")
print(df.head())

print("\n" + "=" * 60)
print("Dataset Shape")
print("=" * 60)
print(df.shape)

print("\n" + "=" * 60)
print("Column Names")
print("=" * 60)
print(df.columns)

print("\n" + "=" * 60)
print("Dataset Information")
print("=" * 60)
print(df.info())

print("\n" + "=" * 60)
print("Statistical Summary")
print("=" * 60)
print(df.describe())