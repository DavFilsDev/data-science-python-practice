# numpy_array_operations.py
# ===============================
# This file explains how to perform arithmetic and element-wise operations on NumPy arrays.

import numpy as np

# Create two 1D arrays
a = np.array([10, 20, 30, 40])
b = np.array([1, 2, 3, 4])

# ---------------------------
# 1. Element-wise Arithmetic Operations
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

# ---------------------------
# 2. Element-wise Power
print("\nExponentiation:", a ** 2)

# ---------------------------
# 3. Scalar Operations (apply the operation to every element)
print("\nAdd 10 to each element:", a + 10)
print("Multiply each element by 5:", a * 5)

# ---------------------------
# 4. Useful Mathematical Functions
print("\nSquare root of a:", np.sqrt(a))
print("Sine of b:", np.sin(b))
print("Natural log of a:", np.log(a))
print("Sum of a:", np.sum(a))
print("Maximum value in b:", np.max(b))
