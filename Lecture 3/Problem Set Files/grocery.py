def main():
    # init empty user input list and grocery list dictionary for loop
    input_list = []
    grocery_list = {}

    while True:
        try:
            item = input().upper()
            input_list.append(item)  # save item to input list
        except EOFError:
            for item in sorted(input_list):  # transfer data from list to dictionary in alphabetical order
                grocery_list = update_grocery_list(item, grocery_list)
            display_grocery_list(grocery_list)
            break


def update_grocery_list(new_item, grocery_list):
    """Updates the grocery store values with a new item"""
    if new_item in grocery_list:  # if item already exists in list,
        grocery_list[new_item] += 1  # add one more quantity
    else:  # if item does not exist in list,
        grocery_list[new_item] = 1  # add the first one

    return grocery_list


def display_grocery_list(grocery_list):
    """Formats and displays the grocery list"""
    for item in grocery_list:
        print(f"{grocery_list[item]} {item}")


main()
