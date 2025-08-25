# Given a fraction, output the percentage


def main():
    while True:
        try:
            value = input('Fraction: ')

            pct = convert(value)

            print(gauge(pct))
            return
        except ValueError:
            print('Enter integer values where x <y and y is not zero')


def gauge(pct):
    if pct <= 1:
        return 'E'

    if pct >= 99:
        return 'F'

    return f'{pct}%'


def convert(fraction):
    values = fraction.split('/')

    x = get_integer(values[0])

    y = get_integer(values[1])

    if y == 0:
        raise ZeroDivisionError('Value of y is zero')

    if x > y:
        raise ValueError(f'Value of {x} is greater than {y}')

    return round((x / y) * 100)


def get_integer(value):
    try:
        return_value = int(value)
    except:
        raise ValueError(f'Value of "{value}" is not an integer')

    if return_value < 0:
        raise ValueError(f'Value of "{value}" is negative')

    return return_value


if __name__ == '__main__':
    main()
