def main():
    name = input("What's your name? ")
    print(hello(name))  # prints custom parameter value


def hello(name="World!"):
    """Says hello to user by name"""
    return f"Hello, {name}"


if __name__ == "__main__":
    main()
