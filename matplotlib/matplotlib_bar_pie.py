# matplotlib_bar_pie.py
# ========================================================
# This file demonstrates how to create bar charts and pie charts in Matplotlib.

import matplotlib.pyplot as plt

# ---------------------------
# 1. Bar chart - Sales by product
products = ['Apples', 'Bananas', 'Cherries', 'Dates']
sales = [50, 75, 30, 45]

plt.figure(figsize=(6, 4))
plt.bar(products, sales, color='orange')
plt.title("Product Sales")
plt.xlabel("Product")
plt.ylabel("Units Sold")
plt.grid(axis='y')
plt.tight_layout()
plt.show()

# ---------------------------
# 2. Pie chart - Market share
labels = ['Company A', 'Company B', 'Company C']
sizes = [45, 30, 25]
colors = ['#66b3ff', '#99ff99', '#ff9999']

plt.figure(figsize=(5, 5))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.title("Market Share")
plt.axis('equal')  # Equal aspect ratio ensures pie is a circle
plt.tight_layout()
plt.show()
