def main():
    greeting = input("Greeting: ")
    payout = value(greeting)
    print(f"${payout}")


def value(greeting):
    """Returns the value of a payout based on the criteria of a greeting."""
    greeting = greeting.lower().strip()  # format for processing
    if greeting.startswith("h"):
        if greeting.startswith("hello"):
            return 0  # starts with 'hello'
        else:
            return 20  # starts with 'h' but no 'hello'
    else:
        return 100  # starts with anything but 'h'


if __name__ == "__main__":
    main()
