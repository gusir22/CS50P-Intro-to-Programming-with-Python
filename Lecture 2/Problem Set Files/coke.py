def main():
    balance = 0
    while True:
        coin = validate_coin(int(input("Enter Coin: ")))
        balance = balance + coin  # update current balance

        # If balance is 50 or higher, vends coke and change
        if balance >= 50:
            print("*Vending Coke*")
            change = balance - 50
            print(f"Change Owed: {change}")
            break
        else:
            print(f"Your balance is {balance} cents")
            amount_due = 50 - balance
            print(f"Amount Due: {amount_due}")

        print("")  # add whitespace between times asked to insert coin


def validate_coin(coin):
    match coin:
        case 5 | 10 | 25:
            return coin
        case _:  # ignores all coins not acceptable
            print(f"This machine does not accept {coin} cent coins. 5, 10, or 25 cents ONLY!")
            return 0


main()
