import numpy as np
import pandas as pd
import seaborn as sns

#  컬럼별 문자열 함수 적용 방법
import numpy as np

'''
   series.str.문자열함수(arr) : 활용도가 매우 높다.
'''
import seaborn as sns

df = sns.load_dataset("mpg")
print(dir(df["name"].str))
'''
'capitalize', 'casefold', 'cat', 'center', 'contains', 'count',
'decode', 'encode', 'endswith', 'extract', 'extractall', 'find',
'findall', 'fullmatch', 'get', 'get_dummies', 'index', 'isalnum',
'isalpha', 'isdecimal', 'isdigit', 'islower', 'isnumeric', 'isspace',
'istitle', 'isupper', 'join', 'len', 'ljust', 'lower', 'lstrip',
'match', 'normalize', 'pad', 'partition', 'repeat', 'replace',
'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip',
'slice', 'slice_replace', 'split', 'startswith', 'strip',
'swapcase', 'title', 'translate', 'upper', 'wrap', 'zfill'
'''
print(df["name"].head(10))
'''
0    chevrolet chevelle malibu
1            buick skylark 320
2           plymouth satellite
3                amc rebel sst
4                  ford torino
'''
data = df["name"].head(10)
print(data)
'''
0    "chevrolet chevelle malibu"
1            buick skylark 320
2           plymouth satellite
3                amc rebel sst
4                  ford torino
5             ford galaxie 500
6             chevrolet impala
7            plymouth fury iii
8             pontiac catalina
9           amc ambassador dpl
'''
print("1. 첫글자 대문자: \n", data.str.capitalize())
print("2. 대문자: \n", data.str.upper())
print("3. 소문자: \n", data.str.lower())
print("4. swapcase: \n", data.str.swapcase())
print("5. title: \n", data.str.title())
encode_s = data.str.encode("utf-8")
print("5. encode: \n", encode_s )
decode_s = encode_s.str.decode("utf-8")
print("6. decode: \n", decode_s )
print("7. join", data.str.join(" "))
################################################
series_x = pd.Series(["   hello   ","    xyz", "kkk    "])
print("8. 양쪽공백제거 \n", series_x.str.strip())
print("8. 왼쪽공백제거 \n", series_x.str.lstrip())
print("8. 오른쪽공백제거 \n", series_x.str.rstrip())

series_x = pd.Series(["HHHHhelloHHHHH","HHHHxyz", "kkkHHHHH"])
print("9. 양쪽 H 제거 \n", series_x.str.strip("H"))
print("9. 왼쪽 H 제거 \n", series_x.str.lstrip("H"))
print("9. 오른쪽 H 제거 \n", series_x.str.rstrip("H"))

################################################
series_x = pd.Series(["hello","haPy", "New"])
print("10. 특정문자로 시작? \n", series_x.str.startswith("h")) # boolean 색인 활용
print("11. 특정문자로 끝? \n", series_x.str.endswith("w"))  # boolean 색인 활용

print("12. 특정문자 포함여부? \n", series_x.str.contains("e")) # boolean 색인 활용
print("12. 특정문자 포함된 값 반환? \n", series_x[series_x.str.contains("e")]) # boolean 색인 활용

print("14. 특정문자 위치 반환? \n", series_x.str.find("e")) # 없으면 -1 반환

print("15. SQL lpad? \n", series_x.str.rjust(10,"*")) #
print("15. SQL rpad? \n", series_x.str.ljust(10,"*")) #
print("15. ? \n", series_x.str.center(10,"*")) #

print("16. islower? \n", series_x.str.islower()) #
print("16. isupper? \n", series_x.str.isupper()) #
print("16. isalpha? \n", series_x.str.isalpha()) #
print("16. isdigit? \n", series_x.str.isdigit()) #