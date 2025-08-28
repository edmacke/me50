import validators

def main():
    value = input('What''s your email address? ')

    print('Valid' if valid(value) else 'Invalid')


def valid(value):
    return validators.email(value)


if __name__ == '__main__':
    main()
