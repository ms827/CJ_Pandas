import numpy as np
import pandas as pd
import seaborn as sns

#  컬럼별 문자열 함수 적용 방법
import numpy as np

'''
   merge ==> pd.merge(df1, df2, 옵션)
   1. sql의 조인 비슷
   2. inner 및 outer merge 제공
   3. 기본적인 연결은 2가지로 연결
      가. 컬럼 대 컬럼
      나. 컬럼 대 인덱스
      다. 인덱스 대 인덱스
'''
# 2. 비공통컬럼 병합
df1 = pd.DataFrame({"x1":["A","B","C"],
                    "x2":[1,2,3]})
df2 = pd.DataFrame({"y1":["A","B","C"],
                    "y2":[10,20,30],
                    "y3":[100,200,300]})

print(df1)
'''
  x1  x2
0  A   1
1  B   2
2  C   3
'''
print(df2)
'''
  y1  y2   y3
0  A  10  100
1  B  20  200
2  C  30  300
'''
m_df = pd.merge(df1, df2, left_on="x1" , right_on="y1" , how="inner")
m_df = pd.merge(df1, df2, left_on="x1" , right_on="y1" , how="inner").drop(columns=["y1"])
m_df = pd.merge(df1, df2, left_on="x1" , right_on="y1" , how="inner")\
         .drop(columns=["y1"]).rename(columns={"x1":"x1/y1"})
print("1. 비 공통컬럼 병합, inner 병합 \n", m_df)
########################################################################
df1 = pd.DataFrame({"x1":["A","B","C"],
                    "x2":[1,2,3]})
df2 = pd.DataFrame({"y1":["A","B","D"],
                    "y2":[10,20,30],
                    "y3":[100,200,300]})

m_df = pd.merge(df1, df2, left_on="x1" , right_on="y1" , how="left" )
m_df = pd.merge(df1, df2, left_on="x1" , right_on="y1" , how="right" )
m_df = pd.merge(df1, df2, left_on="x1" , right_on="y1" , how="outer" )
m_df = pd.merge(df1, df2, left_on="x1" , right_on="y1" , how="outer" , indicator=True )
m_df = pd.merge(df1, df2, left_on="x1" , right_on="y1" , how="outer" , indicator=True ) \
         .query("x1 in ['C','B']")
print("2. 비 공통컬럼 병합, outer 병합 \n", m_df)
