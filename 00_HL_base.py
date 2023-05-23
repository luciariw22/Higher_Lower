import random


# Functions go here
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

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
    elif low is not None and high is not None:
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

    already_guessed = []
    guesses_allowed = 10

    guesses_left = guesses_allowed

    if mode == "infinite":
        heading = f"Round {rounds_played + 1} (infinite mode)"
        rounds += 1
    else:
        heading = f"Round {rounds_played + 1} of {rounds}"

    print(heading)

    rounds_played += 1
    secret = random.randint(low_number, high_number)

    # Start Round!!
    while True:

        print("spoiler alert: ", secret)

        guess = int_check("Guess (or 'xxx' to exit): ", low_number, high_number, "xxx")
        print("you guessed", guess)

        if guess == "xxx":
            end_game = "yes"
            break

        if guess in already_guessed:
            print("You already guessed that number! Please try again."
                  "You *still* have {} guesses left".format(guesses_left))
            continue

        guesses_left -= 1
        already_guessed.append(guess)

        # compare guess to secret number
        if guesses_left >= 1:

            if guess < secret:
                print("Too low, try a higher number/ Guesses left: ")

            elif guess > secret:
                print("Too high, try a lower number. Guesses left: ")
        else:
            if guess < secret:
                print("Too low!")
            elif guess > secret:
                print("Too high!")

        if guess == secret:
            rounds_won += 1
            print("you got it")
            break

    # check if we are out of rounds
    if rounds_played >= rounds:
        break
