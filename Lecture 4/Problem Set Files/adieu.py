import inflect


def main():

    names = get_names()  # ask user for all names

    p = inflect.engine()  # init inflection engine
    print(f"Adieu, adieu, to {p.join(names)}")  # format and print output string using recommended inflect library


def get_names():
    """Prompts the user for multiple names and saves it to a list. When user exits out of
    prompt by using ctr-D, function returns list"""
    names = []  # init empty list to add names

    while True:
        try:
            user_input = input("Name: ")  # ask user for a name
            names.append(user_input)  # add name to list
        except EOFError:
            break

    return names


if __name__ == "__main__":
    main()
