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

# 1. 단일 컬럼 삭제: df.pop(), inplace=True로 동작, 기존 DataFrame에서 삭제됨.
df.pop("과학")
print(df)

# 2. 다중 컬럼 삭제:, df.drop(columns=[col1, col2]), 삭제된 새로운 DataFrame 반환
# df = df.drop(columns=["수학","영어"])
# print(df)

# 3. 다중 컬럼 삭제:, df.drop([값, 값], axis=1), 삭제된 새로운 DataFrame 반환
df = df.drop(["수학","영어"], axis=1)
print(df)