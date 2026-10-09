"""
Initial exploration of the Online Retail II dataset.
Identifies data quality issues before cleaning.
"""

import pandas as pd

# Load both sheets
print("Loading data...")
df_2009 = pd.read_excel("../data/raw/online_retail_II.xlsx", sheet_name="Year 2009-2010")
df_2010 = pd.read_excel("../data/raw/online_retail_II.xlsx", sheet_name="Year 2010-2011")

# Combine both years
df = pd.concat([df_2009, df_2010], ignore_index=True)

print("=" * 60)
print("📊 DATASET OVERVIEW")
print("=" * 60)
print(f"Total rows: {len(df):,}")
print(f"Columns: {list(df.columns)}")
print(f"\nDate range: {df['InvoiceDate'].min()} to {df['InvoiceDate'].max()}")

print("\n" + "=" * 60)
print("🔍 DATA QUALITY CHECK")
print("=" * 60)

# Missing values
print("\nMissing values per column:")
print(df.isnull().sum())

# Negative quantities (returns/cancellations)
negative_qty = (df['Quantity'] < 0).sum()
print(f"\nNegative quantities (returns): {negative_qty:,} rows")

# Cancelled orders (Invoice starting with 'C')
cancelled = df['Invoice'].astype(str).str.startswith('C').sum()
print(f"Cancelled invoices (start with 'C'): {cancelled:,} rows")

# Zero or negative prices
bad_price = (df['Price'] <= 0).sum()
print(f"Zero/negative prices: {bad_price:,} rows")

# Unique customers, products, countries
print(f"\nUnique customers: {df['Customer ID'].nunique():,}")
print(f"Unique products: {df['StockCode'].nunique():,}")
print(f"Unique countries: {df['Country'].nunique():,}")

print("\n" + "=" * 60)
print("✅ Exploration complete")
print("=" * 60)