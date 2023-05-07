# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 16:08:19 2022

@author: user
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df = pd.read_csv('[FN] Saledata.csv',encoding = ('latin1') )
pd.set_option('display.max_rows', None)
df['Order Date']=pd.to_datetime(df['Order Date'])
df.info()
print(df.describe())
print(df.isnull().sum())



plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
plt.rcParams['axes.unicode_minus'] = False


# 2014每月銷售總額趨勢
df2014 = df[df['Order Date'] <= '2014-12-31']
monthly_revenue_df2014 = df2014.set_index('Order Date').resample('M')['Sales'].sum()
monthly_revenue_df2014 = pd.DataFrame(monthly_revenue_df2014)
monthly_revenue_df2014['Sales'].plot()
plt.title('2014銷售趨勢圖')    
plt.show()
# 2015每月銷售總額趨勢
df2015 = df[(df['Order Date'] >= '2015-01-01') & (df['Order Date'] <= '2015-12-31')]
monthly_revenue_df2015 = df2015.set_index('Order Date').resample('M')['Sales'].sum()
monthly_revenue_df2015 = pd.DataFrame(monthly_revenue_df2015)
monthly_revenue_df2015['Sales'].plot()
plt.title('2015銷售趨勢圖')
plt.show()
# 2016每月銷售總額趨勢
df2016 = df[(df['Order Date'] >= '2016-01-01') & (df['Order Date'] <= '2016-12-31')]
monthly_revenue_df2016 = df2016.set_index('Order Date').resample('M')['Sales'].sum()
monthly_revenue_df2016 = pd.DataFrame(monthly_revenue_df2016)
monthly_revenue_df2016['Sales'].plot()
plt.title('2016銷售趨勢圖')
plt.show()
# 2017每月銷售總額趨勢
df2017 = df[df['Order Date'] >= '2017-01-01']
monthly_revenue_df2017 = df2017.set_index('Order Date').resample('M')['Sales'].sum()
monthly_revenue_df2017 = pd.DataFrame(monthly_revenue_df2017)
monthly_revenue_df2017['Sales'].plot()
plt.title('2017銷售趨勢圖')
plt.show()
# 2014 產品每月銷量數量前五名
date_item_df = df2014.groupby([
        pd.Grouper(key = 'Order Date',freq = 'M'), 'Product ID'
    ])['Quantity'].sum().reset_index()
date_item_df = pd.DataFrame(date_item_df)
date_item_df = date_item_df.sort_values("Quantity",ascending=False).head()
print(date_item_df)
date_item_df = date_item_df[['Product ID','Quantity']].set_index('Product ID')
date_item_df.plot(kind = 'bar') 
plt.title('2014每月銷售前五名商品')
plt.show()
# 2015 產品每月銷量數量前五名
date_item_df = df2015.groupby([
        pd.Grouper(key = 'Order Date',freq = 'M'), 'Product ID'
    ])['Quantity'].sum().reset_index()
date_item_df = pd.DataFrame(date_item_df)
date_item_df = date_item_df.sort_values("Quantity",ascending=False).head()
date_item_df = date_item_df[['Product ID','Quantity']].set_index('Product ID')
date_item_df.plot(kind = 'bar')
plt.title('2015每月銷售前五名商品')
plt.show()
# 2016 產品每月銷量數量前五名
df2016 = df[(df['Order Date'] >= '2016-01-01') & (df['Order Date'] <= '2016-12-31')]
date_item_df = df2016.groupby([
        pd.Grouper(key = 'Order Date',freq = 'M'), 'Product ID'
    ])['Quantity'].sum().reset_index()
date_item_df = pd.DataFrame(date_item_df)
date_item_df = date_item_df.sort_values("Quantity",ascending=False).head()
date_item_df = date_item_df[['Product ID','Quantity']].set_index('Product ID')
date_item_df.plot(kind = 'bar')
plt.title('2016每月銷售前五名商品')
plt.show()
# 2017 每個產品每月銷量數量前五名
date_item_df = df2017.groupby([
        pd.Grouper(key = 'Order Date',freq = 'M'), 'Product ID'
    ])['Quantity'].sum().reset_index()
date_item_df = pd.DataFrame(date_item_df)
date_item_df = date_item_df.sort_values("Quantity",ascending=False).head()
date_item_df = date_item_df[['Product ID','Quantity']].set_index('Product ID')
date_item_df.plot(kind = 'bar')
plt.title('2017每月銷售前五名商品')
plt.show()
# 各地區每年利潤分析
profit_df = df.groupby(['Region',pd.Grouper(key = 'Order Date', freq=('Y'))])['Profit'].sum().unstack()
profit_df.plot(kind = 'bar')  
plt.legend(['2014','2015','2016','2017'])
plt.show()
# 2014回頭客
# 回頭客
monthly_repeat_customers_df2014 = df2014.groupby([
    'Customer ID',pd.Grouper(key='Order Date',freq='M') 
]).filter(lambda x: len(x) > 1)  #filter>1意思為，用兩個維度做分群後，筆數>1，即同一個月同一顧客有1筆以上消費
monthly_repeat_customers_df2014 = monthly_repeat_customers_df2014.set_index('Order Date').resample('M')['Customer ID'].nunique()    
# 所有顧客
monthly_all_customers_df2014 = df2014.set_index('Order Date').resample('M')['Customer ID'].nunique()
# 回頭客比率
monthly_repeat_percent2014 = monthly_repeat_customers_df2014/monthly_all_customers_df2014*100
pd.DataFrame(monthly_repeat_percent2014.values).plot(    
    kind='bar',
    legend = False)
plt.title('2014每月回頭客比率')
plt.ylabel('%')
plt.xticks(
    range(len(monthly_repeat_customers_df2014.index)), 
    [x.strftime('%Y,%m') for x in monthly_repeat_customers_df2014.index], 
    rotation=45)
for x,y in enumerate(monthly_repeat_percent2014):
    plt.text(x,y,'%s' %round(y),ha='center',fontsize=10)
plt.show()
# 2015頭客
# 回頭客
monthly_repeat_customers_df2015 = df2015.groupby([
    'Customer ID',pd.Grouper(key='Order Date',freq='M') 
]).filter(lambda x: len(x) > 1) 
 #filter>1意思為，用兩個維度做分群後，筆數>1，即同一個月同一顧客有1筆以上消費
monthly_repeat_customers_df2015 = monthly_repeat_customers_df2015.set_index('Order Date').resample('M')['Customer ID'].nunique()    
# 所有顧客
monthly_all_customers_df2015 = df2015.set_index('Order Date').resample('M')['Customer ID'].nunique()
# 回頭客比率
monthly_repeat_percent2015 = monthly_repeat_customers_df2015/monthly_all_customers_df2015*100
pd.DataFrame(monthly_repeat_percent2015.values).plot(    
    kind='bar',
    legend = False)
plt.title('2015每月回頭客比率')
plt.ylabel('%')
plt.xticks(
    range(len(monthly_repeat_customers_df2015.index)), 
    [x.strftime('%Y,%m') for x in monthly_repeat_customers_df2015.index], 
    rotation=45)
for x,y in enumerate(monthly_repeat_percent2015):
    plt.text(x,y,'%s' %round(y),ha='center',fontsize=10)
plt.show()
# 2016頭客
# 回頭客
monthly_repeat_customers_df2016 = df2016.groupby([
    'Customer ID',pd.Grouper(key='Order Date',freq='M') 
]).filter(lambda x: len(x) > 1)  #filter>1意思為，用兩個維度做分群後，筆數>1，即同一個月同一顧客有1筆以上消費
monthly_repeat_customers_df2016 = monthly_repeat_customers_df2016.set_index('Order Date').resample('M')['Customer ID'].nunique()    
# 所有顧客
monthly_all_customers_df2016 = df2016.set_index('Order Date').resample('M')['Customer ID'].nunique()
# 回頭客比率
monthly_repeat_percent2016 = monthly_repeat_customers_df2016/monthly_all_customers_df2016*100
pd.DataFrame(monthly_repeat_percent2016.values).plot(    
    kind='bar',
    legend = False)
plt.title('2016每月回頭客比率')
plt.ylabel('%')
plt.xticks(
    range(len(monthly_repeat_customers_df2016.index)), 
    [x.strftime('%Y,%m') for x in monthly_repeat_customers_df2016.index], 
    rotation=45)
for x,y in enumerate(monthly_repeat_percent2016):
    plt.text(x,y,'%s' %round(y),ha='center',fontsize=10)
plt.show()
# 2017頭客
# 回頭客
monthly_repeat_customers_df2017 = df2017.groupby([
    'Customer ID',pd.Grouper(key='Order Date',freq='M') 
]).filter(lambda x: len(x) > 1) 
print(monthly_repeat_customers_df2017)
 #filter>1意思為，用兩個維度做分群後，筆數>1，即同一個月同一顧客有1筆以上消費
monthly_repeat_customers_df2017 = monthly_repeat_customers_df2017.set_index('Order Date').resample('M')['Customer ID'].nunique()    
# 所有顧客
monthly_all_customers_df2017 = df2017.set_index('Order Date').resample('M')['Customer ID'].nunique()
# 回頭客比率
monthly_repeat_percent2017 = monthly_repeat_customers_df2017/monthly_all_customers_df2017*100
pd.DataFrame(monthly_repeat_percent2017.values).plot(    
    kind='bar',
    legend = False)
plt.title('2017每月回頭客比率')
plt.ylabel('%')
plt.xticks(
    range(len(monthly_repeat_customers_df2017.index)), 
    [x.strftime('%Y,%m') for x in monthly_repeat_customers_df2017.index], 
    rotation=45)
for x,y in enumerate(monthly_repeat_percent2017):
    plt.text(x,y,'%s' %round(y),ha='center',fontsize=10)
plt.show()
# rfm
import datetime as dt
theday=dt.datetime.strptime("2017-12-31","%Y-%m-%d")
summary_df = df.groupby('Customer ID').agg({
    'Order Date': lambda x: (theday-x.max()),
    'Ship Date': lambda x: x.nunique(),
    'Sales': lambda x: x.sum(),
})
summary_df.columns = ['recency','freqnency','monetary']
summary_df["recency"]=summary_df["recency"].astype(str)
summary_df["recency"]=summary_df["recency"].str.replace("days.*","")
print(summary_df)
# 產品協同導向
# 最可能連同最熱銷商品一起購買的五樣產品
customer_item_matrix = df.pivot_table(
    index='Customer ID', 
    columns='Product ID', 
    values='Quantity',
    aggfunc='sum'
)
customer_item_matrix = customer_item_matrix.applymap(lambda x: 1 if x > 0 else 0)
from sklearn.metrics.pairwise import cosine_similarity
item_item_sim_matrix = pd.DataFrame(cosine_similarity(customer_item_matrix.T))
item_item_sim_matrix.columns = customer_item_matrix.T.index
item_item_sim_matrix['Product ID'] = customer_item_matrix.T.index
item_item_sim_matrix = item_item_sim_matrix.set_index('Product ID')
top_5_similar_item2014 =list(item_item_sim_matrix.loc['TEC-AC-10002076'].sort_values(ascending=False).iloc[:5].index) #Stockcode, 型態為index
top_5_similar_item2015 =list(item_item_sim_matrix.loc['OFF-BI-10004040'].sort_values(ascending=False).iloc[:5].index) #Stockcode, 型態為index
top_5_similar_item2016 =list(item_item_sim_matrix.loc['OFF-BI-10003981'].sort_values(ascending=False).iloc[:5].index) #Stockcode, 型態為index
top_5_similar_item2017 =list(item_item_sim_matrix.loc['TEC-AC-10001772'].sort_values(ascending=False).iloc[:5].index) #Stockcode, 型態為index
print('最可能連同2014最熱銷商品一起購買的五樣產品')
print(top_5_similar_item2014)
print('最可能連同2015最熱銷商品一起購買的五樣產品')
print(top_5_similar_item2015)
print('最可能連同2016最熱銷商品一起購買的五樣產品')
print(top_5_similar_item2016)
print('最可能連同2017最熱銷商品一起購買的五樣產品')
print(top_5_similar_item2017)