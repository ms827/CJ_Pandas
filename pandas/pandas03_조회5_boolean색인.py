import numpy as np
import pandas as pd

'''
   boolean 색인
  1.  loc 표현식

  2.  iloc 표현식
'''

df = pd.DataFrame([[1, 2, 43], [4, 5, 5], [7, 8, 6]],
                  index=['cobra', 'viper', 'sidewinder'],
                  columns=['max_speed', 'shield', "min_weight"])
print(df)
'''
            max_speed  shield  min_weight
cobra               1       2          43
viper               4       5           5
sidewinder          7       8           6
'''
print("1. 인덱스 라벨 boolean \n", df.loc[[False, False, True]])
print("1. 인덱스 라벨 boolean \n", df.loc[df['shield'] > 6])
# ########################################################
print("2. 인덱스 라벨 boolean, max_speed, min_weight컬럼 \n", df.loc[[False, False, True], ["max_speed", "min_weight"]])

# 논리 연산자 : &, | , ~
print("3. 인덱스 라벨 boolean \n", df.loc[(df['shield'] > 6) | (df['max_speed'] >= 4)])
print("3. 인덱스 라벨 boolean \n", df.loc[(df['shield'] > 6) | (df['max_speed'] >= 4), ["max_speed", "min_weight"]])
###################################
print("4. 컬럼 라벨 boolean \n", df.loc[["cobra", "viper"], [False, False, True]])
print("5. 컬럼 라벨 boolean \n", df.loc[["cobra", "viper"], df.loc['viper'] >= 1])
print("6. 컬럼 라벨 boolean \n", df.loc[df["max_speed"] > 4, df.loc['viper'] >= 1])
print()