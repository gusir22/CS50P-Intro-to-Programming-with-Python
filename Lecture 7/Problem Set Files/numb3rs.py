import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    matches = re.search(r"^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip)

    try:
        for match in matches.groups():
            if int(match) > 255:  # ensures groups are all within an IPv4 range of 0-255
                return False
    except AttributeError:  # triggers if regex finds no matches
        return False
    else:
        return True


if __name__ == "__main__":
    main()
