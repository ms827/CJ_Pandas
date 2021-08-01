import numpy as np
import pandas as pd
import seaborn as sns

#  컬럼별 문자열 함수 적용 방법
import numpy as np

'''
   pd.pivot() :     행 --> 열 (세로 --> 가로)
'''
df = pd.DataFrame({"date":[2000,2000,2000,2001,2001,2001,2002,2002,2002],
                     "item":["A","B","C","A","B","C","A","B","C"],
                     "value":[1,2,3,4,5,6,7,8,9]})
print(df)
'''
 date item  value
0  2000    A      1
1  2000    B      2
2  2000    C      3
3  2001    A      4
4  2001    B      5
5  2001    C      6
6  2002    A      7
7  2002    B      8
8  2002    C      9
'''
copy_df = df.pivot(index="date", columns="item", values="value")
print(copy_df)
'''
item  A  B  C
date         
2000  1  2  3
2001  4  5  6
2002  7  8  9
'''
copy_df = df.pivot(index="item", columns="date", values="value")
print(copy_df)
'''
date  2000  2001  2002
item                  
A        1     4     7
B        2     5     8
C        3     6     9
'''