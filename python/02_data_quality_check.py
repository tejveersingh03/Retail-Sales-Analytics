# ==========================================================
# Project : Retail Sales Analytics Platform
# Module 2 : Data Quality Check
# Author : Tejveer Yadav
# ==========================================================

import pandas as pd

# Load Dataset
df = pd.read_csv("data/raw/retail_sales_dataset.csv")

print("=" * 60)
print("DATA QUALITY CHECK")
print("=" * 60)

# Missing Values
print("\n1. Missing Values")
print(df.isnull().sum())

# Duplicate Records
print("\n2. Duplicate Records")
print(df.duplicated().sum())

# Data Types
print("\n3. Data Types")
print(df.dtypes)