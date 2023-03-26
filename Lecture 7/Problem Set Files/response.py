import validators


def main():
    email = input("What's your email address? ")

    if validators.email(email):
        validation = "Valid"
    else:
        validation = "Invalid"

    print(validation)


if __name__ == "__main__":
    main()
