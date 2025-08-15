# In deep.py, implement a program that prompts the user for the answer to the Great Question of Life, the Universe and Everything,
# outputting Yes if the user inputs 42 or (case-insensitively) forty-two or forty two. Otherwise output No.

def main():
    msg = input('What is the answer to the Great Question of Life, the Universe and Everything: ')

    print(answer(msg))


def answer(msg):
    match msg.lower().strip():
        case "42" | "forty-two" | "forty two":
            return "Yes"
        case _:
            return "No"


if __name__ == '__main__':
    main()
