# Prompt user for vanity license plate - return boolean if valid according to following rules:

#    “All vanity plates must start with at least two letters.”
#    “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
#    “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
#    “No periods, spaces, or punctuation marks are allowed.”

def main():
    value = input('Plate: ')

    if is_valid(value):
        print('Valid')
    else:
        print('Invalid')


def is_valid(value):
    if not start_with_two_letters(value):
        return False

    if not valid_length(value):
        return False

    if not valid_numbers(value):
        return False

    if not valid_punctuation(value):
        return False

    return True


def start_with_two_letters(value):
    return value[0:1].isalpha() and value[1:2].isalpha()


def valid_length(value):
    return 2 <= len(value) <= 6


def valid_numbers(value):
    number_included = False

    for char in value:
        if char.isdigit():
            if not number_included and char == '0':
                return False
            number_included = True
        if char.isalpha():
            if number_included:
                return False

    return True

def valid_punctuation(value):
    for char in value:
        if not char.isalnum():
            return False

    return True


if __name__ == '__main__':
    main()
