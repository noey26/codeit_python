from random import randint


def generate_numbers(n):
    i = 0
    numbers = []
    while len(numbers) < n:
        number = randint(1, 45)
        if number not in numbers:
            numbers.append(number)
        i += 1

    return numbers


print(generate_numbers(6))