import pandas as pd
from load_data import read_csv_file

# Load sample data
df = read_csv_file('../files/customers-100.csv')

# Basic aggregation functions
print("=== BASIC AGGREGATIONS ===")
print(f"Count: {df['Index'].count()}")
print(f"Sum: {df['Index'].sum()}")
print(f"Mean: {df['Index'].mean()}")
print(f"Median: {df['Index'].median()}")
print(f"Standard Deviation: {df['Index'].std()}")
print(f"Min: {df['Index'].min()}")
print(f"Max: {df['Index'].max()}")

# Group by operations
print("\n=== GROUP BY OPERATIONS ===")
if 'Country' in df.columns:
    country_stats = df.groupby('Country').agg({
        'Index': ['count', 'mean', 'sum'],
        'Customer Id': 'count'
    })
    print(country_stats.head())

# Multiple aggregations
print("\n=== MULTIPLE AGGREGATIONS ===")
aggregations = df.agg({
    'Index': ['count', 'mean', 'sum'],
    'Customer Id': ['count', 'nunique']
})
print(aggregations)

# Custom aggregation function
def custom_range(x):
    return x.max() - x.min()

print("\n=== CUSTOM AGGREGATION ===")
custom_agg = df['Index'].agg(custom_range)
print(f"Custom range: {custom_agg}")

# Pivot table
print("\n=== PIVOT TABLE ===")
if 'Country' in df.columns and 'City' in df.columns:
    pivot = df.pivot_table(
        values='Index',
        index='Country',
        columns='City',
        aggfunc='mean',
        fill_value=0
    )
    print(pivot.head())

# Rolling window calculations
print("\n=== ROLLING WINDOW ===")
df_sorted = df.sort_values('Index')
df_sorted['rolling_mean'] = df_sorted['Index'].rolling(window=3).mean()
print(df_sorted[['Index', 'rolling_mean']].head(10))

# Cumulative operations
print("\n=== CUMULATIVE OPERATIONS ===")
df_sorted['cumsum'] = df_sorted['Index'].cumsum()
df_sorted['cumprod'] = df_sorted['Index'].cumprod()
print(df_sorted[['Index', 'cumsum', 'cumprod']].head(10))
