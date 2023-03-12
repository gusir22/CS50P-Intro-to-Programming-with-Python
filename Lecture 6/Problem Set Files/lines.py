import sys


def main():
    loc = []  # init empty list to store valid lines of code
    file = get_file()  # get file path based on argv command

    try:
        with open(file, "r") as file:
            for line in file:
                if not is_comment(line) and not line.isspace():  # if line is not a comment or blank line,
                    loc.append(line)  # add to valid lines list
    except FileNotFoundError:
        sys.exit("File does not exist")

    print(len(loc))  # print the quantity of lines of code found


def get_file():
    """Validates proper argv command file path. There MUST only be one additional argv command passed that
    represents the file path we want to count the LOCs of"""

    # Validate correct amount of argvs
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")

    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    file = sys.argv[1]  # save file path into variable

    # validate if file at path is a python file
    if file.endswith(".py"):
        return file
    else:
        sys.exit("Not a Python file")


def is_comment(line):
    """Determines if a line of python code is a comment line"""

    if line.lstrip().startswith("#"):  # finds comments, even when indented by removing left whitespace
        return True
    else:
        return False


if __name__ == "__main__":
    main()
