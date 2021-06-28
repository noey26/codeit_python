import random

with open('vocabulary.txt', 'r') as f:

    ans = ""
    sheet = {}
    i = 1

    for line in f:
        sheet[i] = line.strip()
        i += 1

    while ans != 'q':
        num = random.randint(1,i-1)
        q = sheet[num].split(': ')
        ans = input(f"{q[1]}: ")
        if ans == 'q':
            break
        elif ans == q[0]:
            print("맞았습니다!")
        else:
            print(f"틀렸습니다. 정답은 {q[0]}입니다.")