# ==========================================================
# Project : Retail Sales Analytics Platform
# Module 3 : Data Cleaning
# Author : Tejveer Yadav
# ==========================================================

import pandas as pd

# Load Dataset
df = pd.read_csv("data/raw/retail_sales_dataset.csv")

print("=" * 60)
print("DATA CLEANING")
print("=" * 60)

# -----------------------------
# Convert Date Column
# -----------------------------
df["Date"] = pd.to_datetime(df["Date"])

print("\n✅ Date column converted successfully!")

# -----------------------------
# Standardize Column Names
# -----------------------------
df.columns = (
    df.columns
      .str.strip()
      .str.lower()
      .str.replace(" ", "_")
)

print("\n✅ Column names standardized!")

print("\nUpdated Data Types:")
print(df.dtypes)

print("\nUpdated Column Names:")
print(df.columns)

# -----------------------------
# Save Clean Dataset
# -----------------------------
df.to_csv("data/cleaned/retail_sales_cleaned.csv", index=False)

print("\n✅ Clean dataset saved successfully!")