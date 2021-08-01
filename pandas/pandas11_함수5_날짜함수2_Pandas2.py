import numpy as np
import pandas as pd
import seaborn as sns

#  Pandas 날짜 함수 정리

# 지정된 범위의 날짜 생성 반환 :  pd.date_range( start날짜,  end날짜 )
copy_date = pd.date_range("2002/01/01", "2002/01/08")
print(copy_date)
copy_date = pd.date_range(start="2002/01/01", periods=5) #  freq="D"
print(copy_date)
copy_date = pd.date_range(start="2002/01/01", periods=5, freq="M") #  Month, 월의 마지막날 출력
print(copy_date)
copy_date = pd.date_range(start="2002/01/01", periods=5, freq="2M") #  2Month, 월의 마지막날 출력
print(copy_date)
copy_date = pd.date_range(start="2002/01/01", periods=5, freq="Y") #  Year,   년도의 마지막월 출력
print(copy_date)

# 활용 ==> 년 매출 출력 (  시계열 분석에서 응용 및 활용 )
date10 = pd.date_range(end="2021/07/27", periods=10, freq="Y")
print(date10)
df = pd.DataFrame({"매출":np.arange(1,11)},
                  index=date10)
print(df)