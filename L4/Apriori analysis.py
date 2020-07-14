import pandas as pd
import numpy as np
from efficient_apriori import apriori

# Header = None
dataset = pd.read_csv('./Market_Basket_Optimisation.csv', header = None)
# 将交易放到集合中去
transaction = []
for i in range(0,dataset.shape[0]):
    temp = []
    for j in range(0,20):
        if str(dataset.values[i,j]) != 'nan':
            temp.append(str(dataset.values[i,j]))
    transaction.append(temp)

itemsets,rules = apriori(transaction,min_support = 0.05, min_confidence = 0.1)
print('频繁项集：',itemsets)
print('关联规则：',rules)




