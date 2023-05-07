# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 10:21:14 2022

@author: a
"""
#題目:針對任一地區(Region)，分析其獲利最高、銷售數量及金額最高的商品(子類別)。
import pandas as pd
import numpy as np
import warnings
warnings.simplefilter("ignore")
pd.set_option('display.max_columns',None)
df=pd.read_csv('[FN] Saledata.csv',encoding='latin1')

#需要的欄位
df2=df[['Region','Sub-Category','Sales','Quantity','Profit']]
#挑選出東區資料
df2=df2[df2['Region']=='East'].reset_index(drop=True)


Tops=df2.groupby('Sub-Category').sum()
Top_Profit=Tops['Profit'].sort_values(ascending=False)
print("獲利最高商品子類別:%s  金額:%s" %(Top_Profit[0:1].index[0],Top_Profit[0]))
Top_Qty=Tops['Quantity'].sort_values(ascending=False)
print("銷售數量最高商品子類別:%s  金額:%s" %(Top_Qty[0:1].index[0],Top_Qty[0]))
Top_Sales=Tops['Sales'].sort_values(ascending=False)
print("銷售金額最高商品子類別:%s  金額:%s" %(Top_Sales[0:1].index[0],Top_Sales[0]))
