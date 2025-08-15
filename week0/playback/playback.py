# Given a user-entered string, replace all spaces with elipsis

def main():
    msg = input('Enter something: ')
    msg = fix_msg(msg)
    print(msg)


def fix_msg(msg):
    return msg.replace(' ', '...')


if __name__ == '__main__':
    main()
