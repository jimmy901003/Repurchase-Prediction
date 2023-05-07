# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 23:51:23 2023

@author: user
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df = pd.read_csv('[FN] Saledata.csv',encoding = ('latin1') )
pd.set_option('display.max_rows', None)
df['Order Date']=pd.to_datetime(df['Order Date'])

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