# seaborn_intro.py
# =====================================================
# This file introduces basic plotting with Seaborn.

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Sample data
np.random.seed(0)
data = pd.DataFrame({
    'x': np.arange(50),
    'y': np.random.randn(50).cumsum(),
    'z': np.random.randint(1, 5, 50)
})

# ---------------------------
# 1. Scatter plot
sns.scatterplot(data=data, x='x', y='y')
plt.title("Basic Scatter Plot")
plt.show()

# ---------------------------
# 2. Line plot
sns.lineplot(data=data, x='x', y='y')
plt.title("Basic Line Plot")
plt.show()

# ---------------------------
# 3. Histogram
sns.histplot(data=data, x='y', bins=10, kde=True)
plt.title("Histogram with KDE")
plt.show()
