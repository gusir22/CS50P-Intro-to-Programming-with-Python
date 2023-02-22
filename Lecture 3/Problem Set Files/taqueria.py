def main():
    menu = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

    # Set initial balance
    total_balance = 0.00

    while True:
        try:
            item = input("Item: ").title()
        except EOFError:
            break
        else:
            total_balance = update_balance(item, menu, total_balance)


def update_balance(item, menu, total_balance):
    """Updates the total balance while printing the current value"""
    try:
        total_balance += menu[item]
        print(f"Total: ${total_balance}0")
        return total_balance
    except KeyError:
        pass


main()
