# Ask user for camel case name, output corresponding snake case name

def main():
    value = input('Enter a camel case variable (e.g. firstName): ')

    print(answer(value))


def answer(value):
    return_value = ''

    for char in value:
        if char.isupper():
            return_value += f'_{char.lower()}'
        else:
            return_value += char

    return return_value


if __name__ == '__main__':
    main()
