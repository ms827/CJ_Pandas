import numpy as np
import pandas as pd
import seaborn as sns

#  컬럼별 문자열 함수 적용 방법
import numpy as np

'''
  json 파일
   1. 읽기
       pd.read_json("파일경로", 옵션)
       
   2. 쓰기
       df.to_json("파일경로")
       
  html 파일
  1. 읽기
     pd.read_html(url경로)   
     ==> <table>태그 읽는다. 
'''
# 1. 기본
df = pd.read_json("./data/my.json")
print("1.  기본: \n", df)

# 2. html
# pip install lxml
table = pd.read_html("https://www.seoul.go.kr/coronaV/coronaStatus.do")
print(len(table))
print(table[0].head())
print(table[1].head())
print(table[2].head())