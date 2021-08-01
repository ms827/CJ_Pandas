import numpy as np
import pandas as pd

# 3. 중첩리스트 이용한 DataFrame 생성 ( 모든 열의 길이가 동일해야 한다)
df = pd.DataFrame([[5,3,2],[10,45,22],[6,2,43]],
                  index=list("ABC"),
                  columns=['col1','col2','col3'])
print(df)
'''
   col1  col2  col3
A     5     3     2
B    10    45    22
C     6     2    43
'''
p
