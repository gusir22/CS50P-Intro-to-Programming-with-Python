def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def separate_at_numbers(s):
    """Returns the portion of the plate string after the first number"""
    index = 0
    for c in s:
        if c.isdigit():
            return s[index:]  # return a portion of the original string starting from the first found digit
        index += 1  # count up the index for next loop

    return None


def is_valid(s):
    """Uses a while loop to test str through various validation requirements. If a fail is triggered, loop
    returns an invalid flag. If all tests pass, loop returns a valid flag"""
    while True:
        # Validates plate starts with at least two letters
        if not s[:2].isalpha():
            return False

        # Validates Max 6 chars, min 2 chars
        if not 2 <= len(s) <= 6:
            return False

        # Validates plate has no periods, spaces, or punctuation
        if not s.isalnum():
            return False

        # extract number sequence, if any
        numbers = separate_at_numbers(s)

        # Validates that no letter goes after a number sequence if str has numbers
        if numbers:  # confirms there are numbers in the sequence
            if not numbers.isdigit():  # These should all be numbers so a letter will trigger the false validation flag
                return False

        # Validates that number sequence, if any, does not start with 0
        if numbers:  # confirms there are numbers in the sequence
            if numbers[0] == "0":
                return False

        return True  # if loop reached here, all validations where approved


if __name__ == "__main__":
    main()
