import sys


def main():
    if len(sys.argv) < 2:
        sys.exit('Too few command-line arguments')

    if len(sys.argv) > 2:
        sys.exit('Too many command-line arguments')

    filename = sys.argv[1]
    if not filename.lower().endswith('.py'):
        sys.exit('Not a Python file')

    loc = get_count(filename)

    print(loc)


def get_count(filename):
    try:
        with open(filename) as file:
            lines = file.readlines()
    except FileNotFoundError:
        sys.exit('File does not exist')

    loc = 0

    for line in lines:
        line = line.strip()
        if len(line) == 0 or line.startswith('#'):
            continue
        loc += 1

    return loc


if __name__ == '__main__':
    main()
