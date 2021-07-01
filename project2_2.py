def take_guess():
    print("숫자 3개를 하나씩 차례대로 입력하세요.")
    new_guess = []
    i = 0
    while len(new_guess) < 3:
        user_number = int(input("{}번째 숫자를 입력하세요: ".format(i + 1)))
        i += 1
        if 9 < user_number or user_number < 0:
            print("범위를 벗어나는 숫자입니다. 다시 입력하세요.")
            i -= 1
            continue
        elif user_number in new_guess:
            print("중복되는 숫자입니다. 다시 입력하세요.")
            i -= 1
            continue
        else:
            new_guess.append(user_number)
    return new_guess



# 모범 답안

def take_guess():
    print("숫자 3개를 하나씩 차례대로 입력하세요.")

    new_guess = []
    while len(new_guess) < 3:
        new_num = int(input("{}번째 숫자를 입력하세요: ".format(len(new_guess) + 1)))

        if new_num < 0 or new_num > 9:
            print("범위를 벗어나는 숫자입니다. 다시 입력하세요.")
        elif new_num in new_guess:
            print("중복되는 숫자입니다. 다시 입력하세요.")
        else:
            new_guess.append(new_num)

    return new_guess