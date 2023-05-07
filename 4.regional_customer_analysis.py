# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 22:30:05 2022

@author: 葉冠麟
"""
import scipy.stats as stats
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from statsmodels.stats.multicomp import pairwise_tukeyhsd

df = pd.read_csv('[FN] Saledata.csv',encoding = ('latin1') )

transfer = LabelEncoder()
df['Category'] = transfer.fit_transform(df['Category'])

S = [int(df['Category'][i])
    for i in range(len(df)) if df['Region'][i] == "South"]
W = [int(df['Category'][i])
    for i in range(len(df)) if df['Region'][i] == "West"]
C = [int(df['Category'][i])
    for i in range(len(df)) if df['Region'][i] == "Central"]
E = [int(df['Category'][i])
    for i in range(len(df)) if df['Region'][i] == "East"]

lev = stats.levene(S,W,C,E)

print(lev)

if lev[1] > 0.05:
    print('差異性結果:')
    ano1 = stats.f_oneway(S,W,C,E)
    print(ano1)
    if ano1[1] <= 0.05:
        allsun = df['Region']
        allheight = ['Category']
        tukey = pairwise_tukeyhsd(endog=allheight ,groups=allsun ,alpha=0.05)
        print(tukey.summmary())
else:
    k = stats.kruskal(S,W,C,E)
    print('差異性結果:',k)
    
transfer = LabelEncoder()
df['Sub-Category'] = transfer.fit_transform(df['Sub-Category'])

S1 = [int(df['Sub-Category'][i])
    for i in range(len(df)) if df['Region'][i] == "South"]
W1 = [int(df['Sub-Category'][i])
    for i in range(len(df)) if df['Region'][i] == "West"]
C1 = [int(df['Sub-Category'][i])
    for i in range(len(df)) if df['Region'][i] == "Central"]
E1 = [int(df['Sub-Category'][i])
    for i in range(len(df)) if df['Region'][i] == "East"]

lev = stats.levene(S1,W1,C1,E1)

print(lev)

if lev[1] > 0.05:
    print('差異性結果:')
    ano1 = stats.f_oneway(S1,W1,C1,E1)
    print(ano1)
    if ano1[1] <= 0.05:
        print('post hoc comparision test')
        allsun = df['Region']
        allheight = ['Quantity']
        tukey = pairwise_tukeyhsd(endog=allheight ,groups=allsun ,alpha=0.05)
        print(tukey.summmary())
else:
    k = stats.kruskal(S1,W1,C1,E1)
    print('差異性結果:',k)   
