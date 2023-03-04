import random


def main():
    # init game attributes
    level = get_level()  # difficulty level
    score = 0  # init score board

    # ask 10 questions, one at a time
    for i in range(10):
        # generate the problem and answer
        x = generate_integer(level)
        y = generate_integer(level)
        answer = str(x + y)  # str format to ensure str responses like "cat" are counted as wrong answers

        # collect responses
        attempts = 0  # reset attempts ticker
        while attempts < 3:
            response = input(f"{x} + {y} = ")  # prompt user

            # validate response
            if answer == response:  # if answer is correct,
                score += 1  # add point to score
                break  # go to next question
            else:
                # display error messages
                if attempts == 2:  # if over 3rd attempt,
                    print(f"{x} + {y} = {answer}")  # display answer
                else:
                    print("EEE")  # print standard error message

            attempts += 1  # uptick attempt count

    print(f"Score: {score}")  # print collective score after all questions are asked


def get_level():
    """Prompts the user for a level and returns 1, 2, or 3 only"""
    while True:
        level = input("Level: ")
        if level in ["1", "2", "3"]:
            return int(level)


def generate_integer(level):
    """Returns a randomly generated, non-negative integer with level(n) digits or
    raises a ValueError if level is not 1, 2, or 3"""
    match level:
        case 1:
            return random.randint(0,9)
        case 2:
            return random.randint(10,99)
        case 3:
            return random.randint(100,999)
        case _:
            raise ValueError


if __name__ == "__main__":
    main()
