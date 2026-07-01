import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# url="https://raw.githubusercontent.com/TheiScale/YouTube-Video-Notes/main/Website%20Data%20Analysis%20Project/data-export%20(1).csv" #data set from github


df = pd.read_csv('data-export.csv')
df.columns=df.iloc[0]
df=df.drop(index=0).reset_index(drop=True)
df.columns=['Channel Group','DateHour','Users','Sessions','Engaged sessions','Avg Engagement Time Session','Avg Engagement per user','Events per session','Engagement Rate','Event count']
df['DateHour']=pd.to_datetime(df['DateHour'],format='%Y%m%d%H',errors='coerce')
numeric_col=df.columns.drop(['Channel Group','DateHour'])
df[numeric_col]=df[numeric_col].apply(pd.to_numeric,errors='coerce')
df['Hour']=df['DateHour'].dt.hour
# print(df.head())


# sns.set(style="whitegrid")
# plt.figure(figsize=(10,5))
# df.groupby('DateHour')[['Sessions','Users']].sum().plot(ax=plt.gca())
# plt.title('Session and User Over Time')
# plt.xlabel('DateHour')
# plt.ylabel('Count')

# plt.figure(figsize=(8,5))
# sns.barplot(data=df,x='Channel Group',y='Users',estimator=np.sum,palette='viridis')
# plt.title('Total user by channel')
# plt.xticks(rotation=45)

# plt.figure(figsize=(8,5))
# sns.barplot(data=df,x='Channel Group',y='Avg Engagement per user',estimator=np.mean,palette='magma')
# plt.title('Average engagement time by channel')
# plt.xticks(rotation=45)

# plt.figure(figsize=(8,5))
# sns.barplot(data=df,x='Channel Group',y='Engagement rate',palette='coolwarm')
# plt.title('Engagement Rate Distrubution by channel')
# plt.xticks(rotation=45)

# session_df=df.groupby('Channel Group')[['Sessions','Engaged sessions']].sum().reset_index()
# session_df['Non Engaged']=session_df['Sessions']-session_df['Engaged sessions']
# session_df_melted=session_df.melt(id_vars='Channel Group',value_vars=['Engaged sessions','Non Engaged'])
# plt.figure(figsize=(8,5))
# sns.barplot(data=session_df_melted,x='Channel Group',y='value',hue='variable')
# plt.title('Engaged vs Non Engaged')
# plt.xticks(rotation=45)

# heatmap_data=df.groupby(['Hour','Channel Group'])['Sessions'].sum().unstack().fillna(0)
# plt.figure(figsize=(12,8))
# sns.heatmap(heatmap_data,cmap='YlGnBu',linewidths=.5,annot=True,fmt='.0f')
# plt.title('Traffic by Channel and Hour')
# plt.xlabel('Channel by Group')
# plt.ylabel("Hour of the day")


df_plot=df.groupby('DateHour')[['Engagement Rate','Sessions']].mean().reset_index()
plt.figure(figsize=(10,5))
plt.plot(df_plot['DateHour'],df_plot['Engagement Rate'],label='Engagement Rate',color='green')
plt.plot(df_plot['DateHour'],df_plot['Sessions'],label='Sessions',color='blue')
plt.title('Engagement Rate vs Sessions Over Time')
plt.xlabel('DateHour')
plt.legend()
plt.grid(True)
plt.show()
