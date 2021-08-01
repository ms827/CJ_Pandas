import numpy as np
import pandas as pd
import seaborn as sns

#  컬럼별 문자열 함수 적용 방법
import numpy as np

'''
   merge ==> pd.merge(df1,df2, 옵션)
   1. SQL의 조인 비슷
   2. inner 및 outer merge 제공
   3. 기본적인 연결은 3가지로 연경
      가. 컬럼 대 컬럼 (  공통컬럼:on속성, 비공통컬럼: left_on, right_on )
      나. 컬럼 대 인덱스
      다. 인덱스 대 인덱스
   4. 병합된 결과에서 query(select)해서 필터링 가능
'''
# 1. 공통컬럼 병합
df1 = pd.DataFrame({"x1":["A","B","C"],
                    "y1":[1,2,3]})
df2 = pd.DataFrame({"x1":["A","B","C"],
                    "y1":[10,20,30]})
m_df = pd.merge(df1, df2, on="x1" , how="inner", suffixes=["_left","_right"])
print("1. 공통컬럼 병합, inner 병합 \n", m_df)