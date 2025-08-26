import sys
from csv import DictReader

from tabulate import (tabulate)


def main():
    items = []

    filename = get_filename()

    try:
        with open(filename) as file:
            reader = DictReader(file)
            for item in reader:
                items.append(item)

            print(tabulate(items, headers="keys", tablefmt="grid"))

    except FileNotFoundError:
        sys.exit('File does not exist')


def get_filename():
    if len(sys.argv) < 2:
        sys.exit('Too few command-line arguments')

    if len(sys.argv) > 2:
        sys.exit('Too many command-line arguments')

    filename = sys.argv[1]
    if not filename.lower().endswith('.csv'):
        sys.exit('Not a CSV file')

    return filename


if __name__ == '__main__':
    main()
