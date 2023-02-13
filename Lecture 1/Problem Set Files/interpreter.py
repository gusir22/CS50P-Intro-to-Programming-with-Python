def main():
    expression = input("Expression: ")

    # Parse expression into x, y, and z values
    x, y, z = expression.split(" ")

    # Turn x and z into floats
    x = float(x)
    z = float(z)

    # Calculate expression
    match y:
        case "+":
            ans = x+z
        case "-":
            ans = x-z
        case "*":
            ans = x*z
        case "/":
            ans = x/z

    print(round(ans, 1))


main()
