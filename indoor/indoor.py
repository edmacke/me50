# Convert a user-entered string to lower-case

def main():
    msg = input('Yell something: ')
    msg = fix_msg(msg)
    print(msg)


def fix_msg(msg):
    return msg.lower()


if __name__ == '__main__':
    main()
