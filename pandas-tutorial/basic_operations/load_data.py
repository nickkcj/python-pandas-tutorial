import pandas as pd

def read_csv_file(file_path):
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        print(f"Error reading the CSV file: {e}")
        return None
    

def read_excel_file(file_path):
    try:
        df = pd.read_excel(file_path)
        return df
    except Exception as e:
        print(f"Error reading the Excel file: {e}")
        return None
    

def read_sql(query, connection):
    try:
        df = pd.read_sql(query, connection)
        return df
    except Exception as e:
        print(f"Error executing SQL query: {e}")
        return None