def main():
    read_names()


def record_name():
    name = input("What's your name? ")
    with open("names.txt", "a") as file:
        file.write(f"{name}\n")  # adds \n to save below previous name in txt file


def read_names():
    names = []  # init empty list to store names

    with open("names.txt", "r") as file:
        for line in file:
            # rstrip removes \n from txt file line so it does not double with the print \n
            names.append(line.rstrip())  # append name data to names lists memory

    # print names in alphabetical order
    for name in sorted(names):
        print(f"Hello, {name}")


if __name__ == "__main__":
    main()
