from random import randint


def generate_numbers(n):
    numbers = []
    while len(numbers) < n:
        number = randint(1, 45)
        if number not in numbers:
            numbers.append(number)
    return numbers

# 보너스 번호 추첨
def draw_winning_numbers():
    numbers = generate_numbers(6)
    bonus = randint(1, 45)
    if bonus not in numbers:
        numbers.append(bonus)
    return numbers

print(draw_winning_numbers())

# 모범답안-----------------------------------------
def draw_winning_numbers():
    winning_numbers = generate_numbers(7)
    return sorted(winning_numbers[:6]) + winning_numbers[6:]