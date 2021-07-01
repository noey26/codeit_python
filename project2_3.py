# 모범 답안
def get_score(guess, solution):
    strike_count = 0
    ball_count = 0

    for i in range(3):
        if guess[i] == solution[i]:
            strike_count += 1
        elif guess[i] in solution:
            ball_count += 1

    return strike_count, ball_count

# 내가 짠 코드
def get_score(guess, solution):
    strike_count = 0
    ball_count = 0

    for i in guess:
        if i in solution:
            x = solution.index(i)
            y = guess.index(i)
            if x == y:
                strike_count += 1
            else:
                ball_count += 1

    return strike_count, ball_count