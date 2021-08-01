import numpy as np
import pandas as pd
import seaborn as sns

#  컬럼별 문자열 함수 적용 방법
import numpy as np

'''
  그룹핑
  1. SQL의 group by 기능과 동일
  2. df.groupby(by="컬럼명").그룹함수
  
'''
df = pd.DataFrame({"deptno":[10,20,30,40],
                   "dname":["개발","인사","영업","관리"],
                   "loc":["서울","부산","제주","광주"]})

df2 = pd.DataFrame({"empno":["A1","A2","A3","A4","A5"],
                    "sal":[1000,5000,2400,3200,4500],
                    "hiredate":pd.date_range("2021/02/04", periods=5),
                    "deptno":[10,20,30,20,10]})
print(df)
print(df2)
'''
   deptno dname loc
0      10    개발  서울
1      20    인사  부산
2      30    영업  제주
3      40    관리  광주
  empno   sal   hiredate  deptno
0    A1  1000 2021-02-04      10
1    A2  5000 2021-02-05      20
2    A3  2400 2021-02-06      30
3    A4  3200 2021-02-07      20
4    A5  4500 2021-02-08      10

'''

# 1.부서별 sql 합계 및 평균?
sum_df = df2.groupby(by="deptno")["sal"].sum()
print("1.부서별 sal 합계 \n", sum_df)
mean_df = df2.groupby(by="deptno")["sal"].mean()
print("2.부서별 sal 평균 \n", mean_df)

max_df = df2.groupby(by="deptno")["sal"].max()
print("3.부서별 sal 최대값 \n", max_df)
min_df = df2.groupby(by="deptno")["sal"].min()
print("4.부서별 sal 최소값 \n", min_df)

size_df = df2.groupby(by="deptno")["sal"].size()
print("5.부서별 sal 개수 \n", size_df)