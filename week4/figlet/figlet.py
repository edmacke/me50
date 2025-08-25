# App expects CLI parms:
# None = use random font
# -f | --font [FONT] = use font (exit if invalid)
#

import sys

import pyfiglet
from pyfiglet import Figlet


def main():
    # Get args after program name
    args = sys.argv[1:]

    if len(args) == 0:
        font = None
    elif len(args) == 2:
        parm = args[0].lower()
        if parm == '-f' or parm == '-font':
            font = args[1]
        else:
            sys.exit('Invalid usage')
    else:
        sys.exit('Invalid usage')

    if font:
        try:
            f = Figlet(font=font)
        except pyfiglet.FontNotFound:
            sys.exit('Invalid usage')
    else:
        f = Figlet()

    text = input('Input: ')

    print(f.renderText(text))


if __name__ == '__main__':
    main()
