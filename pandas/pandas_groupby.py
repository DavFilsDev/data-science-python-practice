# pandas_groupby.py
# ========================================================
# This file shows how to group data in Pandas using .groupby()
# and how to perform aggregate operations.

import pandas as pd

# Sample DataFrame with repeated categories
data = {
    'Department': ['IT', 'HR', 'IT', 'HR', 'Finance', 'IT'],
    'Employee': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank'],
    'Salary': [60000, 50000, 65000, 52000, 58000, 62000],
    'Age': [25, 30, 28, 32, 41, 29]
}
df = pd.DataFrame(data)
print("Original DataFrame:\n", df)

# ---------------------------
# 1. Group by one column
grouped = df.groupby('Department')
print("\nGrouped by Department (object):", grouped)

# ---------------------------
# 2. Aggregate functions on Salary by Department
salary_mean = grouped['Salary'].mean()
print("\nAverage salary by department:\n", salary_mean)

# ---------------------------
# 3. Aggregate multiple statistics
agg_stats = grouped['Salary'].agg(['min', 'max', 'mean', 'sum'])
print("\nSalary statistics by department:\n", agg_stats)

# ---------------------------
# 4. Group by multiple columns (example)
multi_group = df.groupby(['Department', 'Age'])['Salary'].mean()
print("\nGrouped by Department and Age:\n", multi_group)

# ---------------------------
# 5. Reset index after groupby (optional)
agg_reset = agg_stats.reset_index()
print("\nReset index:\n", agg_reset)
