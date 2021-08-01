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
# 1. 공통컬럼 병합
df1 = pd.DataFrame({"x1":["A","B","C"],
                    "y1":[1,2,3]})
df2 = pd.DataFrame({"x1":["A","B","C"],
                    "x2":[10,20,30],
                    "x3":[100,200,300]})

print(df1)
'''
  x1  y1
0  A   1
1  B   2
2  C   3
'''
print(df2)
'''
  x1  x2
0  A  10
1  B  20
2  C  30
'''
m_df = pd.merge(df1, df2, on="x1" , how="inner")
print("1. 공통컬럼 병합, inner 병합 \n", m_df)

m_df = pd.merge(df1, df2[["x1","x3"]], on="x1" , how="inner")
print("2. 공통컬럼 병합, inner 병합, 특정컬럼만 참여 \n", m_df)

#############################################################
df1 = pd.DataFrame({"x1":["A","B","C"],
                    "y1":[1,2,3]})
df2 = pd.DataFrame({"x1":["A","B","D"],
                    "x2":[10,20,30],
                    "x3":[100,200,300]})
m_df = pd.merge(df1, df2, on="x1" , how="left")  #left outer 병합
print("3. 공통컬럼 병합, left outer 병합 \n", m_df)

m_df = pd.merge(df1, df2, on="x1" , how="right")  #right outer 병합
print("3. 공통컬럼 병합, right outer 병합 \n", m_df)

m_df = pd.merge(df1, df2, on="x1" , how="outer")  #full outer 병합
print("3. 공통컬럼 병합, outer outer 병합 \n", m_df)
##############################################################
m_df = pd.merge(df1, df2, on="x1" , how="outer", indicator=True)  # indicator=True시 _merge컬럼추가
print("3. 공통컬럼 병합, outer outer 병합 \n", m_df)
###########################################################################
m_df = pd.merge(df1, df2, on="x1" , how="outer").query("x1 in ['A','B']")
print(m_df)