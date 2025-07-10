# numpy_statistics.py
# ===============================
# This file shows how to use NumPy for basic statistical calculations.

import numpy as np

# Example 1D array
data = np.array([10, 20, 30, 40, 50, 60, 70])

# ---------------------------
# 1. Basic statistics
print("Sum:", np.sum(data))
print("Mean (average):", np.mean(data))
print("Median:", np.median(data))
print("Standard Deviation:", np.std(data))
print("Variance:", np.var(data))
print("Minimum:", np.min(data))
print("Maximum:", np.max(data))

# ---------------------------
# 2. Apply statistics on 2D arrays
matrix = np.array([[1, 2, 3],
                   [4, 5, 6]])

# Sum across rows (axis=1)
print("\nRow-wise Sum:", np.sum(matrix, axis=1))

# Mean across columns (axis=0)
print("Column-wise Mean:", np.mean(matrix, axis=0))
