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
# 1. df.assign(컬럼명=리스트)
df = df.assign(영어=[45,35,57,78])
print(df)
'''
    이름  국어  수학  영어
1  홍길동  10  60  45
2  이순신  45  25  35
3  유관순  22  43  57
4  강감찬  45  76  78
'''
# 2. df.assign(컬럼명:lambda함수)
df = df.assign(총합=lambda df: df["국어"]+df["수학"]+df["영어"])
print(df)
'''
    이름  국어  수학  영어   총합
1  홍길동  10  60  45  115
2  이순신  45  25  35  105
3  유관순  22  43  57  122
4  강감찬  45  76  78  199
'''
#######################################################################
# 3. df["컬럼명"] = 값
df["평균"] = np.round(df["총합"]/3, 2)
print(df)

# 4.df["컬럼명"] = 조건식(True/False)
# df["합격여부"] = df["평균"] >= 40
# 실습 : "합격여부"컬럼에 True면 "합격",False면 "불합격" 출력 되도록 구현하시오(list comprehension)
df["합격여부"] = ["합격" if avg > 40 else "불합격" for avg in df["평균"]]
print(df)

# 5. df.insert(컬럼인덱스, 컬럼명, 값)
df.insert(1,"이메일",["hong","lee","ryu","kang"])
print(df)