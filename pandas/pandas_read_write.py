# pandas_read_write.py
# =========================================
# This file shows how to read and write data files using Pandas.

import pandas as pd

# ---------------------------
# 1. Create a sample DataFrame
data = {
    'Name': ['Anna', 'Ben', 'Chris'],
    'Age': [23, 34, 45],
    'Country': ['France', 'Germany', 'Spain']
}
df = pd.DataFrame(data)

# ---------------------------
# 2. Save DataFrame to a CSV file
df.to_csv('sample_data.csv', index=False)
print("CSV file 'sample_data.csv' created.")

# ---------------------------
# 3. Read CSV file into a DataFrame
df_csv = pd.read_csv('sample_data.csv')
print("\nDataFrame read from CSV:\n", df_csv)

# ---------------------------
# 4. Save to Excel (you need openpyxl or xlsxwriter installed)
df.to_excel('sample_data.xlsx', index=False)
print("\nExcel file 'sample_data.xlsx' created.")

# ---------------------------
# 5. Read Excel file back into a DataFrame
df_excel = pd.read_excel('sample_data.xlsx')
print("\nDataFrame read from Excel:\n", df_excel)
