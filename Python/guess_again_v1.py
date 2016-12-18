import random

# Get the user's guess
# Params: None
# Returns: Integer
#
def get_guess():

    # Get initial guess
    guess = raw_input('Enter your guess: ')

    # Assume it's not valid, until it's proven otherwise
    valid = False

    while valid != True:

        try:
            # Try and convert this number to an integer
            # If it fails, the exception will occur
            guess = int(guess)
        except Exception:
            # Exception was thrown when trying to convert to number,
            # Report the issue and ask again
            print('Invalid input; please enter a whole number.')
            valid = False
            guess = get_guess()

        # If they get here, it means the number must have been valid
        # Set valid to be true to break out of the while loop
        valid = True

    return guess

# # Test get_guess
# print get_guess() # Expected: Keeps prompting until user enters a valid number

def compare(numA, numB):
    if numA < numB:
        return 'low'
    elif numA > numB:
        return 'high'

# # Test compare
# print compare(100,1)  # Expected: 'high'
# print compare(1,100)  # Expected: 'low'
# print compare(99,100) # Expected: 'low'

def play(min, max):

    # Pick a secret number
    secret_number = random.randint(min, max)

    # When building your program, the following line will tell you what
    # the secret_number is; this will make it easier to test the game.
    # When done, remove or comment-out this line.
    print('TEMPORARY DEBUGGING HELPER -> The secret number is: ' + str(secret_number))

    # Print message at the start the game
    print('\nI\'m thinking of a number between ' + str(min) + ' and ' + str(max) + '; what do you think it is?')

    # Get the player's initial guess
    player_guess = get_guess()

    # Keep prompting until they get it correct
    # For every failed attempt, print 'Too x. Guess again.' where x is either 'high' or 'low'
    tries = 1
    while player_guess != secret_number:
        print('Too ' + compare(player_guess, secret_number) + '.')
        tries = tries + 1
        player_guess = get_guess()

    # Print conclusion
    print('You got it! The number was ' + str(secret_number) + '. It took you ' + str(tries) + ' guesses!!\n')

# Run the game
play(1, 50)
