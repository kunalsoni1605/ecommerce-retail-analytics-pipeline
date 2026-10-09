"""
Clean the Online Retail II dataset.
Produces two outputs:
1. transactions_full.csv - all records, flagged for cancellations/returns
2. transactions_clean.csv - valid sales only, ready for RFM/revenue analysis
"""

import pandas as pd

print("Loading raw data...")
df_2009 = pd.read_excel("../data/raw/online_retail_II.xlsx", sheet_name="Year 2009-2010")
df_2010 = pd.read_excel("../data/raw/online_retail_II.xlsx", sheet_name="Year 2010-2011")

df = pd.concat([df_2009, df_2010], ignore_index=True)
print(f"Combined raw rows: {len(df):,}")

# Standardize column names
df.columns = ['invoice', 'stock_code', 'description', 'quantity',
              'invoice_date', 'price', 'customer_id', 'country']

# --- Flag cancellations/returns (don't delete, just flag) ---
df['is_cancelled'] = df['invoice'].astype(str).str.startswith('C')
df['is_return'] = df['quantity'] < 0

# Calculate line revenue
df['line_total'] = df['quantity'] * df['price']

# Save FULL version (flagged, not filtered) - useful for returns analysis later
df.to_csv("../data/processed/transactions_full.csv", index=False)
print(f"✅ Saved transactions_full.csv ({len(df):,} rows)")

# --- Build CLEAN version for sales/RFM analysis ---
df_clean = df[
    (df['quantity'] > 0) &          # exclude returns
    (df['price'] > 0) &             # exclude bad prices
    (df['customer_id'].notna()) &   # exclude missing customer IDs
    (~df['is_cancelled'])           # exclude cancelled orders
].copy()

df_clean['customer_id'] = df_clean['customer_id'].astype(int)

print(f"\n✅ Clean rows: {len(df_clean):,} ({len(df_clean)/len(df)*100:.1f}% of original)")
print(f"   Unique customers in clean set: {df_clean['customer_id'].nunique():,}")
print(f"   Total revenue (clean): £{df_clean['line_total'].sum():,.2f}")

df_clean.to_csv("../data/processed/transactions_clean.csv", index=False)
print(f"✅ Saved transactions_clean.csv")

print("\n" + "=" * 60)
print("CLEANING SUMMARY")
print("=" * 60)
print(f"Original rows:        {len(df):,}")
print(f"Removed (returns):    {(df['quantity'] <= 0).sum():,}")
print(f"Removed (bad price):  {(df['price'] <= 0).sum():,}")
print(f"Removed (no cust ID): {df['customer_id'].isna().sum():,}")
print(f"Final clean rows:     {len(df_clean):,}")