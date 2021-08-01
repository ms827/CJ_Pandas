import numpy as np
import pandas as pd

# 1.dict 이용한 DataFrame 생성 (모든 열의 길이가 동일해야 한다)
df = pd.DataFrame(data={'col1':[5,3,2],
                   'col2':[10,45,22],
                   'col3':[6,2,43]})
print(df)
'''
   col1  col2  col3
0     5    10     6
1     3    45     2
2     2    22    43
'''
print(type(df))