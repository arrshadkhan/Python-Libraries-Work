import numpy as np
import pandas as pd

data = {
    "Category": ["A", "B", "A", "B", "A", "B", "A", "B"],
    "Store": ["S1", "S1", "S2", "S2", "S1", "S2", "S2", "S1"],
    "Sales": [100, 200, 150, 250, 120, 180, 200, 300],
    "Quantity": [10, 15, 12, 18, 8, 20, 15, 25],
    "Date": pd.date_range("2023-01-01", periods=8),
}
df = pd.DataFrame(data)


# cat=df.groupby('Category')
# for i , c in cat:
#     print(i)
#     print(c)

# total=df.groupby('Category')['Sales'].sum()
# print(total)
# total=df.groupby('Store')['Sales'].sum()
# print(total)
# total=df.groupby(['Category','Store'])['Sales'].sum()
# print(total)

# Aggregation
# Aggrefation is nothing but a funtion that give more information about data such as '''mean mode median std min max count'''
print(df["Sales"].max())
#   "min max count std mean mode median count or etc."
print(
    df["Sales"].agg(["mean", "std", "count", "max", "min"])
)  # Multiple aggregation performed but here no mode() work
