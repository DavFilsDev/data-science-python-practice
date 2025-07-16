# matplotlib_hist_scatter.py
# ===============================================================
# This file demonstrates how to plot histograms and scatter plots using Matplotlib.

import matplotlib.pyplot as plt
import numpy as np

# ---------------------------
# 1. Histogram - Distribution of ages
ages = [22, 25, 30, 22, 24, 28, 33, 35, 29, 40, 42, 22, 31, 36, 38]

plt.figure(figsize=(6, 4))
plt.hist(ages, bins=6, color='skyblue', edgecolor='black')
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.grid(True)
plt.tight_layout()
plt.show()

# ---------------------------
# 2. Scatter plot - Height vs Weight
np.random.seed(0)
height = np.random.normal(170, 10, 50)
weight = np.random.normal(65, 8, 50)

plt.figure(figsize=(6, 4))
plt.scatter(height, weight, color='green', alpha=0.7)
plt.title("Height vs Weight")
plt.xlabel("Height (cm)")
plt.ylabel("Weight (kg)")
plt.grid(True)
plt.tight_layout()
plt.show()
