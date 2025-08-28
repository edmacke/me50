import re


def main():
    print(count(input("Text: ")))


def count(s):
    s = ' ' + re.sub('[^a-z0-9]', ' ', s, flags=re.IGNORECASE) + ' '
    s = s.replace(' ', '  ')

    ums = re.findall('[ ]{1}(um)[ ]{1}', s, re.IGNORECASE)

    return len(ums)


if __name__ == "__main__":
    main()
