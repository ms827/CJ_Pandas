import numpy as np
import pandas as pd


df = pd.DataFrame({'col1':[5,3,2,4],
                   'col2':[10,45,22,5],
                   'col3':[6,2,43,6]},
                  index=list("ABCD"))
print(df)
print("1. A 인덱스 라벨 조회: \n", df.loc["A"])  # series
print("2. A, C 인덱스 라벨 조회: \n", df.loc[["A","C"]])  # DataFrame

print("3. A인덱스, col2 컬럼 라벨 조회: \n", df.loc["A","col2"])  # 10,스칼라
print("4. A인덱스, col2,col3 컬럼 라벨 조회: \n", df.loc["A",["col2","col3"]])  # 10, series

print("5. A,C인덱스, col2 컬럼 라벨 조회: \n", df.loc[["A","C"],"col2"])  # series

print("6. A,C인덱스, col2,col3 컬럼 라벨 조회: \n", df.loc[["A","C"],["col2","col3"]])  # DataFrame