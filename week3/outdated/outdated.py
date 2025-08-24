# Given an string input, convert to yyyy-mm-dd format

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


def main():
    while True:
        try:
            value = input('Date: ')
            print(iso8601(value))
            return
        except ValueError:
            continue


def iso8601(value):
    # See if entry is mm/dd/yyyy
    if '/' in value:
        parts = value.split('/')
        return valid_date(parts[0], parts[1], parts[2])

    # Entry has to be month d, yyyy
    if ',' in value:
        parts = value.split(' ')
        try:
            month = months.index(parts[0].title())
        except ValueError:
            raise ValueError(f'Month of "{parts[0]}" is invalid')

        return valid_date(month + 1, parts[1].replace(',', ''), parts[2])

    raise ValueError(f'Input of {value} was not valid')


def valid_date(value1, value2, value3):
    month = convert_int(value1)
    day = convert_int(value2)
    year = convert_int(value3)

    if month < 1 or month > 12:
        raise ValueError(f'Month of "{month} is invalid')

    if day < 1 or day > 31:
        raise ValueError(f'Month of {day} is invalid')

    return f'{year:04}-{month:02}-{day:02}'


def convert_int(value):
    return int(value)


if __name__ == '__main__':
    main()
