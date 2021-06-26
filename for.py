my_list = [2, 3, 5, 7, 11]

for number in my_list:
    print(number)

for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    print(i)

# for i in range(start, stop):
#    print(i) # start부터 stop-1 까지의 범위
# for i in range(stop):
#    print(i)
# for i in range(start, stop, step):
#    print(i)
# 간편함, 깔끔함, 메모리 효율성

numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

for i in range(len(numbers)):
    print(i, numbers[i])

# 2의 제곱
for i in range(11):
    print("{}^{} = {}".format(2, i, 2 ** i))

# 구구단
for i in range(1, 10):
    for j in range(1, 10):
        print("{} * {} = {}".format(i, j, i * j))

# 피타고라스 삼조
for a in range(1, 333):
    for b in range(a + 1, 500):
        c = 1000 - b - a
        if (a * a) + (b * b) == c * c and a < b < c:
            print(a * b * c)

# 리스트 뒤집기
numbers = [2, 3, 5, 7, 11, 13, 17, 19]

# 리스트 뒤집기
for left in range(len(numbers) // 2):
    # 인덱스 left와 대칭인 인덱스 right 계산
    right = len(numbers) - left - 1

    # 위치 바꾸기 (튜플개념)
    numbers[right], numbers[left] = numbers[left], numbers[right]

    # 또다른 방법
    # temp = numbers[left]
    # numbers[left] = numbers[right]
    # numbers[right] = temp

print("뒤집어진 리스트: " + str(numbers))