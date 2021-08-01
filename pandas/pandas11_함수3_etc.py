import numpy as np
import pandas as pd
import seaborn as sns



df = pd.DataFrame({'col1':[5,3,2,np.nan, 5],
                   'col2':[10,40,2,4, 3],
                   'col3':[6,2,40,0,2]},
                  index=list("ABCDE"))
print(df)
'''
   col1  col2  col3
A   5.0  10.0     6
B   3.0  40.0     2
C   2.0   2.0    40
D   NaN   4     0
E   5.0   3.0     2
'''
# 1. unique한 값 반환 :  df[컬럼].unique()
print("1. col1 컬럼의 unique 값 반환:", df["col1"].unique())

# 2. null제외한 unique한 값 갯수 반환:  df[컬럼].nunique()
print("2. null제외한 col1 컬럼의 unique 값 갯수 반환:", df["col1"].nunique()) # 3

# 3. null 포함한 unique한 값 갯수 반환:  df[컬럼].nunique()
print("3. null 포함한  col1 컬럼의 unique 값 갯수 반환:", df["col1"].nunique(dropna=False)) # 4

# 4.  null제외한 값의 빈도수 반환:  df[컬럼].value_counts()
print("4. null제외한 col1 컬럼의 빈도수 반환:", df["col1"].value_counts()) #

# 5.  null 포함한 값의 빈도수 반환:  df[컬럼].value_counts()
print("4. null 포함한 col1 컬럼의 빈도수 반환:", df["col1"].value_counts(dropna=False)) #
print()
# 6. 컬럼 및 인덱스 변경
'''
   col1  col2  col3
A   5.0  10.0     6
B   3.0  40.0     2
C   2.0   2.0    40
D   NaN   4     1
E   5.0   3.0     2
'''
print("5.  컬럼명 변경")
copy_df = df.rename(columns={"col1":"c1","col2":"c2","col3":"c3"})
print(copy_df)

print("6.  index명 변경")
copy_df = df.rename(index={"A":"a","B":"b","C":"c","D":"d","E":"e"})
print(copy_df)

##################################################
print("7. 지정된 범위 포함여부 boolean 반환 ==> boolean 색인")  # sql문의 between a and b
print(df["col3"].between(4,10))

print("8. 지정된 값 포함여부 boolean 반환 ==> boolean 색인")  # sql문의 in (값1, 값2, ...)
print(df["col3"].isin([6,40]))


##########################################
# any(): 하나라도 참이냐?, all(): 모두 참이냐?
'''
   col1  col2  col3
A   5.0  10.0     6
B   3.0  40.0     2
C   2.0   2.0    40
D   NaN   4     0
E   5.0   3.0     2
'''
print("9. null 제외한특정 컬럼값이 모두 참이냐?", df["col1"].all())   # 시험문제
# skipna=False 이면 포함시키는데 True로 치환되어 포함된다
print("9. null 포함한특정 컬럼값이 모두 참이냐?(null은 True로 치환됨)", df["col3"].all(skipna=False))
print("9. 특정 컬럼값이 모두 참이냐?", df["col3"].all())  # False
print("9. 특정 컬럼값이 하나라도 참이냐?", df["col3"].any())  # True
print()
print("10. null 제외한 모든 컬럼값이 모두 참이냐?", df.all())  # False
print("10. null 제외한 컬럼값이 하나라도 참이냐?", df.any())  # False

# 응용
'''
   col1  col2  col3
A   5.0  10.0     6
B   3.0  40.0     2
C   2.0   2.0    40
D   NaN   4     0
E   5.0   3.0     2
'''
print("응용1: col1이 하나라도 짝수가 있는가?", (df["col1"]%2==0).any())  # True

print("응용2: col1,col2 모두 짝수인가?", (df[["col1","col2"]]%2==0).all())
print("응용2: col1,col2 모두 짝수인가?", (df[["col1","col2"]]%2==0).all().all())  # False