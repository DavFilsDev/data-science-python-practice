# pandas_datetime.py
# ====================================================
# This file shows how to work with date and time data using Pandas.

import pandas as pd

# ---------------------------
# 1. Create a DataFrame with dates as strings
data = {
    'Event': ['Login', 'Logout', 'Login', 'Logout'],
    'Date': ['2023-07-01 08:30:00', '2023-07-01 17:45:00',
             '2023-07-02 09:00:00', '2023-07-02 18:00:00']
}
df = pd.DataFrame(data)
print("Original DataFrame:\n", df)

# ---------------------------
# 2. Convert the 'Date' column to datetime objects
df['Date'] = pd.to_datetime(df['Date'])
print("\nAfter converting 'Date' to datetime:\n", df)

# ---------------------------
# 3. Extract components (year, month, day, hour)
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Hour'] = df['Date'].dt.hour

print("\nDate components extracted:\n", df)

# ---------------------------
# 4. Filter rows based on date
filtered = df[df['Date'] > '2023-07-01 12:00:00']
print("\nEvents after July 1st, noon:\n", filtered)

# ---------------------------
# 5. Set datetime column as index
df = df.set_index('Date')
print("\nDataFrame with datetime index:\n", df)

# ---------------------------
# 6. Resample by day (count events per day)
daily_events = df.resample('D').count()
print("\nResampled daily event counts:\n", daily_events)
