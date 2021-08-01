import numpy as np
import pandas as pd
import seaborn as sns



df = sns.load_dataset("mpg")
print(df.head())
'''
    mpg  cylinders  displacement  ...  model_year  origin                       name
0  18.0          8         307.0  ...          70     usa  chevrolet chevelle malibu
1  15.0          8         350.0  ...          70     usa          buick skylark 320
2  18.0          8         318.0  ...          70     usa         plymouth satellite
3  16.0          8         304.0  ...          70     usa              amc rebel sst
4  17.0          8         302.0  ...          70     usa                ford torino
'''
# applly함수 용도 : 사용자가 작성한 함수(built_in포함)를 한번에 DataFrame의 행과 열에 적용 가능한 함수

#  df.apply(함수, [옵션])

print("1. 첫번째 행 반환:", df.iloc[0])
print("2. 첫번째 행 반환(apply함수적용):")

def kkk(n):
    print(">>> \n", n)
    return n[0]

# copy_df = df.apply(kkk , axis=0) # kkk 함수가 df의 컬럼별로 적용된다.(*****)
copy_df = df.apply(lambda n:n[0], axis=0) # kkk 함수가 df의 컬럼별로 적용된다.(*****)
print(copy_df)
print()
print("3. 첫번째 행 ~ 3번째 행까지 반환(apply함수적용):")
copy_df = df.apply(lambda n:n[:3]) # kkk 함수가 df의 컬럼별로 적용된다.(*****)
print(copy_df)
#####################################################
df = pd.DataFrame({
                   '국어':[10,20,30,40],
                   '수학':[1,2,3,4]},
                  index=np.arange(1,5))
print(df)
'''
   국어  수학
1  10   1
2  20   2
3  30   3
4  40   4
'''
print("4. 컬럼별 총합:", df.apply(sum, axis=0))
print("4.  행별 총합:", df.apply(sum, axis=1))
df["총합"]= df.apply(sum, axis=1)
df["평균"]= df.apply(np.mean, axis=1)
print(df)
copy_df = df.append(df.apply(sum, axis=0), ignore_index=True)
copy_df.index = [1,2,3,4,"합"]
print(copy_df)
##################################################################
# series 적용
print("5. 특정컬럼에서 apply 적용", copy_df["총합"] > 30 )
print("5. 특정컬럼에서 apply 적용", copy_df["총합"].apply(lambda n: n >30) )
print("5. 특정컬럼에서 apply 적용", copy_df[copy_df["총합"].apply(lambda n: n >30)])
