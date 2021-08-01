import numpy as np
import pandas as pd


# np.nan ==> null의미
df = pd.DataFrame({'이름':["홍길동","이순신","유관순","강감찬", np.nan],
                   '국어':[10,45,np.nan,45, np.nan],
                   '수학':[60,25,43,np.nan ,np.nan],
                   '영어': [10, np.nan, 22, 45, np.nan],
                   '과학': [60, 34, 43, 76, np.nan],
                   '체육': [np.nan, np.nan, np.nan, np.nan, np.nan]},
                  index=np.arange(1,6))
print(df)
'''
    이름    국어    수학    영어    과학  체육
1  홍길동  10.0  60.0  10.0  60.0 NaN
2  이순신  45.0  25.0  45.0  34.0 NaN
3  유관순   NaN  43.0  22.0  43.0 NaN
4  강감찬  45.0   NaN  45.0  76.0 NaN
5  NaN   NaN   NaN   NaN   NaN NaN
'''
#  DataFrame에서 NaN, nan, null, None 찾아서 삭제
# 1. pd.dropna(axis=0|1) ==> boolean 반환
print("1. null이 하나라도 있는 행 모두 삭제: \n")
drop_df = df.dropna(axis=0) # df.dropna() 동일
print(drop_df)
print()
print("2. null이 하나라도 있는 열 모두 삭제: \n")
drop_df = df.dropna(axis=1)
print(drop_df)
##################################################
 # 3. pd.dropna( how="all", axis=0|1) ==> boolean 반환
print("3. null이  모두 있는 행 삭제: \n")
drop_df = df.dropna(axis=0, how="all") # df.dropna() 동일
print(drop_df)
print()
print("4. null이  모두 있는 열 삭제: \n")
drop_df = df.dropna(axis=1, how="all")
print(drop_df)
##################################################
# 4. df.fillna(변경값) :      null ==> 임의의 값으로 변경
print("4. 모든 null값을 N/A로 변경: \n")
fill_na = df.fillna("N/A")
print(fill_na)
print()
# 5. df.fillna({컬럼명:변경값, 컬럼명:변경값})
fill_na = df.fillna({"국어":0,"수학":-1})
print(fill_na)
######################################\
print(df)
'''
    이름    국어    수학    영어    과학  체육
1  홍길동  10.0  60.0  10.0  60.0 NaN
2  이순신  45.0  25.0   NaN  34.0 NaN
3  유관순   NaN  43.0  22.0  43.0 NaN
4  강감찬  45.0   NaN  45.0  76.0 NaN
5  NaN   NaN   NaN   NaN   NaN NaN
'''
fill_na = df.fillna(method="ffill") # null값  앞(front)에 있는 값으로 변경
print(fill_na)
fill_na = df.fillna(method="bfill") # null값  뒤(back)에 있는 값으로 변경
print(fill_na)