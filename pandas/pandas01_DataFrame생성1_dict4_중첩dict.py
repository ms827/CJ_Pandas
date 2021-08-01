import numpy as np
import pandas as pd

# 2. 중첩 dict : 바깥의 key가 컬럼이 되고 중첩dict의 key는 인덱스로 처리된다
df = pd.DataFrame({'col1': {2000:300, 2001:150},
                   'col2':{2000:400, 2001:100},
                   'col3':{2000:500, 2001:80}})
print(df)
'''
      col1  col2  col3
2000   300   400   500
2001   150   100    80
'''
print(df.T)  #전치
'''
      2000  2001
col1   300   150
col2   400   100
col3   500    80
'''