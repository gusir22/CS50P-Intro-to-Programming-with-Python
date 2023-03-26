import re


def main():
    time = convert(input("Hours: "))
    print(time)


def convert(s):
    if matches := re.search(r"(\d?\d)(?::(\d\d))?( AM| PM)? to (\d?\d)(?::(\d\d))?( AM| PM)?", s):
        s_time = matches.groups()[0:3]  # start time values
        e_time = matches.groups()[3:6]  # end time values

        # validate and process tuple time data for the start and end time separately
        s_time = parse_time(s_time)
        e_time = parse_time(e_time)

        return f"{s_time} to {e_time}"

    else:
        raise ValueError


def parse_time(time):
    """Turns a tuple of time values into a 24-hour formatted time string"""
    hour, minutes, meridiem = time  # unpack tuple

    # if minutes not provided, save as "00" value
    if not minutes:
        minutes = "00"

    # if meridiem not provided, save as "" value
    if not meridiem:
        meridiem = ""

    # turn time values into strings
    hour = int(hour)
    minutes = int(minutes)

    # validate for time ranges
    if not 0 < hour <= 12:  # hour must be from 1 to 12 before conversion
        raise ValueError
    if not 0 <= minutes < 60:  # minutes must be from 0 to 59 to be valid
        raise ValueError

    # Adjust for meridiem into 24-hour format
    if meridiem.lstrip() == "PM" and hour <= 11:  # adds 12 hours for PM meridiems under 12
        hour = hour + 12
    elif meridiem.lstrip() == "AM" and hour == 12:  # ensures 12 AM reflects as midnight
        hour = 0

    return f"{hour:02}:{minutes:02}"


if __name__ == "__main__":
    main()
