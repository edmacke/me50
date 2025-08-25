def main():
    ...


def shorten(word):
    return ''.join([char for char in word if not is_vowel(char)])


def is_vowel(char):
    vowels = ('a', 'e', 'i')

    return char.lower() in vowels


if __name__ == "__main__":
    main()
