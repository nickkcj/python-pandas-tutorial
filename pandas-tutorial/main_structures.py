import pandas as pd

# Series is a one-dimensional labeled array capable of holding any data type
s = pd.Series([1, 2, 3, 4, 5], name='numbers')

print(s)



data = {
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35],
    'city': ['New York', 'Los Angeles', 'Chicago']}


# Dataframe is a 2D labeled data structure with columns of potentially different types
# It is similar to a spreadsheet or SQL table
df = pd.DataFrame(data)
print(df)
