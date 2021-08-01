import numpy as np
import pandas as pd

df = pd.DataFrame({'col1':[5,3,2,4],
                   'col2':[10,45,22,5],
                   'col3':[6,2,43,6]},
                  index=list("ABCD"))
print(df)
'''
   col1  col2  col3
A     5    10     6
B     3    45     2
C     2    22    43
D     4     5     6
'''
print("###########################")
# 1. loc[라벨] 로 조회후 값 변경
print( df.loc['A','col2'] ) # 10, 스칼라
df.loc['A','col2'] = 100
print(df)
print("###########################")
print( df.loc[["B","D"],["col1","col2"]])
df.loc[["B","D"],["col1","col2"]] = -1
print(df)

# 2. iloc[위치] 로 조회후 값 변경
print( df.iloc[[1,3],[0,1]])
df.iloc[[1,3],[0,1]]= 1000  # 순방향
print(df)
df.iloc[[1,3],[-1,-2]]= 2000  # 역방향
print(df)