def main():
    value = input('Enter mass: ')

    value = convert(int(value))

    print(value)


def convert(value):
    return value * pow(300000000, 2)


if __name__ == '__main__':
    main()
