# Imports

import pandas as pd
import numpy as np


data = {
    'Product' : ['Book', 'Pen', 'Notebook', 'Pencil'],
    'Price': [18.50, 5.00, 11.20, 3.99],
    'Stock': [7, 100, 30, 200]
}

df = pd.DataFrame(data)

print(df.head(2))
print(df.tail(3))

# reading the statistical summary
print(df.describe())

# reading the structure of the data
print(df.info())