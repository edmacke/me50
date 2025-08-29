import re
import sys
from datetime import date

import inflect


def main():
    value = input('Date of Birth: ')

    delta = calculate_delta(value)

    print(delta_words(delta))


def delta_words(delta):
    if delta.seconds == 60:
        return 'One minute'

    p = inflect.engine()

    words = p.number_to_words(delta.days * 1440, wantlist=True)

    words = [word.replace(' and ', ' ') for word in words]

    return str.capitalize(', '.join(words) + ' minutes')


def calculate_delta(value):
    match = re.search(r'(\d{4})-(\d{2})-(\d{2})', value)
    if not match:
        sys.exit('Invalid date')

    year = match.group(1)
    month = match.group(2)
    day = match.group(3)

    try:
        dob = date(int(year), int(month), int(day))
    except ValueError:
        sys.exit('Invalid date')

    return date.today() - dob


if __name__ == '__main__':
    main()
