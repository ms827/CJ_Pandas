import numpy as np
import pandas as pd
import seaborn as sns


df = pd.DataFrame({'col1':[5,3,2,np.nan, 5],
                   'col2':[10,40,2,np.nan, 3],
                   'col3':[6,2,40,1,2]},
                  index=list("ABCDE"))
print(df)
'''
   col1  col2  col3
A   5.0  10.0     6
B   3.0  40.0     2
C   2.0   2.0    40
D   NaN   NaN     1
E   5.0   3.0     2
'''
# 단일 컬럼
print("1. 특정 컬럼의 최대값:\n", df["col1"].max())  # 5.0
print("1. 특정 컬럼의 최대값의 index:\n", df["col1"].idxmax())  # A
print("1. 특정 컬럼의 최소값:\n", df["col1"].min())  # 2.0
print("1. 특정 컬럼의 최소값의 index:\n", df["col1"].idxmin())  # C
print("1. 특정 컬럼의 합계:\n", df["col1"].sum())  # 15.0
print("1. 특정 컬럼의 평균:\n", df["col1"].mean())  # 3.75
print("1. 특정 컬럼의 중앙값:\n", df["col1"].median())  # 4.0
print("1. 특정 컬럼의 개수:\n", df["col1"].count())  # 4

# 다중 컬럼
print("2. 다중 컬럼의 최대값:\n", df[["col1","col2"]].max())
print()
# 행선택
'''
   col1  col2  col3
A   5.0  10.0     6
B   3.0  40.0     2
C   2.0   2.0    40
D   NaN   NaN     1
E   5.0   3.0     2
'''
print("3. 특정 행의 최대값:" , df.loc["A"].max())
print("3. 특정 행의 최소값:" , df.loc["A"].min())
print("3. 특정 행의 합계:" , df.loc["A"].sum())
print("3. 특정 행의 평균:" , df.loc["A"].mean())
print("3. 특정 행의 갯수:" , df.loc["A"].count())
print("3. 특정 행의 중앙값:" , df.loc["A"].median())
print("3. 특정 행의 누적합:" , df.loc["A"].cumsum())
print("3. 특정 행의 누적곱:" , df.loc["A"].cumprod())
