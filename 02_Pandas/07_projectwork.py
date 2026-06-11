import numpy as np
import pandas as pd
df=pd.read_csv('anime.csv')
# print(df.head())
# print(df.loc[1]['Title'])
def Extract_episodes(txt):
    check=False
    data=''
    for i in txt:
        if i == ')':
            check=False
            break
        if i=='(':
            check=True
            continue
        if check:
            data+=i
    return data

def Extract_timestamp(txt):
    check=False
    data=''
    for i in range(len(txt)):
        if txt[i]==')':
            for j in range(i+1,i+20):
                data+=txt[j]
            return data
        
from dateutil.relativedelta import relativedelta
from datetime import datetime

def calculate_total_months(period):
    try:
        start_str, end_str = period.split(' - ')
        start_date = datetime.strptime(start_str, '%b %Y')
        end_date = datetime.strptime(end_str, '%b %Y')
        r = relativedelta(end_date, start_date)
        return r.years * 12 + r.months + 1
    except: 
        return None
    
def remove_unnecessary_content(title):
    return title.split('(')[0].strip()

df['Episodes']=df['Title'].apply(Extract_episodes)
df['Episodes']=df['Episodes'].str.replace(' eps',"")
df['Episodes']=df['Episodes'].astype(int)
df['Time stamp']=df['Title'].apply(Extract_timestamp)
df['Months'] = df['Time stamp'].apply(calculate_total_months)
df['Title'] = df['Title'].apply(remove_unnecessary_content)
print(df.head())
# print(df[df['Score'] == df['Score'].max()]['Title'])
# print(df[df['Episodes'] == df['Episodes'].max()])