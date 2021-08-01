import numpy as np
import pandas as pd

# 5. Series 이용한 DataFrame 생성 ( 모든 열의 길이가 동일해야 한다)

# 가. 하나의 열을 갖는 Series 생성 및 DataFrame 변경
s = pd.Series(["홍길동","유관순"],name="이름")
print(s, type(s))  # <class 'pandas.core.series.Series'>
s_df = s.to_frame()
print(s_df, type(s_df))  # <class 'pandas.core.frame.DataFrame'>

# 나. 여러개의 Series 생성 및 DataFrame 생성
name_s = pd.Series(["홍길동","유관순"])
age_s = pd.Series([23,14])
address_s = pd.Series(["서울","부산"])

df = pd.DataFrame([name_s,age_s,address_s])
df.columns = ["학생1","학생2"]
df.index=["이름","나이","주소"]
print(df)
print(df.T)

