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

df1 = pd.DataFrame({"key":['a','b','a','a','b','c'],
                    "value":range(6)},
                    index=["A","B","C","D","E","F"])
print(df1)
'''
  key  value
0   a      0
1   b      1
2   a      2
3   a      3
4   b      4
5   c      5
'''
df2 = pd.DataFrame({"group_value":[4,23,5]},index=["A","B","Z"])
print(df2)
'''
   group_value
a            4
b           23
c            5
'''
m_df = pd.merge(df1,df2,left_index=True,right_index=True, how="inner")
print(m_df)
m_df = pd.merge(df1,df2,left_index=True,right_index=True, how="outer")
print(m_df)