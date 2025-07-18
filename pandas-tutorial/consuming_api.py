# import requests
# import zipfile

# with zipfile.ZipFile('/home/nickcj/titanic.zip', 'r') as zip_ref:
#     zip_ref.extractall('titanic_data')


import pandas as pd
import requests

df = pd.read_csv('titanic_data/train_and_test2.csv')
print(df.head())



url = "https://api.spacexdata.com/v4/launches"
data = requests.get(url).json()
df = pd.json_normalize(data)
print(df[['name', 'date_utc', 'success']].head())




