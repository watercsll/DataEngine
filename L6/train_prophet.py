#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
#数据加载
train = pd.read_csv('./train.csv')
print(train.head())
#转化pd日期格式
train['Datetime'] = pd.to_datetime(train.Datetime,format='%d-%m-%Y %H:%M')
#更新索引
train.index = train.Datetime
print(train.head())
#去掉不需要的ID和datetime
train.drop(['ID','Datetime'],axis = 1,inplace = True)
print(train.head())
#按照天采样
daily_train = train.resample('D').sum()
daily_train['ds'] = daily_train.index
daily_train['y'] = daily_train.Count
daily_train = daily_train.drop(['Count'],axis = 1)
print(daily_train.head())
#使用fbprophet拟合
from fbprophet import Prophet
m = Propeht(yearly_seasonality = True, seasonality_prior_scale = 0.1)
m.fit(daily_train)
#预测未来七个月，213天
future = m.make_future_dateframe(periods = 213)
forecast = m.predict(future)
print(forecast)
#绘图
m.plot(forecast)
#查看各个成分
m.plot_components(forecast)
