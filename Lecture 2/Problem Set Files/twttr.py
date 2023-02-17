def main():
    vowels = "aeiouAEIOU"  # vowel chars

    input_str = input("Input: ")
    output_str = ""  # init empty str to save data in

    # iterate through input string; chars not in the vowels string are not appended to the output string
    for c in input_str:
        if c not in vowels:
            output_str += c

    print(f"Output: {output_str}")


main()
