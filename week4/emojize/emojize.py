# Given

import emoji


def main():
    value = input('Input: ')

    print('Output: ' + emojify(value))


def emojify(value):
    return emoji.emojize(value, language='alias')


if __name__ == '__main__':
    main()
