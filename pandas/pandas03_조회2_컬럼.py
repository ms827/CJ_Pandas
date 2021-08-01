import numpy as np
import pandas as pd

'''
   DataFrame 컬럼 및 행 조회
  
  1. DataFrame 구성요소
     - 인덱스
     - 컬럼
     - 데이터
  
  2. 조회
    가. 컬럼만 조회
        - [] 이용
          예> df['컬럼명']  ==> Series로 반환
              df[['컬럼명','컬럼명']] ==> DataFrame 반환
             
        - .  이용
          에> df.컬럼명 ==> Series로 반환
  
    나. loc 표현식 ==>  loc[]
        - 행과 컬럼 모두 조회
        - 조회하는 값은 행label 또는 컬럼label 사용한다.
    
    다. iloc 표현식  ==>  iloc[]
        - 행과 컬럼 모두 조회
        -  조회하는 값은 행 위치값 또는 컬럼 위치값 사용한다.
'''

df = pd.DataFrame({'col1':[5,3,2],
                   'col2':[10,45,22],
                   'col3':[6,2,43]})
print(df)
print("1. col1 컬럼 조회[]:\n",  df["col1"]) # Series 로 반환
print("2. col1 컬럼 조회.dot:\n",  df.col1 ) # Series 로 반환

print("3. 여러 컬럼 조회[]:\n",  df[["col1","col3"]]) # DataFrame 로 반환