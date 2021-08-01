import numpy as np
import pandas as pd

# np.nan ==> null의미
df = pd.DataFrame({'이름':["홍길동","이순신","유관순","강감찬"],
                   '국어':[10,45,np.nan,45],
                   '수학':[60,25,43,np.nan],
                   '영어': [10, 45, 22, 45],
                   '과학': [60, np.nan, 43, 76]},
                  index=np.arange(1,5))
print(df)
'''
    이름    국어    수학  영어    과학
1  홍길동  10.0  60.0  10  60.0
2  이순신  45.0  25.0  45   NaN
3  유관순   NaN  43.0  22  43.0
4  강감찬  45.0   NaN  45  76.0
'''
#  DataFrame에서 NaN, nan, null, None 찾기
# 1. pd.isna() ==> boolean 반환
print("1.df에 nan 조회:  \n", pd.isna(df))
print("1. '과학' 컬럼의 nan 조회:  \n", pd.isna(df["과학"])) # Series
print("1. '과학',국어 컬럼의 nan 조회:  \n", pd.isna(df[["과학","국어"]])) # DataFrame
print()

# 2. pd.isnull() ==> boolean 반환
print("2.df에 nan 조회:  \n", pd.isnull(df))
print("2. '과학' 컬럼의 nan 조회:  \n", pd.isnull(df["과학"])) # Series
print("2. '과학',국어 컬럼의 nan 조회:  \n", pd.isnull(df[["과학","국어"]])) # DataFrame
print()

#  null이 아닌것 조회
# 3. pd.notnull(), ~pd.isnull(), ~pd.inna()
print("3.df에 nan 이 아닌것 조회:  \n", pd.notnull(df))
print("3.df에 nan 이 아닌것 조회:  \n", ~pd.isnull(df))
print("3.df에 nan 이 아닌것 조회:  \n", ~pd.isna(df))
print("3. '과학' 컬럼의 nan이 아닌것 조회:  \n", ~pd.isnull(df["과학"]))