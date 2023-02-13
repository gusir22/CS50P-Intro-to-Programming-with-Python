def main():
    hello()  # prints default parameter value
    name = input("What's your name? ")
    hello(name)  # prints custom parameter value


def hello(name="There"):
    """Says hello to user by name"""
    print("Hello", name.strip().title())


main()
