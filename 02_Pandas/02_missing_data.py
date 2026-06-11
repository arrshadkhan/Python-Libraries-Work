import numpy as np
import pandas as pd

data = {
    'A': [1, 2, np.nan, 4, 5],
    'B': [1, 2, 3, 4, 5],
    'C': [1, 2, 3, np.nan, np.nan],
    'D': [1, np.nan, np.nan, np.nan, 5]
}
df=pd.DataFrame(data)
print(df)

#null value see
# print(df)
# print(df.isna())
# print(df.isna().sum())
# print(df.notna())

# remove null value
# print(df.dropna())
# print(df.dropna(thresh=2))

#add data 
# print(df.fillna(0))  # add zero in nan place
#add specific data
values={ 'A':100 , 'B':200 ,'C':300,'D':400}
print(df.fillna(value=values))