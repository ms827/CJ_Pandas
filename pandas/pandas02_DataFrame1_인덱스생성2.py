import numpy as np
import pandas as pd

'''
   DataFrame 인덱스 생성
   1. 기본 인덱스
      ==> 자동으로 0,1,2,....

   2. 명시적 인덱스
      df.index=[1,2,3]

   3. 기존 컬럼을 인덱스로 변경 ( 기존 인덱스에 덮어씀)
     df.set_index(컬럼명) ==> 복사본 반환
     df.set_index(컬럼명, inplace=True) ==> 자신이 변경

   4. 기존 인덱스를 컬럼으로 변경하고 새로운 인덱스 생성 
     df.reset_index()  ==> 복사본 반환
     df.reset_index(inplace=True)  ==> 자신이 변경

   5. 기존 인덱스를 삭제하고 새로운 인덱스 생성   
     df.reset_index(drop=True)  ==> 복사본 반환
     df.reset_index(drop=True, inplace=True)  ==> 자신이 변경


   6. 기존 인덱스의 재배치 ==> 기존에 없던 인덱스를 추가로 지정하면 NaN 설정된다.
    예> B     A
        A => B
        C    C
     df.reindex()  

   7.  ignore_index=True => df병합시 index 중복된다. 따라서 index는 무시하고 병합하자.
'''

# 7. 기존 인덱스의 재배치
df1 = pd.DataFrame({'col1': [5, 3, 2]})
print(df1)
'''
   col1
0     5
1     3
2     2
'''
df2 = pd.DataFrame({'col1': [50, 30, 20]})
print(df2)
new_df = pd.concat([df1, df2], ignore_index=True)
print(new_df)
print("##############################################")