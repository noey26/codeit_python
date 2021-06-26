# scope (범위)
# scope : 변수가 사용 가능한 범위
# 로컬 변수 : 변수를 정의한 함수 내에서만 사용 가능
# 글로벌 변수 : 모든 곳에서 사용 가능
# 함수에서 변수를 사용하면, 로컬 변수를 먼저 찾고 나서 글로벌 변수를 찾음

def my_function():
    x = 3 # 로컬변수
    print(x)

my_function()
# --------------------------
x = 2 # 글로벌변수

def my_function2():
    print(x)

my_function2()
print(x)
# --------------------------
x = 2

def my_function3():
    x = 3
    print(x)

my_function3()
print(x)

# 파라미터도 로컬 변수
def square(x):
    return x * x
print(square(3))

