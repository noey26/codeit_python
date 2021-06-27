import calculator as calc
from calculator import add, multiply
from calculator import * # 함수의 위치가 불분명하기 때문에 비추천

print(calc.add(2, 5))
print(calc.multiply(3, 4))
print(add(2, 5))
print(multiply(3, 4))

# standard library (표준 라이브러리)
import math # log, cos, pi,,,
import random # random, randint, uniform
import os # getlogin, getcwd
import datetime # datetime, .now, .timedelta, .strftime(포맷코드)