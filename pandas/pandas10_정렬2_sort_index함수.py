import numpy as np
import pandas as pd


import seaborn as sns

df = pd.DataFrame(np.arange(12).reshape(3,4),
                  index=["B","A","C"],
                  columns=['d','a','b','c'])
print(df)
'''
   d  a   b   c
B  0  1   2   3
A  4  5   6   7
C  8  9  10  11
'''

#  인덱스 정렬:  행정렬: df.sort_index( axis=0 )  열정렬:  df.sort_index( axis=1 )
# 1. 행단위 index정렬
copy_df = df.sort_index(axis=0)
print(copy_df)

copy_df = df.sort_index(axis=0, ascending=False) # 내림차순
print(copy_df)

# 2. 열단위 index정렬
copy_df = df.sort_index(axis=1)
print(copy_df)

copy_df = df.sort_index(axis=1, ascending=False) # 내림차순
print(copy_df)