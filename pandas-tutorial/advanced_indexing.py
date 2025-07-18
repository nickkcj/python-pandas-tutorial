import pandas as pd
import numpy as np

# Advanced indexing and selection techniques
print("=== ADVANCED INDEXING ===")

# Create multi-dimensional sample data
np.random.seed(42)
dates = pd.date_range('2023-01-01', periods=100, freq='D')
companies = ['AAPL', 'GOOGL', 'MSFT', 'AMZN']
data = []

for date in dates[:20]:  # Use first 20 dates for simplicity
    for company in companies:
        data.append({
            'date': date,
            'company': company,
            'price': np.random.uniform(100, 500),
            'volume': np.random.randint(1000, 10000),
            'sector': np.random.choice(['Tech', 'Finance', 'Healthcare'])
        })

df = pd.DataFrame(data)
print(f"Sample data:\n{df.head()}")

# MultiIndex creation
print("\n=== MULTIINDEX ===")
df_multi = df.set_index(['date', 'company'])
print(f"MultiIndex DataFrame:\n{df_multi.head()}")

# MultiIndex selection
print("\n=== MULTIINDEX SELECTION ===")
# Select specific date and company
specific_selection = df_multi.loc[('2023-01-01', 'AAPL')]
print(f"Specific selection:\n{specific_selection}")

# Select all companies for a specific date
date_selection = df_multi.loc['2023-01-01']
print(f"All companies for 2023-01-01:\n{date_selection}")

# Select specific company across all dates
company_selection = df_multi.loc[(slice(None), 'AAPL'), :]
print(f"AAPL across all dates:\n{company_selection.head()}")

# Cross-section selection
print("\n=== CROSS-SECTION SELECTION ===")
cross_section = df_multi.xs('AAPL', level='company')
print(f"Cross-section for AAPL:\n{cross_section.head()}")

# Boolean indexing with MultiIndex
print("\n=== BOOLEAN INDEXING WITH MULTIINDEX ===")
high_volume = df_multi[df_multi['volume'] > 5000]
print(f"High volume trades:\n{high_volume.head()}")

# Query with MultiIndex
print("\n=== QUERY WITH MULTIINDEX ===")
query_result = df_multi.query('volume > 5000 and price < 300')
print(f"Query result:\n{query_result.head()}")

# Index slicing
print("\n=== INDEX SLICING ===")
# Slice by date range
date_slice = df_multi.loc['2023-01-01':'2023-01-03']
print(f"Date slice:\n{date_slice.head()}")

# Hierarchical indexing operations
print("\n=== HIERARCHICAL OPERATIONS ===")
# Group by level
level_stats = df_multi.groupby(level='company').agg({
    'price': ['mean', 'std'],
    'volume': ['sum', 'count']
})
print(f"Stats by company:\n{level_stats}")

# Unstack and stack
print("\n=== UNSTACK AND STACK ===")
unstacked = df_multi['price'].unstack(level='company')
print(f"Unstacked prices:\n{unstacked.head()}")

stacked = unstacked.stack()
print(f"Stacked back:\n{stacked.head()}")

# Pivot operations
print("\n=== PIVOT OPERATIONS ===")
pivot_table = df.pivot_table(
    values='price',
    index='date',
    columns='company',
    aggfunc='mean'
)
print(f"Pivot table:\n{pivot_table.head()}")

# Advanced loc and iloc
print("\n=== ADVANCED LOC AND ILOC ===")
# Conditional selection with loc
condition_loc = df.loc[df['price'] > 300, ['company', 'price', 'volume']]
print(f"Conditional loc:\n{condition_loc.head()}")

# Multiple column selection with iloc
iloc_selection = df.iloc[:5, [0, 2, 3]]  # First 5 rows, columns 0, 2, 3
print(f"Iloc selection:\n{iloc_selection}")

# Index alignment
print("\n=== INDEX ALIGNMENT ===")
df1 = pd.DataFrame({'A': [1, 2, 3]}, index=[1, 2, 3])
df2 = pd.DataFrame({'B': [4, 5, 6, 7]}, index=[2, 3, 4, 5])

# Automatic alignment
aligned_sum = df1['A'] + df2['B']
print(f"Aligned sum:\n{aligned_sum}")

# Reindexing
print("\n=== REINDEXING ===")
new_index = pd.date_range('2023-01-01', periods=5, freq='D')
df_subset = df.head(5).set_index('date')
reindexed = df_subset.reindex(new_index, method='ffill')
print(f"Reindexed DataFrame:\n{reindexed}")

# Advanced filtering techniques
print("\n=== ADVANCED FILTERING ===")
# Filter using isin
companies_of_interest = ['AAPL', 'GOOGL']
filtered = df[df['company'].isin(companies_of_interest)]
print(f"Filtered companies:\n{filtered.head()}")

# Filter using where
where_result = df.where(df['price'] > 300).dropna()
print(f"Where result:\n{where_result.head()}")

# Filter using mask (opposite of where)
mask_result = df.mask(df['price'] > 300).dropna()
print(f"Mask result:\n{mask_result.head()}")

print("\nAdvanced indexing tips:")
print("1. Use MultiIndex for hierarchical data")
print("2. Use xs() for cross-section selection")
print("3. Use query() for complex conditions")
print("4. Understand index alignment in operations")
print("5. Use stack/unstack for reshaping")
print("6. Use pivot_table for data summarization")
print("7. Use reindex for changing index structure")
