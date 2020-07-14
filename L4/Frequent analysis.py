import pandas as pd
import numpy as np
from pandas import Series,DataFrame
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

# Header = None
dataset = pd.read_csv('./Market_Basket_Optimisation.csv', header = None)
# 将交易放到集合中去
transaction = pd.DataFrame(columns = ('id','commodities'))
# 循环取数据
for i in range(0,dataset.shape[0]):
    temp = []
    for j in range(0,20):
        if str(dataset.values[i,j]) != 'nan':
            temp.append(str(dataset.values[i,j]))
    temp = ",".join(temp)
    transaction = transaction.append(pd.DataFrame({'id':[i],'commodities':[temp]}),ignore_index = True)   
# 将数据归一化
temp = transaction.commodities.str.get_dummies(',')
transaction = transaction.drop('commodities',1).join(temp)
# 用id列做index
transaction.set_index(['id'],inplace=True)
#print(transaction)
#计算频繁项集，排序
frequent_itemsets = apriori(transaction,min_support = 0.05,use_colnames = True)
frequent_itemsets = frequent_itemsets.sort_values(by = 'support',ascending = False)
#计算提升度，排序
rules = association_rules(frequent_itemsets, metric = 'lift', min_threshold = 0.5)
rules = rules.sort_values(by = 'lift',ascending = False)
#打印结果
print('频繁项集：',frequent_itemsets)
print('提升度：',rules)




