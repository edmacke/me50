# In a file called interpreter.py, implement a program that prompts the user for an arithmetic expression
# and then calculates and outputs the result as a floating-point value formatted to one decimal place.
# Assume that the user’s input will be formatted as x y z, with one space between x and y and one space between y and z, wherein:
#
#     x is an integer
#     y is +, -, *, or /
#     z is an integer
#
# For instance, if the user inputs 1 + 1, your program should output 2.0. Assume that, if y is /, then z will not be 0.


def main():
    value = input('Enter an integer, an operator, and another integer: ')

    print(interpret(value))


def interpret(value):
    values = value.split(' ')

    answer = math_it(values)

    return f'{answer:.1f}'


def math_it(values):
    value1 = int(values[0])
    value2 = int(values[2])

    match values[1]:
        case '+':
            return float(value1 + value2)
        case '-':
            return float(value1 - value2)
        case '*':
            return float(value1 * value2)
        case '/':
            return float(value1 / value2)
        case _:
            return 0.0


if __name__ == '__main__':
    main()
