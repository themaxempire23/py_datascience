# Customizing Plots

# imports
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# data
x = [1, 2, 3, 4, 5, 7]
y = [2, 3, 5, 7, 11, 13]

# visualising the data
plt.plot(x, y)
plt.title('prime number trend')
plt.xlabel('position')
plt.ylabel('prime number')
plt.grid(True)
plt.show()
