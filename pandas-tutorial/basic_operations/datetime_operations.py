import pandas as pd
import numpy as np

# Date and time operations
print("=== DATE AND TIME OPERATIONS ===")

# Create date range
dates = pd.date_range('2023-01-01', periods=100, freq='D')
print(f"Date range: {dates[:5]}")

# Create DataFrame with datetime
df = pd.DataFrame({
    'date': dates,
    'value': np.random.randn(100),
    'category': np.random.choice(['A', 'B', 'C'], 100)
})

print(f"\nDataFrame with dates:\n{df.head()}")

# Extract date components
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df['day'] = df['date'].dt.day
df['day_of_week'] = df['date'].dt.dayofweek
df['day_name'] = df['date'].dt.day_name()

print(f"\nDate components:\n{df[['date', 'year', 'month', 'day', 'day_name']].head()}")

# Set date as index
df_indexed = df.set_index('date')
print(f"\nDataFrame with date index:\n{df_indexed.head()}")

# Resample data (time series resampling)
print("\n=== RESAMPLING ===")
monthly_mean = df_indexed.resample('M')['value'].mean()
print(f"Monthly mean:\n{monthly_mean.head()}")

weekly_sum = df_indexed.resample('W')['value'].sum()
print(f"Weekly sum:\n{weekly_sum.head()}")

# Time zone operations
print("\n=== TIME ZONE OPERATIONS ===")
df_tz = df.copy()
df_tz['date'] = pd.to_datetime(df_tz['date'])
df_tz['date_utc'] = df_tz['date'].dt.tz_localize('UTC')
df_tz['date_ny'] = df_tz['date_utc'].dt.tz_convert('America/New_York')

print(f"Time zone conversions:\n{df_tz[['date', 'date_utc', 'date_ny']].head()}")

# Date filtering
print("\n=== DATE FILTERING ===")
recent_data = df_indexed['2023-02-01':'2023-02-28']
print(f"February data:\n{recent_data.head()}")

# Business day operations
print("\n=== BUSINESS DAY OPERATIONS ===")
business_days = pd.bdate_range('2023-01-01', periods=50)
print(f"Business days: {business_days[:5]}")

# Date arithmetic
print("\n=== DATE ARITHMETIC ===")
df['days_from_start'] = (df['date'] - df['date'].min()).dt.days
df['future_date'] = df['date'] + pd.Timedelta(days=30)
print(f"Date arithmetic:\n{df[['date', 'days_from_start', 'future_date']].head()}")

# Lag and lead operations
print("\n=== LAG AND LEAD ===")
df_indexed['value_lag1'] = df_indexed['value'].shift(1)
df_indexed['value_lead1'] = df_indexed['value'].shift(-1)
print(f"Lag and lead:\n{df_indexed[['value', 'value_lag1', 'value_lead1']].head()}")
