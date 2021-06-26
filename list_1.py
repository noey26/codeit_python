numbers = []
x = [19, 13, 2, 5, 3, 11, 7, 17]

numbers.extend(x) # append는 하나씩 넣을 수 있고, extend는 한꺼번에 수를 넣을 수 있다.
print(numbers)

new_list = sorted(numbers, reverse=True) # 기존 리스트는 건드리지 않고, 정렬된 새로운 리스트를 리턴
print(new_list)
print(numbers)

print(numbers.sort())
numbers.sort() # 아무것도 리턴하지 않고, 기존 리스트를 정렬
print(numbers)
numbers.sort(reverse=True)

# ex 섭씨 온도에서 화씨 온도로 바꿔주는 함수
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

temperature_list = [40, 15, 32, 64, -4, 11]
print("화씨 온도 리스트: " + str(temperature_list))

i = 0
while i < len(temperature_list):
    temperature_list[i] = round(fahrenheit_to_celsius(temperature_list[i]), 1)
    i += 1

print("섭씨 온도 리스트: {}".format(temperature_list))