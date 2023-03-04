def main():
    input_str = input("Input: ")  # ask user for string to shorten
    output_str = shorten(input_str)  # format string
    print(f"Output: {output_str}")  # display output string for user


def shorten(word):
    """Shortens a word by removing all vowels"""
    # prepare function
    vowels = "aeiouAEIOU"  # vowel chars
    output_str = ""  # init empty str to save data in

    # iterate through input string; chars not in the vowels string are not appended to the output string
    for c in word:
        if c not in vowels:
            output_str += c

    return output_str


if __name__ == "__main__":
    main()
