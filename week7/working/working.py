import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    match = re.search(r'^(\d{1,2})(:(\d{2}))? (AM|PM)* to (\d{1,2})(:(\d{2}))? (AM|PM)$', s)

    if not match:
        raise ValueError('No regex found')

    from_hrs = check_hours(match.group(1), match.group(4))
    from_mins = check_minutes(match.group(3))

    to_hrs = check_hours(match.group(5), match.group(8))
    to_mins = check_minutes(match.group(7))

    return f'{from_hrs}:{from_mins:02} to {to_hrs}:{to_mins:02}'


def check_hours(value, ampm):
    hours = int(value)

    if 1 <= hours <= 12:
        if ampm.upper() == 'AM':
            return hours
        else:
            return hours + 12

    raise ValueError(f'Value of {value} is invalid')


def check_minutes(value):
    if value is None:
        return 0

    mins = int(value)

    if 0 <= mins <= 59:
        return mins

    raise ValueError(f'Value of {value} is invalid')

    raise ValueError(f'Value of {value} is invalid')


if __name__ == "__main__":
    main()
