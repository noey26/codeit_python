name = input("이름을 입력하세요: ")
print(name)
# print(name + 5) # input 리턴값은 문자열

import random

# 코드를 작성하세요.
number = random.randint(1, 20)

for i in range(1, 5):
    user = int(input("기회가 {}번 남았습니다. 1-20 사이의 숫자를 맞혀 보세요: ".format(5 - i)))
    if number == user:
        print("축하합니다. {}번 만에 숫자를 맞히셨습니다.".format(i))
        break
    elif user > number:
        print("Down")
    else:
        print("Up")

    if i == 4 and number != user:
        print("아쉽습니다. 정답은 {}입니다.".format(number))

# 모범 답안
import random

# 상수 정의
ANSWER = random.randint(1, 20)
NUM_TRIES = 4

# 변수 정의
guess = -1
tries = 0

while guess != ANSWER and tries < NUM_TRIES:
    guess = int(input("기회가 {}번 남았습니다. 1-20 사이의 숫자를 맞혀보세요: ".format(NUM_TRIES - tries)))
    tries += 1

    if ANSWER > guess:
        print("Up")
    elif ANSWER < guess:
        print("Down")

if guess == ANSWER:
    print("축하합니다. {}번 만에 숫자를 맞히셨습니다.".format(tries))
else:
    print("아쉽습니다. 정답은 {}입니다.".format(ANSWER))