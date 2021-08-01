import numpy as np
import pandas as pd

df = pd.DataFrame({'이름':["홍길동","이순신","유관순","강감찬"],
                   '국어':[10,45,22,45],
                   '수학':[60,25,43,76]},
                  index=np.arange(1,5))
print(df)
'''
    이름  국어  수학
1  홍길동  10  60
2  이순신  45  25
3  유관순  22  43
4  강감찬  45  76

'''
# 주의할 점은 DataFrame의 인덱스와 반드시 일치해야 된다.
eng_series = pd.Series(data=[76,43,22,44], index=[1,2,3,4])
print(eng_series)
df["영어"] = eng_series
print(df)