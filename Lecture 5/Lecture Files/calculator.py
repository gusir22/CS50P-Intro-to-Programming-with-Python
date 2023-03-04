def main():
    x = int(input("What's x? "))
    print(f"{x} squared is", square(x))


def square(n):
    """Squares a number"""
    return pow(n, 2)


if __name__ == "__main__":
    main()
