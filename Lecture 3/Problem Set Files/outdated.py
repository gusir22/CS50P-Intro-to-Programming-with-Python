def main():
    while True:
        date = input("Date: ")

        try:
            month, day, year = date.split("/")
        except ValueError:
            try:
                month, day, year = date.split()
            except ValueError:
                # Triggers when user does not provide the three date attributes (month, day, and year)
                continue
            else:
                # Validate user typed date with correct format
                month = fetch_month_number(month)
                day = validate_for_comma(day)

        # turn all date attributes into integers and validate their ranges
        month = format_month(month)
        day = format_day(day)
        year = int(year)

        if 0 < month <= 12:
            if 0 < day <= 31:
                if 1000 <= year <= 9999:
                    print(f"{year}-{month:02}-{day:02}")
                    break


def format_month(month):
    """Tries to turn month string into and integer; if it can't, the function sets up the month value to
    fail validation later on and resulting in prompting the user again"""
    try:
        return int(month)
    except ValueError:
        return 66  # Execute Order 66...


def format_day(day):
    """Tries to turn day string into and integer; if it can't, the function sets up the day value to
    fail validation later on and resulting in prompting the user again"""
    try:
        return int(day)
    except ValueError:
        return 66  # Execute Order 66...


def validate_for_comma(day):
    """Validates user used proper format for the day. If the function finds the comma in the string,
    it will erase it and format the day properly; if it does not find the comma, it will change the value
    to fail validation later and result in prompting the user again"""
    if "," in day:
        return day[:-1]
    else:
        return "66"  # Execute Order 66...


def fetch_month_number(month):
    """Uses the month written value provided to return the month number value.
    If month not found in list, return value that will fail validation to cause the program to ask
    the user for a new date. Good soldiers follow orders..."""
    month_list = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    try:
        return month_list.index(month) + 1  # match month by index and add 1 to adjust for correct month number
    except ValueError:
        return "66"  # Execute Order 66...


main()
