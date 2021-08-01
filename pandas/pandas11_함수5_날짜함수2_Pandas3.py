import numpy as np
import pandas as pd
import seaborn as sns

#  Pandas 날짜 함수 정리 ==> 날짜에서  특정 정보만 얻는 방법

date10 = pd.date_range(end="2021/07/27", periods=10, freq="D")
print(date10)
df = pd.DataFrame({"날짜":date10})
print(dir(df["날짜"].dt))
'''
'ceil', 'date', 'day', 'day_name',
 'day_of_week', 'day_of_year', 'dayofweek',
  'dayofyear', 'days_in_month', 'daysinmonth', 'floor', 'freq',
   'hour', 'is_leap_year', 'is_month_end', 'is_month_start', 
   'is_quarter_end', 'is_quarter_start', 'is_year_end', 'is_year_start',
    'isocalendar', 'microsecond', 'minute', 'month', 'month_name', 
    'nanosecond', 'normalize', 'quarter', 'round', 'second',
     'strftime', 'time', 'timetz', 'to_period', 'to_pydatetime',
      'tz', 'tz_convert', 'tz_localize', 'week', 'weekday', 'weekofyear', 'year']
'''
'''
    날짜
0 2021-07-18
1 2021-07-19
2 2021-07-20
'''
print("2.  년도 출력:", df["날짜"].dt.year)
print("3.  월도 출력:", df["날짜"].dt.month)
print("3.  월(영문)도 출력:", df["날짜"].dt.month_name())
print("3.  일도 출력:", df["날짜"].dt.day)
print("3.  주(week)도 출력:", df["날짜"].dt.isocalendar().week)

########################################################
# 날짜 ==> str 변경
print("4. 날짜=> str:",  df["날짜"].astype(str))