# Prompt user to enter a coin, inform user of amount due

def main():
    total = 0

    while True:
        value = int(input('Insert Coin: '))

        if is_valid_coin(value):
            total += value

        if total >= 50:
            break

        print(f'Amount Due: {50 - total}')

    print(f'Change Owed: {total - 50}')


def is_valid_coin(value):
    return value == 5 or value == 10 or value == 25


if __name__ == '__main__':
    main()
