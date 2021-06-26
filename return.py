def square(x):
    print("함수 시작")
    return 3 * 3
    print("함수 끝") # -> dead code

print(square(3))
print("Hello World!")

# return : 값을 리턴함, 함수 즉시 종료

# return vs print

def print_square(x):
    print(x * x)

def get_square(x):
    return x * x

print(get_square(3))
print(print_square(3)) # -> None