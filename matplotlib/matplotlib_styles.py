# matplotlib_styles.py
# ===================================================
# This file demonstrates how to customize line styles, colors, and markers.

import matplotlib.pyplot as plt

# Sample data
x = [0, 1, 2, 3, 4]
y1 = [0, 1, 4, 9, 16]
y2 = [0, 2, 8, 18, 32]

# ---------------------------
# 1. Line color and style
plt.plot(x, y1, color='blue', linestyle='--', linewidth=2, label='Dashed Blue')

# ---------------------------
# 2. Adding markers
plt.plot(x, y2, color='red', marker='o', linestyle='-', linewidth=2, label='Red with circles')

# ---------------------------
# 3. Add labels, legend, and grid
plt.title("Styled Line Plots")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.legend()
plt.grid(True)
plt.show()
