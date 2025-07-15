# matplotlib_subplot.py
# ========================================================
# This file demonstrates how to use subplots in Matplotlib.

import matplotlib.pyplot as plt

# Sample data
x = [0, 1, 2, 3, 4]
y1 = [i**2 for i in x]
y2 = [i**3 for i in x]

# ---------------------------
# 1. Create two subplots (1 row, 2 columns)
fig, axs = plt.subplots(1, 2, figsize=(10, 4))

# First plot (square)
axs[0].plot(x, y1, color='green')
axs[0].set_title("Square")
axs[0].set_xlabel("X")
axs[0].set_ylabel("X²")

# Second plot (cube)
axs[1].plot(x, y2, color='purple')
axs[1].set_title("Cube")
axs[1].set_xlabel("X")
axs[1].set_ylabel("X³")

# Add spacing between subplots
plt.tight_layout()
plt.show()
