# In a file called extensions.py, implement a program that prompts the user for the name of a file
# and then outputs that file’s media type if the file’s name ends, case-insensitively, in any of these suffixes:

def main():
    x = input('Enter a file name: ')

    print(mime_type(x))


def mime_type(input):
    value = input.lower().strip()

    if value.endswith('.gif'):
        return 'image/gif'

    if value.endswith('.jpg') or value.endswith('.jpeg'):
        return 'image/jpeg'

    if value.endswith('.png'):
        return 'image/png'

    if value.endswith('.pdf'):
        return 'application/pdf'

    if value.endswith('.txt'):
        return 'text/plain'

    if value.endswith('.zip'):
        return 'application/zip'

    return 'application/octet-stream'


if __name__ == '__main__':
    main()
