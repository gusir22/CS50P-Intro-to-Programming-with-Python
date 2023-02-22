def main():
    numerator, denominator = get_fraction("What does the fuel gauge read? ")
    percentage = convert_to_percentage(numerator, denominator)
    display_formatted_percentage(percentage)


def convert_to_percentage(numerator, denominator):
    """Turns any fraction into a percentage rounded to the nearest integer"""
    while True:
        try:
            numerator = int(numerator)
            denominator = int(denominator)

            decimal = numerator / denominator

            return round(decimal * 100)
        except (ValueError, ZeroDivisionError):
            numerator, denominator = get_fraction("No, really. What does it say? ")


def get_fraction(prompt):
    """Asks the user for a fraction and returns the numerator and denominator as strings to preserve trailing zeros"""
    while True:
        fraction_string = input(prompt)

        # validates fraction format
        if "/" not in fraction_string:
            continue

        fraction_split = fraction_string.split("/")
        numerator = fraction_split[0]
        denominator = fraction_split[1]

        return numerator, denominator


def display_formatted_percentage(percentage):
    """Formats and prints the percentage to the correct fuel format"""
    if percentage > 100:  # Validates numerator is never greater than denominator
        main()
    elif percentage <= 1:
        print("E")
    elif percentage < 99:
        print(f"{percentage}%")
    else:
        print("F")


main()
