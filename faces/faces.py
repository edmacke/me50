# Replace a string that has an emoji with the character representation of that emoji

def main():
    msg = input('Enter something with a smile or frown: ')

    msg = fix_msg(msg)

    print(msg)


def fix_msg(msg):
    return msg.replace(':(', '🙁').replace(':)', '🙂')


if __name__ == '__main__':
    main()
