# numpy_indexing.py
# ===============================
# This file explains how to access and modify elements in a NumPy array.

import numpy as np

# Create a 2D array
matrix = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

# ---------------------------
# 1. Accessing elements
print("Element at row 0, column 1:", matrix[0, 1])  # Should print 20

# ---------------------------
# 2. Slicing rows and columns
print("\nFirst two rows:\n", matrix[:2, :])  # Rows 0 and 1, all columns
print("\nLast column:\n", matrix[:, -1])     # All rows, last column

# ---------------------------
# 3. Modifying elements
matrix[1, 1] = 555  # Change the element at row 1, column 1
print("\nModified matrix:\n", matrix)

# ---------------------------
# 4. Boolean Indexing (Filtering)
# Find all elements > 50
print("\nElements greater than 50:\n", matrix[matrix > 50])

# ---------------------------
# 5. Fancy Indexing (Advanced Indexing)
# Select rows at positions 0 and 2
print("\nFancy Indexing (rows 0 and 2):\n", matrix[[0, 2]])
