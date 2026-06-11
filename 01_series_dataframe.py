import numpy as np
import pandas as pd

#       series
# my_list=[12,'hello','franklin',40]
# # print(pd.Series(my_list))
# arr=np.array([12,54,75,85,4,6,3,24])
# lebels=1,2,3,4,5,6,7,8
# # print(pd.Series(arr,index=lebels))
# name=['Name','Arshad','Faizan','Josh','Rahul','kratik']
# age='Age',23,30,32,53,18
# print(pd.Series(name,index=age))  # commented out to avoid duplicate output


#      data frame

data={
    "Name":['Arshad',"ramesh",'john','rahul','falak'],
    "Age":[23,55,32,53,64],
    'City':['indore','banglore','pune','delhi','kolkata'],
    "Salary":[12555,23475,65634,12434,63443]
}
df=pd.DataFrame(data)

# print(pd.DataFrame(data))

# my_list=[['Arshad',"ramesh",'john','rahul','falak'],
#          [23,55,32,53,64],
#          ['indore','banglore','pune','delhi','kolkata']]
# print(pd.DataFrame(my_list))
# label='name',"Age","city",'0','1'
# print(pd.DataFrame(my_list,columns=label))


# select coulum
# print(data['Name'])

# add coloum
# df["Position"]=["hr","head","boss","employee",'trainee']
# print(pd.DataFrame(data))

# removecolumn
# df.drop("Position",axis=1,inplace=True)

#select row
# print(df.loc[1])
# print(df.loc[[1,0]])

#select subset of row and column (use exact column names)
# print(df.loc[[0,1]][['Salary','Position']])
# print(df.loc[[3,4]][['Name','Age']])

# condition selection
# print(df[df["Age"]>30])
print(df[(df['Age']<30) & (df['Name']=='Arshad')])