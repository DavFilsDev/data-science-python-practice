# pandas_selection.py
# ================================================
# This file demonstrates how to select data in a DataFrame
# using labels (.loc), index positions (.iloc), and conditions.

import pandas as pd

# Sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'Age': [25, 30, 35, 40],
    'City': ['Paris', 'Berlin', 'Madrid', 'Rome']
}
df = pd.DataFrame(data)

# ---------------------------
# 1. Select a column
print("Select 'Name' column:\n", df['Name'])

# ---------------------------
# 2. Select multiple columns
print("\nSelect 'Name' and 'City':\n", df[['Name', 'City']])

# ---------------------------
# 3. Select a row by index label using .loc
print("\nSelect row at index 1 with .loc:\n", df.loc[1])

# ---------------------------
# 4. Select a row by position using .iloc
print("\nSelect row at position 2 with .iloc:\n", df.iloc[2])

# ---------------------------
# 5. Select multiple rows and columns
print("\nSelect rows 1 to 2 and columns 'Name' and 'Age':\n", df.loc[1:2, ['Name', 'Age']])

# ---------------------------
# 6. Conditional filtering
print("\nRows where Age > 30:\n", df[df['Age'] > 30])

# ---------------------------
# 7. Combined conditions (use & and | with parentheses)
print("\nRows where Age > 30 AND City is 'Rome':\n", df[(df['Age'] > 30) & (df['City'] == 'Rome')])
