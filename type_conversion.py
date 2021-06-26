print(int(3.8))
print(float(3))
print(int("2") + int("5"))
print(float("1.1") + float("2.5"))

print(str(2) + str(5))
age = 7
print("제 나이는 " + str(age) + "살 입니다.")
#print(int("Hello world!")) # -> 오류

year = 2021
month = 6
day = 24

print("오늘은 " + str(year) + "년 " + str(month) + "월 " + str(day) + "일입니다.")

date_string = "오늘은 {}년 {}월 {}일입니다."
print(date_string.format(year, month, day))

print("저는 {1}, {0}, {2}를 좋아합니다!".format("박지성", "유재석", "빌 게이츠"))

num_1 = 1
num_2 = 3
print("{0} 나누기 {1}은 {2:.0f}입니다.".format(num_1, num_2, num_1/num_2))

name = "이수연"
age = 26
print(f"제 이름은 {name}이고 {age}살입니다.")