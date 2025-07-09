# numpy_intro.py
# ===============================
# This file introduces NumPy and explains how to create arrays and explore their properties.

# Import the numpy library
import numpy as np

# ---------------------------
# 1. Create a 1D NumPy Array
# ---------------------------
# NumPy arrays are created using np.array()
arr1 = np.array([1, 2, 3, 4, 5])
print("1D Array:", arr1)

# ---------------------------
# 2. Create a 2D NumPy Array (Matrix)
arr2 = np.array([[1, 2, 3],
                 [4, 5, 6]])
print("\n2D Array:\n", arr2)

# ---------------------------
# 3. Arrays filled with zeros
zeros_array = np.zeros((2, 3))  # 2 rows, 3 columns
print("\nArray of Zeros:\n", zeros_array)

# ---------------------------
# 4. Arrays filled with ones
ones_array = np.ones((3, 4))  # 3 rows, 4 columns
print("\nArray of Ones:\n", ones_array)

# ---------------------------
# 5. Array with a range of numbers
range_array = np.arange(0, 10, 2)  # Start at 0, stop before 10, step by 2
print("\nRange Array:", range_array)

# ---------------------------
# 6. Array with equally spaced numbers
linspace_array = np.linspace(0, 1, 5)  # 5 numbers between 0 and 1
print("\nLinspace Array:", linspace_array)

# ---------------------------
# 7. Array properties
print("\nShape of arr2:", arr2.shape)  # Shows (rows, columns)
print("Data type of arr2:", arr2.dtype)  # Shows the type of elements
print("Number of dimensions in arr2:", arr2.ndim)
