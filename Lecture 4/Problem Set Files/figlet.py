import random
import sys
from pyfiglet import Figlet


def main():
    font_list = [
        "slant",
        "rectangles",
        "alphabet",
    ]

    if len(sys.argv) == 1:  # if executed with no additional args,
        random_index = random.choice(font_list)  # Pick random font from list
        print_figlet(random_index)
    elif len(sys.argv) == 3:  # if executed with font provided in args,
        if sys.argv[1] in ["-f", "--font"] and sys.argv[2] in font_list:  # validate command,
            print_figlet(sys.argv[2])
        else:
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")


def print_figlet(font):
    """Prints a fliglet with a specific font"""
    # ask user for text to print
    text = input("Input: ")

    # configure figlet object
    figlet = Figlet()
    figlet.setFont(font=font)

    # print figlet
    print(figlet.renderText(text))


if __name__ == "__main__":
    main()
