from load_data import read_csv_file

df = read_csv_file('files/customers-100.csv')

print(df.head()) # Display the first few rows of the DataFrame
print(df.tail())  # Display the last few rows of the DataFrame
print(df.shape())  # Display the shape of the DataFrame
print(df.info())  # Display a concise summary of the DataFrame

