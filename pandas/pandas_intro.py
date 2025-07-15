# pandas_intro.py
# ===================================
# This file introduces Pandas and demonstrates how to create Series and DataFrames.

import pandas as pd

# ---------------------------
# 1. Create a Series (like a column of data)
data = [10, 20, 30, 40]
series = pd.Series(data)
print("Series:\n", series)

# With custom indexes
series2 = pd.Series([100, 200, 300], index=['a', 'b', 'c'])
print("\nSeries with custom index:\n", series2)

# ---------------------------
# 2. Create a DataFrame from a dictionary
data_dict = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['Paris', 'London', 'Berlin']
}
df = pd.DataFrame(data_dict)
print("\nDataFrame from dict:\n", df)

# ---------------------------
# 3. Create a DataFrame from a list of lists
data_list = [
    ['Tom', 28],
    ['Jerry', 22],
    ['Spike', 31]
]
df2 = pd.DataFrame(data_list, columns=['Name', 'Age'])
print("\nDataFrame from list of lists:\n", df2)

# ---------------------------
# 4. Basic DataFrame attributes
print("\nColumn Names:", df.columns.tolist())
print("Row Index:", df.index)
print("Data Types:\n", df.dtypes)
