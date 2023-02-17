def main():
    camel_case_variable = input("What is your camelCase variable? ")
    snake_case_variable = translate_camel_case(camel_case_variable)
    print(snake_case_variable)


def translate_camel_case(variable_name):
    """Iterates through the chars of the variable name. When it finds an upper case, the if function
    adds an underscore first and then turns the char into lowercase"""

    results = ""  # init empty result strings to record each char into

    for c in variable_name:  # Uppercase indicates a new word
        if c.isupper():
            results+= "_"
        results += c.lower()  # ensure all chars are lowercase
    return results


main()
