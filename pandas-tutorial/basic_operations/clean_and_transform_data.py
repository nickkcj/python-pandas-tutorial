from visualize_data import df

df.dropna() # Remove rows with any NaN values
df.fillna(0) # Replace NaN values with 0
df['column_name'].fillna(df['column_name'].mean(), inplace=True) # Replace

