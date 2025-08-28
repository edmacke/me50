import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    # Get values matching nnn.nnn.nnn.nnn format
    match = re.search(r'^(\d+)\.(\d+)\.(\d+)\.(\d+?)$', ip)

    # If string doesn't match pattern, return false
    if not match:
        return False

    # Get found groups
    groups = match.groups()

    # If not a group of 4, it's invalid
    if len(groups) != 4:
        return False

    # If all groups are valid, return True
    if valid_range(groups[0]) and valid_range(groups[1]) and valid_range(groups[2]) and valid_range(groups[3]):
        return True

    # At least one group is invalid - return False
    return False


def valid_range(value):
    # Don't allow leading 0's
    if re.search(r'0+\d', value):
        return False

    return 0 <= int(value) <= 255


if __name__ == "__main__":
    main()
