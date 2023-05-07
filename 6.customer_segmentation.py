# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 22:43:29 2022

@author: a
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
from collections import Counter
warnings.filterwarnings("ignore")
#導入資料
pd.set_option('display.max_columns',None)
df=pd.read_csv('./[FN] Saledata.csv',encoding='latin1')
df['Order Date']=pd.to_datetime(df['Order Date'])

#抓取要的欄位並轉換型態
import datetime as dt
theday=dt.datetime.strptime("2017-12-31","%Y-%m-%d")
rfm_df = df.groupby('Customer ID').agg({
    'Order Date': lambda x: (theday-x.max()),
    'Ship Date': lambda x: x.nunique(),
    'Sales': lambda x: x.sum(),
})
rfm_df.columns = ['recency','frequency','monetary']
rfm_df["recency"]=rfm_df["recency"].astype(str)
rfm_df["recency"]=rfm_df["recency"].str.replace("days.*","")
rfm_df=rfm_df.reset_index()
rfm_df['recency']=rfm_df['recency'].astype(int)
#將3個特徵各分成五個區間 recency越大分數越小  frequency、monetary越大分數則越大
rfm_df['recency_score']=pd.qcut(rfm_df['recency'],5,labels=[5,4,3,2,1])
rfm_df['frequency_score']=pd.qcut(rfm_df['frequency'],5,labels=[1,2,3,4,5])
rfm_df["monetary_score"] = pd.qcut(rfm_df['monetary'], 5, labels=[1,2,3,4,5])


score=rfm_df[['recency_score','frequency_score',"monetary_score"]]
from sklearn.cluster import KMeans
wcss = []
# 計算 k=1~10 的損失函數
for i in range(1,11):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=0)
    kmeans.fit(score)
    wcss.append(kmeans.inertia_)

import matplotlib.pyplot as plt 
plt.plot(range(1,11), wcss, marker='o')
plt.title('Elbow graph')
plt.xlabel('Cluster number')
plt.ylabel('WCSS')
plt.show()

kmeans = KMeans(n_clusters=5, init='k-means++', random_state=0)
score['clusters'] = kmeans.fit_predict(score)
print(round(pd.DataFrame(kmeans.cluster_centers_,
                         columns=['Recency','Frequency','Monetary'],
                         index=[1,2,3,4,5]),2))
#畫圖
from mpl_toolkits.mplot3d import Axes3D 
colors=['purple', 'blue', 'green', 'gold','black']
fig = plt.figure()
fig.set_size_inches(13, 13)
ax = fig.add_subplot(111, projection='3d')
for i in range(kmeans.n_clusters):
    df_cluster=score[score['clusters']==i]
    ax.scatter(df_cluster['recency_score'],df_cluster['frequency_score'], df_cluster['monetary_score'],s=50,label='Cluster'+str(i+1), c=colors[i])
plt.legend()
ax.set_xlabel('Recency')
ax.set_ylabel('Monetary')
ax.set_zlabel('Frequency')
ax.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],kmeans.cluster_centers_[:,2],s=200,marker='^', c='red', alpha=0.7, label='Centroids')

