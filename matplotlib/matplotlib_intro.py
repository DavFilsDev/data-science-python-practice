# matplotlib_intro.py
# ====================================================
# This file introduces the basics of plotting with Matplotlib.

import matplotlib.pyplot as plt

# ---------------------------
# 1. Basic line plot
x = [0, 1, 2, 3, 4]
y = [0, 1, 4, 9, 16]

plt.plot(x, y)
plt.title("Basic Line Plot")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.grid(True)
plt.show()

# ---------------------------
# 2. Saving the figure to a file
plt.plot(x, y)
plt.title("Saved Line Plot")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.savefig("saved_plot.png")  # Saves the plot to a file
print("Figure saved as 'saved_plot.png'")
