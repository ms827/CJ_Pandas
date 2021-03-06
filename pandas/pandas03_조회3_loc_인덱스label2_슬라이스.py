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
print("1. B인덱스 라벨 ~ 끝 \n", df.loc["B":])
print("2. B인덱스 라벨 ~ C라벨 \n", df.loc["B":"C"])

print("3. B인덱스 라벨 ~ 끝, col2 컬럼 \n", df.loc["B":"col2"])
print("4. 인덱스 처음라벨 ~ C까지, col2,col1 컬럼 \n", df.loc[:"C",["col2","col1"]])

############################################################
# 2. 컬럼 라벨 슬라이싱
print("5. B인덱스 라벨, col2 ~ 끝 \n", df.loc["B", "col2":])

print("6. B인덱스 라벨, 처음 ~ 끝 \n", df.loc[["A","B"], :"col2"])

############################################################
# 3. 인덱스, 컬럼 라벨 슬라이싱
print("7. 인덱스 처음라벨 ~ C까지, 처음~col2 \n", df.loc[:"C", :"col2"])
