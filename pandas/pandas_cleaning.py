# pandas_cleaning.py
# =================================================
# This file covers basic data cleaning techniques in Pandas:
# handling missing values, duplicates, renaming, and type conversion.

import pandas as pd
import numpy as np

# Create a sample DataFrame with some issues
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Bob', None],
    'Age': [25, 30, None, 30, 22],
    'City': ['Paris', None, 'Madrid', 'Berlin', 'Paris']
}
df = pd.DataFrame(data)
print("Original DataFrame:\n", df)

# ---------------------------
# 1. Detect missing values
print("\nMissing values per column:\n", df.isnull().sum())

# ---------------------------
# 2. Drop rows with any missing values
df_dropped = df.dropna()
print("\nAfter dropping rows with missing values:\n", df_dropped)

# ---------------------------
# 3. Fill missing values
df_filled = df.fillna({
    'Name': 'Unknown',
    'Age': df['Age'].mean(),
    'City': 'Unknown'
})
print("\nAfter filling missing values:\n", df_filled)

# ---------------------------
# 4. Remove duplicates
df_no_duplicates = df_filled.drop_duplicates()
print("\nAfter removing duplicates:\n", df_no_duplicates)

# ---------------------------
# 5. Rename columns
df_renamed = df_filled.rename(columns={
    'Name': 'Full Name',
    'Age': 'Age (Years)'
})
print("\nAfter renaming columns:\n", df_renamed)

# ---------------------------
# 6. Change data type of a column
df_renamed['Age (Years)'] = df_renamed['Age (Years)'].astype(int)
print("\nAfter converting 'Age (Years)' to int:\n", df_renamed)
print("Data types:\n", df_renamed.dtypes)
