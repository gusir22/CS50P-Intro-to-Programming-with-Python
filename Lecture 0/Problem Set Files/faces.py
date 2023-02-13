def convert(message):
    return message.replace(":(", "🙁").replace(":)", "🙂")


def main():
    message = input("Give me a happy or sad face, please... ")
    print(convert(message))


main()
