#

def main():
    items = {}

    while True:
        try:
            value = input()

            add_item(value, items)

        except EOFError:
            for key, value in sorted(items.items()):
                print(f'{value} {key.upper()}')
            return


def add_item(item, items):
    try:
        items[item] += 1
    except KeyError:
        items[item] = 1


if __name__ == '__main__':
    main()
