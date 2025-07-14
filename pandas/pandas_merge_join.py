# pandas_merge_join.py
# =====================================================
# This file explains how to merge, join, and concatenate DataFrames in Pandas.

import pandas as pd

# ---------------------------
# 1. Merge (similar to SQL JOIN)
employees = pd.DataFrame({
    'EmpID': [1, 2, 3, 4],
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'DeptID': [101, 102, 101, 103]
})

departments = pd.DataFrame({
    'DeptID': [101, 102, 103],
    'Department': ['IT', 'HR', 'Finance']
})

merged_df = pd.merge(employees, departments, on='DeptID')
print("Merged DataFrame (inner join by DeptID):\n", merged_df)

# ---------------------------
# 2. Different types of joins
left_join = pd.merge(employees, departments, on='DeptID', how='left')
right_join = pd.merge(employees, departments, on='DeptID', how='right')
outer_join = pd.merge(employees, departments, on='DeptID', how='outer')

print("\nLeft Join:\n", left_join)
print("\nRight Join:\n", right_join)
print("\nOuter Join:\n", outer_join)

# ---------------------------
# 3. Concatenation (stack DataFrames)
df1 = pd.DataFrame({'A': ['A0', 'A1'], 'B': ['B0', 'B1']})
df2 = pd.DataFrame({'A': ['A2', 'A3'], 'B': ['B2', 'B3']})

concat_rows = pd.concat([df1, df2], axis=0)
concat_cols = pd.concat([df1, df2], axis=1)

print("\nConcatenation by rows:\n", concat_rows)
print("\nConcatenation by columns:\n", concat_cols)
