def main():
    fraction = input("What does the fuel gauge read? ")
    percentage = convert(fraction)
    result = gauge(percentage)
    print(result)


def convert(fraction):
    if "/" in fraction:
        x = int(fraction.split("/")[0])
        y = int(fraction.split("/")[1])

        if y == 0:
            raise ZeroDivisionError
        elif x > y:
            raise ValueError

        return round((x/y)*100)


def gauge(percentage):
    """Formats and prints the percentage to the correct fuel format"""
    if percentage <= 1:
        return "E"
    elif percentage < 99:
        return f"{percentage}%"
    else:
        return "F"


if __name__ == "__main__":
    main()
