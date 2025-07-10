# numpy_reshape.py
# ===============================
# This file explains how to change the shape of arrays and concatenate them.

import numpy as np

# ---------------------------
# 1. Reshape a 1D array into a 2D array
arr = np.arange(1, 13)  # Creates array [1 2 3 ... 12]
reshaped = arr.reshape((3, 4))  # 3 rows, 4 columns
print("Reshaped Array (3x4):\n", reshaped)

# ---------------------------
# 2. Flatten a 2D array into a 1D array
flattened = reshaped.flatten()
print("\nFlattened Array:", flattened)

# ---------------------------
# 3. Concatenate arrays along different axes
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

# Horizontal concatenation (axis=1)
concat_h = np.concatenate((a, b), axis=1)
print("\nHorizontal Concatenation:\n", concat_h)

# Vertical concatenation (axis=0)
concat_v = np.concatenate((a, b), axis=0)
print("\nVertical Concatenation:\n", concat_v)
