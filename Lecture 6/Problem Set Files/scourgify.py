from csv import DictReader, DictWriter
import sys


def main():
    validate_argv_commands()
    data = read_csv(sys.argv[1])
    data = format_data(data)
    write_csv(sys.argv[2], data, data[0].keys())


def validate_argv_commands():
    """Reads the argv commands passed on by the user. If argv's are invalid, program will exit prematurely"""

    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    for argv in sys.argv[1:]:
        if not argv.endswith(".csv"):
            sys.exit("Not a CSV file")


def read_csv(file_path):
    """Reads the csv file and returns the full data as a list of dictionary"""
    data = []  # init empty list to save row data in from a csv file

    try:
        with open(file_path) as file:
            reader = DictReader(file)  # returns a list based on the csv file's values
            # save field data
            for row in reader:
                data.append(row)  # save row to data list

            return data
    except FileNotFoundError:
        sys.exit("File does not exist")


def write_csv(filename, data, fieldnames):
    """Writes and saves list of dictionary to a csv data"""
    with open(filename, "w", newline="") as file:
        writer = DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()  # write header title

        # save all data to new file
        for row in data:
            writer.writerow(row)


def format_data(data):
    """Formats the data from name and house values to display first, last, and house values"""
    f_data = []  # init empty formatted data list

    for row in data:
        last, first = row["name"].split(", ")  # unpack into first and last name
        # save new formatted data into a dictionary
        f_row = {
            "first": first,
            "last": last,
            "house": row["house"],
        }
        f_data.append(f_row)  # save to formatted data list

    return f_data


if __name__ == "__main__":
    main()
