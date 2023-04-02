from datetime import date
import re
import sys
import inflect


def main():
    user_input = input("Date of Birth: ")  # prompt user
    birthdate = get_birthdate(user_input)  # parse input into a birthdate object
    minutes = calculate_total_minutes(birthdate)  # convert timedelta into minutes
    translation = translate_to_words(minutes)  # translate int to english
    print(translation)  # print translation results


def get_birthdate(birthdate):
    """Parses a str in the YYYY-MM-DD format and returns a date object"""

    match = re.search(r"^(\d\d\d\d)-(\d\d)-(\d\d)$", birthdate)  # validate for matches

    try:
        # parse birthdate info into separate ints
        year = int(match.groups()[0])
        month = int(match.groups()[1])
        day = int(match.groups()[2])
    except AttributeError:
        sys.exit("Invalid Date")  # reject any input not in YYYY-MM-DD format
    else:
        return date(year, month, day)


def calculate_total_minutes(birthdate):
    """Given a date object from the past, function will return the deltatime in minutes
    from today's date as an int"""
    today = date.today()  # get today's date
    timedelta = today - birthdate  # initialize a timedelta object
    total_minutes = round(timedelta.total_seconds() / 60)  # calculate mins by dividing total_seconds by 60
    return total_minutes  # return int


def translate_to_words(integer):
    """Translates any integer into an english-written string"""
    p = inflect.engine()  # start engine
    words = p.number_to_words(integer)  # translate int to written word string
    words = re.sub(" and ", " ", words)  # replace and with a space to eliminate from translation
    words = words + " minutes"  # append " minutes" suffix to format translation
    return words.capitalize()


if __name__ == "__main__":
    main()
