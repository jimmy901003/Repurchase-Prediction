import pandas as pd 
from mlxtend.preprocessing import TransactionEncoder 
from mlxtend.frequent_patterns import apriori 
from mlxtend.frequent_patterns import association_rules 
from collections import defaultdict
import matplotlib.pyplot as plt
import numpy as np
pd.set_option('display.max_columns',None)
df = pd.read_csv('[FN] Saledata.csv',encoding = ('latin1') )

df.isnull().sum()

df2 = pd.DataFrame()
df2 ["product"] = df["Product Name"]
df2 ["customer"] = df["Customer ID"]


datalist = defaultdict(list)
customer = []
product = []

for cust,prod in zip (df2 ["customer"], df2["product"]):
    datalist[cust].append(prod)
for a,b in datalist.items():
    customer.append(a)
    product.append(b)
    
te = TransactionEncoder()
te_ary = te.fit(product).transform(product)

print(te_ary)
print(f"顧客 :{len(customer)}")
print(f"產品 :{len(te.columns_)}")

df_trans = pd.DataFrame(te_ary,columns = te.columns_)
print(df_trans)


frequency = apriori(df_trans,min_support=0.005,use_colnames=True)
frequency['item_length'] = frequency['itemsets'].apply(lambda x: len(x))
frequency = association_rules(frequency,metric="confidence",min_threshold=0.01)
result_rules = frequency[(frequency['lift']>1)]

print(result_rules)
