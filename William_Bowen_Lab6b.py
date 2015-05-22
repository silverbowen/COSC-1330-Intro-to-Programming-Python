# William_Bowen_Lab6b
# This program is a random number
# guessing game

# First load the random module
import random

# set parameters globally in case
# we want to change them later
LOWER_BOUND = 1
UPPER_BOUND = 1000
RANGE = 10

# define main
def main():
    # initialize again
    again = 'Yes'
    # check if player wants to play again
    while play_again(again):
        # Generate a random number and
        # assign it to target
        target = random.randint(LOWER_BOUND, UPPER_BOUND)

        # Display a welcome message
        print("\nI've chosen a random number between ", \
              LOWER_BOUND, " and ", UPPER_BOUND,\
              ".\nTry and guess it!\nIf you're within plus or "+\
              "minus ", RANGE, " I'll let you know.\nIf you "+\
              "guess the number, I'll tell you a secret!", sep='')

        # Ask player to guess the number,
        # assign guess to guess, initialize count
        guess, count = first_guess()

        # Make sure player hasn't won
        while not_winner(guess, target):
            # Make sure guess is between
            # LOWER_BOUND and
            # UPPER_BOUND, inclusive
            if valid_guess(guess):
                # make sure guess isn't correct
                if incorrect_guess(guess, target):
                # Check if guess is within plus
                # or minus RANGE of target
                # if so display hint, get new
                # guess, and iterate count
                    if close_guess(guess, target):
                        warmer(guess, target)
                        guess = retry()
                        count = tries(count)
                    # If guess isn't close display
                    # high or low, get new guess,
                    # and iterate count
                    else:
                        hi_low(guess, target)
                        guess = retry()
                        count = tries(count)
            # if guess isn't between UPPER_BOUND
            # and LOWER_BOUND, display
            # an error and get new guess
            else:
                invalid(guess)
                guess = retry()
        # display congrats and see if
        # player wants to go again
        yahoo(target, count)
        again = another_go()
    # say bye
    bye()

# check if again is True
def play_again(again):
    if again == 'y' or again == 'yes':
        status = True
    elif again == 'Y' or again == 'Yes' or again == 'YES':
        status = True
    else:
        status = False
    return status

# ask for a number and assign it to
# guess, then return guess and count
def first_guess():
    guess = int(input("\nWhat's your first guess? "))
    count = 1
    return guess, count

# check guess against target
def not_winner(guess, target):
    if guess != target:
        status = True
    else:
        status = False
    return status

# make sure guess is valid
def valid_guess(guess):
    if guess >= LOWER_BOUND and guess <= UPPER_BOUND:
        status = True
    else:
        status = False
    return status

# check if guess is incorrect
def incorrect_guess(guess, target):
    if guess != target:
        status = True
    else:
        status = False
    return status

# check if guess is close
def close_guess(guess, target):
    status = False
    for number in range (0 - RANGE, RANGE + 1):
        if guess  == target + number:
            status = True
    return status

# display how close
def warmer(guess, target):
    if guess > target:
        print('\nGetting warm but still High!\n')
    else:
        print('\nGetting warm but still Low!\n')

# get a new guess
def retry():
    guess = int(input("What's your next guess? "))
    return guess

# iterate count
def tries(count):
    count += 1
    return count

# display if guess is high or low
def hi_low(guess, target):
    if guess > target:
        print('\nToo High!\n')
    else:
        print('\nToo Low!\n')

# display invalid guess message
def invalid(guess):
    print('\nYou entered: ', guess, ', but I asked '+\
          'for a number between ', LOWER_BOUND,\
          ' and ', UPPER_BOUND, ".\n(I'll just pretend"+\
          ' this never happened.)\n', sep='')

# display a congrats that
# includes number of valid tries
def yahoo(target, count):
    print('\nYou guessed the answer! It was ',\
        target, '!\n\nThe secret is...it only '+\
        'took you ', count, ' tries :)\n(I only '+\
        'counted valid guesses, of course.)\n', sep='')

# ask if player wants to play again
# and return again
def another_go():
    again = input('Do you want to play again? ')
    return again

# say bye
def bye():
    print('\nThanks for playing! Bye-bye.\n')

# call main
main()
