import pandas as pd
from pandas import Series,DataFrame
#导入数据
carquality = DataFrame(pd.read_csv('car_complain.csv'))
#数据预处理
carqualitytemp = carquality.problem.str.get_dummies(',')
carqualitytemp2 = carquality.drop(['problem'],axis = 1)
newcarquality = carqualitytemp2.join(carqualitytemp)
#print(newcarquality)
#品牌投诉总数(DataFrame使用sort_values函数)
df_brand = newcarquality.groupby(['brand'])['id'].agg(['count'])
df_brand = df_brand.sort_values(by ='count',ascending = False)
print(df_brand)
#车型投诉总数
df_carmodel = newcarquality.groupby(['car_model'])['id'].agg(['count']).sort_values(by ='count',ascending = False) 
print(df_carmodel)
#哪个品牌平均车型投诉量最大
df_mix = newcarquality.groupby(['brand','car_model'])['id'].agg(['count'])
df_mix = df_mix.groupby(['brand'])['count'].agg(['mean']).sort_values(by = 'mean',ascending = False)
print(df_mix)