import numpy as np
import pandas as pd

# 4. 램덤 이용한 DataFrame 생성 ( 모든 열의 길이가 동일해야 한다)
arr = np.random.random((3,3))  # 다차원 배열
print(arr)

df = pd.DataFrame(arr,
                  index=list("ABC"),
                  columns=['col1','col2','col3'])
print(df)
'''
   col1  col2  col3
A     5     3     2
B    10    45    22
C     6     2    43
'''
