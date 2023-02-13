def main():
    greeting = input("Greeting: ").lower().strip()

    if "hello" in greeting:
        payout = "$0"
    elif greeting.startswith("h"):
        payout = "$20"
    else:
        payout = "$100"

    print(payout)


main()
