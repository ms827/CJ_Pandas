import numpy as np
import pandas as pd


import seaborn as sns
df = sns.load_dataset("mpg")
print(df.head())

# 1. 컬럼값으로 정렬:  df.sort_values(by=컬럼명), 기본은 오름차순, 복사본 반환
copy_df = df.sort_values(by="mpg")
print(copy_df.head(10)) # DataFrame 반환

# 2. 컬럼값으로 정렬:  df.sort_values(by=컬럼명), 내림차순
copy_df = df.sort_values(by="mpg", ascending=False)
print(copy_df.head(10)) # DataFrame 반환

######################################################
# 3. 다중 정렬:  df.sort_values(by=[컬럼명1,컬럼명2]), 내림차순
copy_df = df.sort_values(by=["mpg","displacement"], ascending=False)
print(copy_df[["mpg","displacement"]].head(20)) #

##############################################
list_value = ["a","DDD","EEEE","aa"]
list_value.sort(key=len)
print(list_value)
##############################################
# 4. 특정함수 정렬:  df.sort_values(by=[컬럼명1,컬럼명2], key=함수명)
# print("name 컬럼의 문자열 길이로 정렬")
# def kkk(x):
#     print(">>>", x, type(x))
#     return x.
# copy_df = df.sort_values(by="name", key= kkk)
# print(copy_df.info())