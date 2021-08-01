import numpy as np
import pandas as pd


# np.nan ==> null의미
df = pd.DataFrame({"k1":["one"]*3 + ["two"]*4,
                   "k2":[1,1,2,3,3,4,4]})
print(df)
'''
    k1  k2
0  one   1
1  one   1
2  one   2
3  two   3
4  two   3
5  two   4
6  two   4
'''

# 1.중복행 조회: df.dupliated()
print("1. DataFrame에서 행단위로 중복행 조회\n")
print(df.duplicated())  # Seires
print(df.duplicated(keep="first"))  # Series, default, 처음에 발견된 데이터를 기준으로 중복체크
print(df.duplicated(keep="last"))  # Series, 마지막에 발견된 데이터를 기준으로 중복체크

print()

# 2.특정컬럼 중복행 조회 : df.duplicated(컬럼), df.duplicated([컬럼,컬럼])
print("2. 특정 컬럼 중복행 조회\n")
print(df.duplicated("k1"))

#########################################
# 3. 중복행제거 : df.drop_duplicaes(), 중복 제거후 df 반환
drop_df = df.drop_duplicates(ignore_index=True)
print(drop_df)