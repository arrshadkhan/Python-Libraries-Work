import numpy as np
import pandas as pd
df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': [10, 20, 30, 40, 50],
    'C': [100, 200, 300, 400, 500]
})
# print(df.shape)
# print(df.info())
# print(df.describe())
# add=df['B']+20
# print(add)
# def square(x):
#     return x*x
# print(df["B"].apply(square))

#or
# print(df["A"].apply(lambda x: x *x))