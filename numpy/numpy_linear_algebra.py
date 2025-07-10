# numpy_linear_algebra.py
# ===============================
# This file explains some basic linear algebra operations with NumPy.

import numpy as np

# ---------------------------
# 1. Dot product (1D arrays)
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

dot_product = np.dot(a, b)  # or a @ b in 1D
print("Dot Product of a and b:", dot_product)

# ---------------------------
# 2. Matrix multiplication (2D arrays)
matrix1 = np.array([[1, 2],
                    [3, 4]])
matrix2 = np.array([[5, 6],
                    [7, 8]])

# Matrix multiplication
product = np.matmul(matrix1, matrix2)
# Or equivalently:
# product = matrix1 @ matrix2

print("\nMatrix Multiplication Result:\n", product)

# ---------------------------
# 3. Transpose of a matrix
transpose = matrix1.T
print("\nTranspose of matrix1:\n", transpose)

# ---------------------------
# 4. Determinant (for square matrices)
det = np.linalg.det(matrix2)
print("\nDeterminant of matrix2:", det)

# ---------------------------
# 5. Inverse of a matrix (if invertible)
inverse = np.linalg.inv(matrix2)
print("\nInverse of matrix2:\n", inverse)
