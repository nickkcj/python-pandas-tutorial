from load_data import read_csv_file

df = read_csv_file('files/customers-100.csv')

df[df['Subscription Date'] > '2020-01-01']  # Filter rows where Subscription Date is after 2020-01-01

df.groupby('City').mean()  # Group by City and calculate the mean of each group
df['Country'].describe()  # Get descriptive statistics for the 'Country' column

import matplotlib.pyplot as plt

df['City'].hist()
plt.show()  # Plot a histogram of the 'City' column