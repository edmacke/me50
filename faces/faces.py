def main():
    msg = input('Enter something with a smile or frown: ')

    msg = fix_msg(msg)

    print(msg)

def fix_msg(msg):
    return msg.replace(':(', '🙁').replace(':)','🙂')

if __name__ == '__main__':
    main()
