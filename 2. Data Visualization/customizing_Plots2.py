# Customizing Plots

# imports
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# data
x = [1, 2, 3, 4, 5, 7]
y = [2, 3, 5, 7, 11, 13]

# visualising the data -> adding some styling
plt.plot(x, y, color='darkorange', linewidth=2, linestyle='--', marker='o', markersize=8)
plt.title('Styled line plot of prime number trend')
plt.xlabel('index')
plt.ylabel('prime number')
plt.grid(True)
plt.show()
