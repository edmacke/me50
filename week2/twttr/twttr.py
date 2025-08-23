# Prompt user for a string, return with vowels removed

def main():
    value = input('Enter something: ')

    print(answer(value))


def answer(value):
    return ''.join([char for char in value if not is_vowel(char) ])


def is_vowel(char):
    vowels = ('a', 'e', 'i', 'o', 'u')

    return char.lower() in vowels

if __name__ == '__main__':
    main()
