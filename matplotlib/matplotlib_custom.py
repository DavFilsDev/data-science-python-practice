# matplotlib_custom.py
# ===============================================================
# This file shows how to customize axis ticks, limits, legends, and figure size.

import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y1 = [10, 15, 20, 25, 30]
y2 = [30, 25, 20, 15, 10]

# Create a custom-sized figure
plt.figure(figsize=(8, 5))

# Plot two lines
plt.plot(x, y1, label="Ascending", color='blue', marker='o')
plt.plot(x, y2, label="Descending", color='red', marker='s')

# Add custom x/y ticks
plt.xticks([1, 2, 3, 4, 5])
plt.yticks(range(10, 35, 5))

# Set axis limits
plt.xlim(0, 6)
plt.ylim(5, 35)

# Add labels and title
plt.xlabel("Step")
plt.ylabel("Value")
plt.title("Custom Axis, Ticks, and Legend")

# Add legend and grid
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
