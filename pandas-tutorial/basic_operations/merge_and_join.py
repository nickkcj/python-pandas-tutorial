import pandas as pd
from load_data import read_csv_file

# Load sample data
customers_df = read_csv_file('../files/customers-100.csv')
products_df = read_csv_file('../files/products-100.csv')

# Create sample data for demonstration
orders_data = {
    'order_id': [1, 2, 3, 4, 5],
    'customer_id': [1, 2, 3, 1, 4],
    'product_id': [101, 102, 103, 104, 105],
    'quantity': [2, 1, 3, 1, 2],
    'order_date': ['2023-01-15', '2023-01-16', '2023-01-17', '2023-01-18', '2023-01-19']
}
orders_df = pd.DataFrame(orders_data)

# Different types of joins
inner_join = pd.merge(customers_df, orders_df, left_on='Index', right_on='customer_id', how='inner')
print(inner_join.head())

left_join = pd.merge(customers_df, orders_df, left_on='Index', right_on='customer_id', how='left')
print(left_join.head())

right_join = pd.merge(customers_df, orders_df, left_on='Index', right_on='customer_id', how='right')
print(right_join.head())

outer_join = pd.merge(customers_df, orders_df, left_on='Index', right_on='customer_id', how='outer')
print(outer_join.head())

# Concatenation
concatenated = pd.concat([customers_df.head(3), customers_df.tail(3)])
print(concatenated)

# Join on index
df1 = pd.DataFrame({'A': [1, 2, 3]}, index=[1, 2, 3])
df2 = pd.DataFrame({'B': [4, 5, 6]}, index=[1, 2, 3])
joined = df1.join(df2)
print(joined)
