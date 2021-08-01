import numpy as np
import pandas as pd
import seaborn as sns

#  컬럼별 문자열 함수 적용 방법
import numpy as np

'''
   csv 파일
   1. 읽기
       pd.read_csv("파일경로", 옵션)
       
   2. 쓰기
       pd.to_csv("파일경로")
'''
# 1. 기본
df = pd.read_csv("./data/msft.csv")
print("1.  기본: \n", df.head())

# 2. 특정 컬럼을 index로 변경
df = pd.read_csv("./data/msft.csv", index_col=0)
print("2. 특정 컬럼을 index로 변경: \n", df.head())

# 3. 특정 컬럼만 반환
df = pd.read_csv("./data/msft.csv", usecols=["Date","High"])
print("3. 특정 컬럼만 반환: \n", df.head())

# 4. 행 갯수 지정
df = pd.read_csv("./data/msft.csv", nrows=2)
print("4. 행 갯수 지정: \n", df)

# 5. 끝행 n개 제외
df = pd.read_csv("./data/msft.csv", skipfooter=2)
print("5. 끝행 n개 제외: \n", df.tail(5))

################################################
# 6. null 처리 : 기본은 NaN 로 표현, 공백으로 지정할려면  na_filter=False
df = pd.read_csv("./data/company3.csv", na_filter=False)
print("6. null 처리: \n", df)
################################################
# 7. 구분자가 , 아닌 파일
df = pd.read_csv("./data/msft_piped.txt", sep="|", encoding="utf-8")
print("7. 구분자가 , 아닌 파일: \n", df)
###############################################################################
# 8.  csv로 저장
df2 = pd.DataFrame({"empno":["A1","A2","A3","A4","A5"],
                    "sal":[1000,5000,2400,3200,4500],
                    "hiredate":pd.date_range("2021/02/04", periods=5),
                    "deptno":[10,20,30,20,10]})
df2.to_csv("./data/inky4832.csv")

# 9. csv로 저장 -  컬럼 선택 ==> 컬럼 인덱스  지원 안됨.
df2.to_csv("./data/inky4832_2.csv",  columns=["empno","sal"], index=False)