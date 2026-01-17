# Customizing Plots

# imports
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# visualising the data
sns.set_theme(style='darkgrid')
tips = sns.load_dataset('tips')
sns.scatterplot(data=tips, x='total_bill', y='tip', hue='sex')
plt.title('tips by total bill and gender')
plt.show()
