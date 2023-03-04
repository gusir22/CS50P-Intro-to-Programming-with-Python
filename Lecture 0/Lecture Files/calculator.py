def main():
    x = int(input("What's x? "))
    y = int(input("What's y? "))
    print(f"{x} squared is", square(x))

    print(f"{x} to the power of {y} is", pow(x,y))


def square(n):
    """Squares a number"""
    return pow(n,2)


if __name__ == "__main__":
    main()