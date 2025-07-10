# numpy_broadcasting.py
# ===============================
# This file explains how broadcasting works in NumPy.

import numpy as np

# ---------------------------
# 1. Adding a scalar to an array (broadcasting the scalar)
arr = np.array([[1, 2, 3],
                [4, 5, 6]])

print("Original Array:\n", arr)
print("\nAdd 10 to each element:\n", arr + 10)

# ---------------------------
# 2. Broadcasting a 1D array to a 2D array
arr2 = np.array([[10, 20, 30],
                 [40, 50, 60]])

row = np.array([1, 2, 3])  # Shape (3,)

# NumPy will automatically stretch the 1D row across the rows of arr2
result = arr2 + row

print("\nBroadcasting Row Addition:\n", result)

# ---------------------------
# 3. Broadcasting column-wise (reshape needed)
col = np.array([10, 20]).reshape((2, 1))  # Shape (2, 1)

result2 = arr2 + col
print("\nBroadcasting Column Addition:\n", result2)
