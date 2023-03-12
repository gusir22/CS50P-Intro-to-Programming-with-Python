import csv


def main():
    write_to_csv()
    read_csv()


def read_csv():
    """Reads the csv file and prints data"""
    students = []

    with open("students.csv") as file:
        # this method prevents assuming order of columns
        reader = csv.DictReader(file)  # returns a list of dictionary based on the csv files separated by rows
        for row in reader:
            students.append({"name": row['name'], "home": row['home']})  # key names taken from first row of csv file

    # Using lambda function to more cleanly use a function only once in the program
    # to print in alphabetical order of homes
    for student in sorted(students, key=lambda student: student["home"]):
        print(f"{student['name']} is in {student['home']}")


def write_to_csv():
    name = input("What's your name? ")
    home = input("Where's your home? ")

    with open("students.csv", "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "home"])
        writer.writerow({"name": name, "home": home})


if __name__ == "__main__":
    main()
