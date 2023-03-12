import csv
import sys
from tabulate import tabulate


def main():
    file = get_argv_commands()
    data = read_csv(file)
    print(tabulate(data, headers="firstrow", tablefmt="grid"))


def get_argv_commands():
    """Reads the argv commands passed on by the user. After validating arvg command is valid,
    returns the command-line argument as a string"""

    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")

    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    if not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")

    return sys.argv[1]


def read_csv(file_path):
    """Reads the csv file and returns the full data as a list of lists"""
    data = []  # init empty list to save row data in from a csv file

    try:
        with open(file_path) as file:
            reader = csv.reader(file)  # returns a list based on the csv file's values
            # save field data
            for row in reader:
                data.append(row)  # save row to data list

            return data
    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()
