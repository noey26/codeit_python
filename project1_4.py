from random import randint

# 모범 답안 전체
def generate_numbers(n):
    numbers = []

    while len(numbers) < n:
        new_number = randint(1, 45)
        if new_number not in numbers:
            numbers.append(new_number)

    return numbers


def draw_winning_numbers():
    winning_numbers = generate_numbers(7)
    return sorted(winning_numbers[:6]) + winning_numbers[6:]


def count_matching_numbers(numbers, winning_numbers):
    count = 0

    for num in numbers:
        if num in winning_numbers:
            count = count + 1

    return count


def check(numbers, winning_numbers):
    count = count_matching_numbers(numbers, winning_numbers[:6])
    bonus_count = count_matching_numbers(numbers, winning_numbers[6:])

    if count == 6:
        return 1000000000
    elif count == 5 and bonus_count == 1:
        return 50000000
    elif count == 5:
        return 1000000
    elif count == 4:
        return 50000
    elif count == 3:
        return 5000
    else:
        return 0

# 직접 짠 코드
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
    winning_numbers = generate_numbers(6)
    bonus = randint(1, 45)
    if bonus not in winning_numbers:
        winning_numbers.append(bonus)
    return winning_numbers

# 겹치는 번호 카운트
def count_matching_numbers(numbers, winning_numbers):
    count = 0
    for num in numbers:
        if num in winning_numbers[:6]:
            count += 1
    return count

def check(numbers, winning_numbers):
    rank = count_matching_numbers(numbers, winning_numbers)
    cost = 0
    if rank == 6:
        cost = 1000000000
    elif rank == 5:
        if winning_numbers[6] in numbers:
            cost = 50000000
        else:
            cost = 1000000
    elif rank == 4:
        cost = 50000
    elif rank == 3:
        cost = 5000
    else:
        cost = 0
    return cost