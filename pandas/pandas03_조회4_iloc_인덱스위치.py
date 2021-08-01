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
############################################################
# 1.인덱스 라벨 슬라잉싱
print("1. A인덱스 위치 조회 \n", df.iloc[0])  # series
print("2. A,C 인덱스 라벨 조회 \n", df.iloc[[0,2]])  # DataFrame

print("3. A 인덱스,col2 컬럼 위치 조회 \n", df.iloc[0,1])  # 10, scalar
print("4. A 인덱스,col2,col3 컬럼 위치 조회 \n", df.iloc[0,[1,2]])  # series

print("5. A, C 인덱스, col2 컬럼 위치 조회 \n", df.iloc[[0,2],1])
print("6. A, C 인덱스, col2,col3 컬럼 위치 조회 \n", df.iloc[[0,2],[1,2]])
