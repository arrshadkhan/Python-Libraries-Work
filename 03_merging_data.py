import numpy as np
import pandas as pd

#Merging
employees = pd.DataFrame({
    'employee_id': [1, 2, 3, 4, 5],
    'name': ['John', 'Anna', 'Peter', 'Linda', 'Bob'],
    'department': ['HR', 'IT', 'Finance', 'IT', 'HR']
})

# DataFrame 2: Salary information
salaries = pd.DataFrame({
    'employee_id': [1, 2, 3, 6, 7],
    'salary': [60000, 80000, 65000, 70000, 90000],
    'bonus': [5000, 10000, 7000, 8000, 12000]
})
# print(employees)
# print('\n')
# print(salaries)

merge1=pd.merge(employees,salaries,on='employee_id',how='inner')
print(merge1)
# merge2=pd.merge(employees,salaries,on='employee_id',how='outer')
# print(merge2)
# merge3=pd.merge(employees,salaries,on='employee_id',how='left')
# print(merge3)
# merge4=pd.merge(employees,salaries,on='employee_id',how='right')
# print(merge4)

#concatanation
# df1 = pd.DataFrame({
#     'A': ['A0', 'A1', 'A2'],
#     'B': ['B0', 'B1', 'B2'],
#     'C': ['C0', 'C1', 'C2']
# })

# df2 = pd.DataFrame({
#     'A': ['A3', 'A4', 'A5'],
#     'B': ['B3', 'B4', 'B5'],
#     'C': ['C3', 'C4', 'C5']
# })
# print(pd.concat([df1,df2]))#comman column
# print(pd.concat([df1,df2],axis=1))#comman Row
# print(pd.concat([df1,df2],axis=0))#comman coloumn

#join
# df1 = pd.DataFrame({
#     'name': ['Alice', 'Bob', 'Charlie']
# }, index=[1, 2, 3])

# # Second DataFrame
# df2 = pd.DataFrame({
#     'score': [85, 90, 75]
# }, index=[2, 3, 4])

# print(f'{df1}\n{df2}')
# print(df1.join(df2,how='outer'))
# print(df2.join(df1))
# print(df2.join(df1,how='outer'))