import numpy as np
import pandas as pd
'''
DataFrame 인덱스 생성
1. 기본 인덱스
  ==> 자동으로 0,1,2,...
2. 명시적 인덱스
  df.index=[1,2,3]
  
3. 기존 커럼을 인덱스로 변경 (기존 인덱스에 덮어씀)
  df.set_index(컬럼명) ==> 복사본 반환
  df.set_index(컬럼명, inplace=True) ==> 자신이 변경

4. 기존 인덱스를 컬럼변경하고 새로운 인덱스 생성
  df.reset_index() ==> 복사본 반환
  df.reset_index(inplace=True) ==> 자신이 변경
  
5. 기존 인덱스를 삭제하고 새로운 인덱스 생성
  df.reset_index(drop=True) ==> 복사본 반환
  df.reset_index(drop=True,inplace=True) ==> 자신이 변경
  

'''
#1. 기본인덱스
df = pd.DataFrame({'col1':[5,3,2],
                   'col2':[10,45,22],
                   'col3':[6,2,43]})
print("1. 기본인덱스 \n",df)
print("##########################################################")
#2. 명시적 인덱스
df = pd.DataFrame({'col1':[5,3,2],
                   'col2':[10,45,22],
                   'col3':[6,2,43]},
                  index=list("ABC"))
print("2. 명시적인덱스 \n",df)
print("##########################################################")
#3. 기존 컬럼을 인덱스로 변경
df = pd.DataFrame({'col1':[5,3,2],
                   'col2':[10,45,22],
                   'key':["AA","BB","CC"]})
# copy_df = df.set_index("key")
df.set_index("key", inplace=True)
print("3. 기존 컬럼을 인덱스로 변경 \n",df)
print("##########################################################")

# 4. 기존 인덱스를 컬럼으로 변경하고 새로운 인덱스 생성
# df.reset_index(inplace=True)
# print("4. 기존 인덱스를 컬럼으로 변경하고 새로운 인덱스 생성 \n", df)
# print("##########################################################")

# 5. 기존 인덱스를 삭제하고 새로운 인덱스 생성
df.reset_index(inplace=True, drop=True)
print("5. 기존 인덱스를 컬럼으로 변경하고 새로운 인덱스 생성 \n", df)
print("##########################################################")