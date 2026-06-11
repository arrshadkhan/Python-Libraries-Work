import numpy as np
import pandas as pd
data = {
    'Date': pd.date_range('2023-01-01', periods=20),
    'Product': ['A', 'B', 'C', 'D'] * 5,
    'Region': ['East', 'West', 'North', 'South', 'East', 'West', 'North', 'South', 'East', 'West',
               'North', 'South', 'East', 'West', 'North', 'South', 'East', 'West', 'North', 'South'],
    'Sales': np.random.randint(100, 1000, 20),
    'Units': np.random.randint(10, 100, 20),
    'Rep': ['John', 'Mary', 'Bob', 'Alice', 'John', 'Mary', 'Bob', 'Alice', 'John', 'Mary',
            'Bob', 'Alice', 'John', 'Mary', 'Bob', 'Alice', 'John', 'Mary', 'Bob', 'Alice']
}
df=pd.DataFrame(data)
# print(df)
# new_table=pd.pivot_table(df,values='Sales',index='Region',columns='Product',aggfunc='mean')
# print(new_table)
# new_table=pd.pivot_table(df,values=['Sales','Units'],index='Region',columns='Product',aggfunc='median')
# print(new_table)

#cross table
# table1=pd.crosstab(df['Region'],df['Product'])
# print(table1)
#output
# Product  A  B  C  D
# Region             
# East     5  0  0  0
# North    0  0  5  0
# South    0  0  0  5
# West     0  5  0  0