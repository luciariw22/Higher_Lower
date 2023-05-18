import math


def yes_no(question):
    valid = False
    while not valid:
        response = input("Have you played this game "
                         "before? ").lower()

        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response == "n":
            response = "no"
            return response
        else:
            print("Please answer yes / no")


def instructions():
    print("**** Welcome to the Higher Lower Game ****")
    print()
    print("For each game you will be asked to...\n"
          "- Enter a 'low and 'high number. The computer will randomly\n"
          "generate a 'secret number between your two chosen numbers. It\n"
          "will use these numbers for all rounds in a given game.\n"
          "- The computer will calculate how many guesses you are allowed\n"
          "- enter the number or rounds you want to play"
          "- guess the secret number")
    print()
    print("Good Luck !")
    print()


def int_check(question, low=None, high=None, exit_code=None):
    if low is None and high is None:
        error = "Please enter an integer"
        situation = "any integer"
    if low is not None and high is not None:
        error = f"Please enter an integer between {low} and {high}"
        situation = "both"
    else:
        error = f"Please enter an integer more than {low}"
        situation = "low only"

    while True:
        response = input(question).lower()
        if response == exit_code:
            return response

        try:
            response = int(response)

            # check that integer is valid (ie: not too low / too high etc)
            if situation == "any integer":
                return response

            elif situation == "both":
                if low <= response <= high:
                    return response

            elif situation == "low only":
                if response >= low:
                    return response

            print(error)

        except ValueError:
            print(error)


# main routine goes here

show_instructions = yes_no("have you played the "
                           "game before? ")

if show_instructions == "no":
    instructions()
else:
    print("Program Continues")


rounds_played = 0
rounds_won = 0

low_number = 1
high_number = 10

mode = "regular"

rounds = int_check("How many rounds", 1, exit_code="")

if rounds == "":
    mode = "infinite"
    rounds = 5

# rounds loop
end_game = "no"
while end_game == "no":

    if mode == "infinite":
        heading = f"Round {rounds_played + 1} (infinite mode)"
        rounds += 1
    else:
        heading = f"Round {rounds_played + 1} of {rounds}"

    print(heading)

    rounds_played += 1

    # Start Round!!
    while True:

        secret = 7

        guess = int_check("Guess (or 'xxx' to exit): ", low_number, high_number, "xxx")
        print("you guessed", guess)

        if guess == "xxx":
            end_game = "yes"
            break

            # compare guess to secret number
        print("Pretend we've compared")

        if guess == secret:
            rounds_won += 1
            break

    # check if we are out of rounds
    if rounds_played >= rounds:
        break

# HL component 5 - no duplicates

# To Do
# set up empty list called already_guessed
# when user guesses, add guess to list
# for each guess, check that number is not in already_guessed

# HL component 5 - Prevents duplicate guesses

SECRET = 7
GUESSES_ALLOWED = 5

already_guessed = []
guesses_left = GUESSES_ALLOWED
num_won = 0

guess = ""

while guess != SECRET and guesses_left >= 1:

    guess = int(input("Guess: "))

    # checks that guess is not a duplicate
    if guess in already_guessed:
        print("You already guessed that number! Please try again.")
        continue

        guesses_left -= 1
        already_guessed.append(guess)

        if guesses_left >= 1:

            if guess < SECRET:
                print("Too low, try a higher number. Guesses left:", guesses_left)
            elif guess > SECRET:
                print("Too high, try a lower number. Guesses left:", guesses_left)
        else:
            if guess < SECRET:
                print("Too low!")
            elif guess > SECRET:
                print("Too high!")

if guess == SECRET:
    if guesses_left == GUESSES_ALLOWED:
        print("Amazing! You got it!")
    else:
        print("Well done, you got it!")

# HL component 11 - Maximum Guesses Calculator

import math

for item in range(0,4):     # loop component for east testing...

    low = int(input("Low: "))   # use int check in due course
    high = int(input("High: ")) # use int check in due course

    range = high - low + 1
    max_raw = math.log2(range) # finds maximum # of guesses
    max_upped = math.ceil(max_raw)
    max_guesses = max_upped + 1
    print("Max Guesses: {}".format(max_guesses))

    print()




