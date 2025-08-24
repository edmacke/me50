# User enters an item from the menu, display running total

menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():
    total = 0.0

    while True:
        try:
            value = input('Item: ')

            total += price(value)

            print(f'Total: ${total:.2f}')

        except KeyError:
            continue

        except EOFError:
            return


def price(value):
    return menu[value.title()]


if __name__ == '__main__':
    main()
