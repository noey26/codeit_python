# 파일이름에는 파일의 경로를 포함해서 넣어야함
# with open('chicken.txt', 'r') as f:
#     for line in f:
#         print(line.strip)

# strip : 앞과 뒤의 화이트 스페이스를 제거
print("       abc   def     ".strip())

# split
my_string = "1. 2. 3. 4. 5. 6"
print(my_string.split(". "))
full_name = "Kim, Yuna"
print(full_name.split(", "))
name_data = full_name.split(", ")
last_name = name_data[0]
first_name = name_data[1]

x = "     \n\n    2.3   \t   3.4    \n   5.6  7.8  11.1   \n\n".split()
# split을 이용하여 리스트를 만들경우 이 요소는 문자열 타입 -> 형변환
print(x)
y = " ".join(x)
z = y.split(".")
print(z)

# 월 평균 매출 계산
with open('data/chicken.txt', 'r') as f:
    total_revenue = 0
    total_days = 0

    for line in f:
        data = line.strip().split(": ")
        revenue = int(data[1])  # 그날의 매출

        total_revenue += revenue
        total_days += 1

    print(total_revenue / total_days)

# --------------------------------------------------------------

with open('new_file.txt', 'w') as f:
    f.write("Hello world!\n")
    f.write("My name is suyeon")

# 글 추가와 생성을 동시에 가능하게 하기때문에 되도록이면 이것을 사용
with open('new_file.txt', 'a') as f:
    f.write("my age is twenty-six")