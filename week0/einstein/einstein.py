# Given a user-entered value for mass (m), compute display energy using formula of e=mc^2

def main():
    value = input('Enter mass: ')

    value = convert(int(value))

    print(value)


def convert(value):
    return value * pow(300000000, 2) # Speed of light estimated as 300000000


if __name__ == '__main__':
    main()
