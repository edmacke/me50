import os
import sys

from PIL import Image, ImageOps


def main():
    input_filename, output_filename = get_filenames()

    try:
        with Image.open(input_filename) as input_image, Image.open('shirt.png') as shirt_image:
            image = ImageOps.fit(input_image, size=(600, 600))
            image.paste(shirt_image, box=shirt_image)
            image.save(output_filename)

    except FileNotFoundError:
        sys.exit(f'Could not read {input_filename}')


def get_filenames():
    if len(sys.argv) < 3:
        sys.exit('Too few command-line arguments')

    if len(sys.argv) > 3:
        sys.exit('Too many command-line arguments')

    input_filename, input_ext = get_filename_ext(sys.argv[1])
    if input_ext == '.jpg' or input_ext == '.jpeg' or input_ext == '.png':
        ...
    else:
        sys.exit('Invalid input')

    output_filename, output_ext = get_filename_ext(sys.argv[2])
    if output_ext == '.jpg' or output_ext == '.jpeg' or output_ext == '.png':
        ...
    else:
        sys.exit('Invalid output')

    if input_ext != output_ext:
        sys.exit('Input and output have different extensions')

    return input_filename, output_filename


def get_filename_ext(filename):
    _, ext = os.path.splitext(filename.lower())
    return filename, ext


if __name__ == '__main__':
    main()
