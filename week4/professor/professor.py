#     Prompts the user for a level, 𝑛
#     . If the user does not input 1, 2, or 3, the program should prompt again.
#     Randomly generates ten (10) math problems formatted as X + Y = , wherein each of X and Y is a non-negative integer with 𝑛
#     digits. No need to support operations other than addition (+).
#
# Note: The order in which you generate x and y matters. Your program should generate random numbers in x, y pairs to simulate generating one math question at a time (e.g., x0 with y0, x1 with y1, and so on).
#
#     Prompts the user to solve each of those problems. If an answer is not correct (or not even a number), the program should output EEE and prompt the user again, allowing the user up to three tries in total for that problem. If the user has still not answered correctly after three tries, the program should output the correct answer.
#     The program should ultimately output the user’s score: the number of correct answers out of 10.

import random


def main():
    level = get_level()
    correct = 0

    for index in range(10):
        x, y = generate_pair(level)

        if guess_correct(x, y):
            correct += 1

    print(f'Score: {correct}')


def guess_correct(x, y):
    guesses = 0

    answer = x + y

    while guesses < 3:
        guesses += 1

        value = input(f'{x} + {y} = ')

        try:
            guess = int(value)
            if guess == answer:
                return True
            raise ValueError('Answer is not correct')
        except ValueError:
            print('EEE')

    print(f'{x} + {y} = {answer}')
    return False


def get_level():
    while True:
        value = input('Level: ')

        try:
            level = int(value)

            if 1 <= level <= 3:
                return level

        except ValueError:
            ...


def generate_pair(level):
    x = generate_integer(level)
    y = generate_integer(level)

    return x, y


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)

    if level == 2:
        return random.randint(10, 99)

    if level == 3:
        return random.randint(100, 999)

    raise ValueError('Level must be between 1 and 3, inclusive')


if __name__ == "__main__":
    main()
