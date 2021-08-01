import numpy as np
import pandas as pd
import seaborn as sns


df = pd.DataFrame({'col1':[5,3,2,np.nan, 5],
                   'col2':[10,40,2,np.nan, 3],
                   'col3':[6,2,40,1,2]},
                  index=list("ABCDE"))
print(df)
'''
   col1  col2  col3
A   5.0  10.0     6
B   3.0  40.0     2
C   2.0   2.0    40
D   NaN   NaN     1
E   5.0   3.0     2
'''
print("1. df의 행의 갯수:\n", len(df)) # 5
print("2. 컬럼별 최대값:\n", df.max(axis=0)) #  행을 축으로 삼고 최대값을 구한다.
print("3. 컬럼별 최대값의 index값:\n", df.idxmax(axis=0)) #  행을 축으로 삼고 최대값을 구한다.
print("4. 행별 최대값:\n", df.max(axis=1)) #  컬럼을 축으로 삼고 최대값을 구한다.
print()
print("5. 컬럼별 최소값:\n", df.min(axis=0)) #  행을 축으로 삼고 최소값을 구한다.
print("6. 컬럼별 최소값의 index값:\n", df.idxmin(axis=0)) #  행을 축으로 삼고 최소값을 구한다.
print("7. 행별 최소값:\n", df.min(axis=1)) #  컬럼을 축으로 삼고 최소값을 구한다.
print()
print("8. 컬럼별 합계:\n", df.sum(axis=0))
print("9. 행별 합계:\n", df.sum(axis=1))
print()
print("10. 컬럼별 평균:\n", df.mean(axis=0))
print("11. 행별 평균:\n", df.mean(axis=1))
print()
print("12. 컬럼별 중앙값:\n", df.median(axis=0))
print("13. 행별 중앙값:\n", df.median(axis=1))
print()
print("14. 컬럼별 사분위값:\n", df.quantile([0.25,0.75],axis=0))
print("14. 행별 사분위값:\n", df.quantile([0.25,0.75], axis=1))
print()
print("15. 컬럼별 분산:\n", df.var(axis=0))
print("15. 행별 분산:\n", df.var(axis=1))
print()
print("16. 컬럼별 표준편차:\n", df.std(axis=0))
print("16. 행별 표준편차:\n", df.std(axis=1))
print()
print("17. 컬럼별 null 제외한 개수:\n", df.count(axis=0))
print("17. 행별 null 제외한 개수:\n", df.count(axis=1))
print()
print("18. 컬럼별 누적합(cumsum):\n", df.cumsum(axis=0))
print("18. 행별 누적합(cumsum):\n", df.cumsum(axis=1))
print()
print("19. 컬럼별 누적곱(cumprod):\n", df.cumprod(axis=0))
print("19. 행별 누적곱(cumprod):\n", df.cumprod(axis=1))
print()
print("20. 컬럼별 누적최대값(cummax):\n", df.cummax(axis=0))
print("20. 행별 누적최대값(cummax):\n", df.cummax(axis=1))
print()
print("21. 컬럼별 누적최소값(cummin):\n", df.cummin(axis=0))
print("21. 행별 누적최소값(cummin):\n", df.cummin(axis=1))
print()
print("22. 통계 데이터 통합적으로", df.describe())
print(df.info())  # SQL의 desc 테이블명과 동일한 기능