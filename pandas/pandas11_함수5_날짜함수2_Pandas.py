import numpy as np
import pandas as pd
import seaborn as sns

# pandas 날짜 함수 지정

# 1. 특정 날짜(str) ----------------> datetime 변경 : pd.to_datetime('날짜')
print("1. str-->날짜타입:")
target_date = pd.to_datetime("2002/01/01")
target_date = pd.to_datetime("2002 02 02")
target_date = pd.to_datetime("2002-03-03")
# target_date = pd.to_datetime("2002,03,03") 안됨
print(target_date, type(target_date))
# 1. 년도-월-일
target_date = pd.to_datetime("2002,04,04", format="%Y,%m,%d")
print(target_date, type(target_date))
target_date = pd.to_datetime("2002:04:04", format="%Y:%m:%d")
print(target_date, type(target_date))
target_date = pd.to_datetime("2002년04월04일", format="%Y년%m월%d일")
print(target_date, type(target_date))

target_date = pd.to_datetime("20020505", format="%Y%m%d")
print(target_date, type(target_date))

df = pd.DataFrame({'year' : [2015,2016],
                   'month' : [2,3],
                   'day' : [4,5]})
copy_df = pd.to_datetime(df)
print(copy_df)

# 2. 년도-월-일 시:분:초
target_date = pd.to_datetime("2002년05월05일 12시12분13초", format="%Y년%m월%d일 %H시%M분%S초")
print(target_date,type(target_date))  # 2002-05-05 12:12:13 <class 'pandas._libs.tslibs.timestamps.Timestamp'>