import random
import sys


def main():
    # init game
    level = get_int("Level: ")  # prompt user for difficulty level
    answer = random.randrange(level)  # pick a random number for the user to guess withing the given level difficulty

    # start game
    while True:
        guess = get_int("Guess: ")  # prompt user for guess

        # handle results
        if guess < answer:
            print("Too small!")
        elif guess > answer:
            print("Too large!")
        else:
            print("Just right!")
            sys.exit()


def get_int(message):
    """Prompts the user for a positive integer and returns the value"""
    while True:
        try:
            i = int(input(message))
        except ValueError:
            pass
        else:
            if i > 0:
                return i


if __name__ == "__main__":
    main()
