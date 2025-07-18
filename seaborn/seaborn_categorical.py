# seaborn_categorical.py
# =====================================================
# This file demonstrates categorical plots in Seaborn:
# barplot, countplot, and boxplot.

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Sample categorical data
data = pd.DataFrame({
    'Category': ['A', 'B', 'A', 'C', 'B', 'A', 'C', 'C', 'B', 'A'],
    'Values': [5, 6, 7, 5, 8, 9, 6, 7, 5, 8]
})

# ---------------------------
# 1. Barplot - mean value per category
sns.barplot(x='Category', y='Values', data=data)
plt.title("Barplot of Mean Values by Category")
plt.show()

# ---------------------------
# 2. Countplot - count of each category
sns.countplot(x='Category', data=data)
plt.title("Count of Each Category")
plt.show()

# ---------------------------
# 3. Boxplot - distribution of values by category
sns.boxplot(x='Category', y='Values', data=data)
plt.title("Boxplot of Values by Category")
plt.show()
