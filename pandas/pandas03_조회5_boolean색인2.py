import numpy as np
import pandas as pd

'''
   boolean 색인
  1.  loc 표현식

  2.  iloc 표현식
'''
mydict = [{'a': 1, 'b': 2, 'c': 3, 'd': 4},
          {'a': 100, 'b': 200, 'c': 300, 'd': 400},
          {'a': 1000, 'b': 2000, 'c': 3000, 'd': 4000}]
df = pd.DataFrame(mydict)
print(df)
'''
      0     1     2     3
      a     b     c     d
0 0     1     2     3     4
1 1   100   200   300   400
2 2  1000  2000  3000  4000
'''
print(df.iloc[[True, False, True]])
print(df.iloc[[True, False, True], [0, 1]])
print(df.iloc[:, [True, False, True, False]])

# print(df.iloc[True,[0,1]])
print()
# print(df.iloc[ df.iloc[0,0],[0,1]])
# print(df[df.iloc[1,0]==100])