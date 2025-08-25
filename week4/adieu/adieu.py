#

def main():
    names = []

    while True:
        try:
            value = input()

            names.append(value.strip())

        except EOFError:
            print(f'Adieu, adieu, to {join_names(names)}')
            return


def join_names(names):
    if len(names) == 1:
        return names[0]

    if len(names) == 2:
        return f'{names[0]} and {names[1]}'

    return f'{', '.join(names[:-1])}, and {names[len(names) - 1]}'


if __name__ == '__main__':
    main()
