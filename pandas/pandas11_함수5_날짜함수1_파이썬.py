
'''
   날짜와 시간 처리
   1.  import time
   2.  from datetime import datetime
'''

from datetime import datetime

print("1. 현재 날짜: ", datetime.now()) # 2021-07-20 11:27:54.468136
print("1. 현재 날짜: ", datetime.today()) # 2021-07-20 11:27:54.468136

print("2. 익숙한 날짜와 시간 구하기")
time_date = datetime.today()
print("1) 년도:", time_date.year)
print("2) 월:", time_date.month)
print("3) 일:", time_date.day)
print("4) 시:", time_date.hour)
print("5) 분:", time_date.minute)
print("6) 초:", time_date.second)

print("3. 특정 날짜 지정")
target_date = datetime(year=2002, month=7, day=20, hour=13, minute=12, second=43)
print(target_date, type(time_date)) # <class 'datetime.datetime'>

print("4. 날짜 --> 문자열")
str_target_date = target_date.strftime("%Y년%m월%d일")
print(str_target_date)

print("5. 문자열 --> 날짜")
# "2002-12-24" ---> 날짜객체
format_date = datetime.strptime("2002-12-24", '%Y-%m-%d')
print(format_date, type(format_date))# <class 'datetime.datetime'> #