import numpy as np
import pandas as pd

# 1.dict 이용한 DataFrame 생성 (모든 열의 길이가 동일해야 한다)
df = pd.DataFrame(data={'col1':[5,3,2],
                   'col2':[10,45,22],
                   'col3':[6,2,43]},
                  index=["A","B","C"])
df.columns = ['c1','c2','c3']
print(df)
'''
   c1  c2  c3
A   5  10   6
B   3  45   2
C   2  22  43
'''