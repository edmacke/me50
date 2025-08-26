import sys
from csv import DictReader, DictWriter


def main():
    items = []

    input_filename, output_filename = get_filenames()

    try:
        with open(input_filename) as file:
            reader = DictReader(file)
            for item in reader:
                items.append(item)
    except FileNotFoundError:
        sys.exit(f'Could not read {input_filename}')

    for item in items:
        names = item['name'].split(', ')
        item['last'] = names[0]
        item['first'] = names[1]

    with open(output_filename, 'w', newline='') as file:
        writer = DictWriter(file, fieldnames=['first', 'last', 'house'], extrasaction='ignore')
        writer.writeheader()
        writer.writerows(items)


def get_filenames():
    if len(sys.argv) < 3:
        sys.exit('Too few command-line arguments')

    if len(sys.argv) > 3:
        sys.exit('Too many command-line arguments')

    input_filename = sys.argv[1]
    if not input_filename.lower().endswith('.csv'):
        sys.exit('Not a CSV file')

    output_filename = sys.argv[2]
    if not output_filename.lower().endswith('.csv'):
        sys.exit('Not a CSV file')

    return input_filename, output_filename


if __name__ == '__main__':
    main()
