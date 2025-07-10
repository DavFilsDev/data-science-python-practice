# numpy_random.py
# ===============================
# This file shows how to create random numbers using NumPy.

import numpy as np

# ---------------------------
# 1. Random integers between 0 and 9
random_integers = np.random.randint(0, 10, size=(3, 4))
print("Random Integers:\n", random_integers)

# ---------------------------
# 2. Random floats between 0.0 and 1.0
random_floats = np.random.rand(2, 5)
print("\nRandom Floats:\n", random_floats)

# ---------------------------
# 3. Random numbers from a normal distribution (mean=0, std=1)
normal_dist = np.random.randn(4, 4)
print("\nRandom Normal Distribution:\n", normal_dist)

# ---------------------------
# 4. Shuffling an array
arr = np.arange(10)
np.random.shuffle(arr)
print("\nShuffled Array:", arr)

# ---------------------------
# 5. Random choice from a list
choices = np.random.choice(['apple', 'banana', 'cherry'], size=5)
print("\nRandom Choices:", choices)
