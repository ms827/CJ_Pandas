import numpy as np
import pandas as pd
df = pd.DataFrame({'이름':["홍길동","이순신","유관순","강감찬"],
                   '국어':[10,45,22,45],
                   '수학':[60,25,43,76],
                   '영어': [10, 45, 22, 45],
                   '과학': [60, 25, 43, 76]},
                  index=np.arange(1,5))
print(df)

# 1. 행추가1:   df.append(df2)
df2 = pd.DataFrame({'이름':["세종","태조"],
                   '국어':[10,45],
                   '수학':[60,25],
                   '영어': [10, 45],
                   '과학': [60, 25]},
                  index=np.arange(1,3))
print(df2)

append_df = df.append(df2, ignore_index=True)
print(append_df)
'''
0  홍길동  10  60  10  60
1  이순신  45  25  45  25
2  유관순  22  43  22  43
3  강감찬  45  76  45  76
4   세종  10  60  10  60
5   태조  45  25  45  25
'''
print(df)
print(df2)
# 2 . pd.concat([df,df2], axis=0)
concat_df = pd.concat([df, df2], axis=0, ignore_index=True)
print(concat_df)