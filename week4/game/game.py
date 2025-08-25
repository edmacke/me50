#
import random


def main():
    level = get_level('Level: ')

    answer = random.randint(1, level)

    while True:
        guess = get_level('Guess: ')

        if guess < answer:
            print('Too small!')
            continue

        if guess > answer:
            print('Too large!')
            continue

        print('Just right!')
        return


def get_level(prompt):
    while True:
        value = input(prompt)

        try:
            int_value = int(value)

            if int_value >= 1:
                return int_value
        except ValueError:
            ...


if __name__ == '__main__':
    main()
