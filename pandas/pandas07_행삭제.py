import numpy as np
import pandas as pd
df = pd.DataFrame({'이름':["홍길동","이순신","유관순","강감찬"],
                   '국어':[10,45,22,45],
                   '수학':[60,25,43,76],
                   '영어': [10, 45, 22, 45],
                   '과학': [60, 25, 43, 76]},
                  index=np.arange(1,5))
print(df)
'''
    이름  국어  수학  영어  과학
1  홍길동  10  60  10  60
2  이순신  45  25  45  25
3  유관순  22  43  22  43
4  강감찬  45  76  45  76
'''
# 1. 다중 행 삭제:, df.drop(index=[idx,idx2]), 삭제된 새로운 DataFrame 반환
drop_df = df.drop(index=[1,2])
print(drop_df)

# 2. 다중 행 삭제:, df.drop([idx,idx2], axis=0), 삭제된 새로운 DataFrame 반환
drop_df = df.drop([1,3], axis=0)
print(drop_df)