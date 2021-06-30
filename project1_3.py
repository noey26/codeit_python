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
    total = generate_numbers(6)
    bonus = randint(1, 45)
    if bonus not in total:
        total.append(bonus)
    return total

# 겹치는 번호 카운트
def count_matching_numbers(numbers, total):
    count = 0
    for num in numbers:
        if num in total:
            count += 1
    return count