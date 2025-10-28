import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. Load dataset (header already fixed)
df = pd.read_csv('dataset.csv', header=3)

# 2. Drop empty rows and columns
df = df.dropna(how='all')  # remove completely empty rows
df = df.drop(columns=['Unnamed: 0'], errors='ignore')  # drop useless unnamed col

# 3. Convert numeric columns
numeric_cols = ['unique_idfas', 'unique_ips', 'unique_uas', 'total_requests',
                'requests_per_idfa', 'impressions', 'impressions_per_idfa',
                'idfa_ip_ratio', 'idfa_ua_ratio', 'IVT']

for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# 4. Quick look
print("\n Cleaned DataFrame:")
print(df.head())

# 5. Summary
print("\nShape:", df.shape)
print("\nMissing values per column:\n", df.isna().sum())
print("\nNumeric Summary:\n", df.describe().T)

# 6. Value counts for Date
print("\nTop Dates:")
print(df['Date'].value_counts().head(10))

# 7. Example plot
plt.figure(figsize=(8, 5))
df['unique_idfas'].hist(bins=30)
plt.title('Distribution of Unique IDFAs')
plt.xlabel('unique_idfas')
plt.ylabel('Count')
plt.savefig('unique_idfas_hist.png', bbox_inches='tight')
plt.show()

