# This program takes in the numeric grades
# of students in COSC 1336. It accepts any number
# of inputs, and stops taking input when a
# student enters -1. It issues a letter grade
# for the student and a comment, then prints
# the class average at the end.

def main():
        # Initialize running total at 0.
        # total will accumulate the total
        # of all grades entered
        total = 0
        # initialize number at 0
        # number will handle student count
        # as well as total number of grades
        number = 0
        # initialize value at 0
        # This must be set here so
        # the while loop doesn't produce an error
        value = 0
        # Inform user of the program's purpose
        # and how to use it
        print("Hello! It's time to enter your grade.\n" + \
                "I'll give comments, and then give a class " + \
                "average at the end.\n" + \
                "Please enter your grade.\n" + \
                "After the last student inputs their grade, " + \
                "enter -1 to quit and get the class average.\n")
        # get input from user and check for sentinel
        while value != -1:
            print('Enter -1 to quit and get the class average.\n' + \
                    'Otherwise, enter the grade for student #', \
                    number + 1, ': ', sep='', end='')
            value = float(input(''))
            print('')
            # if sentinel = false, print message
            if value != -1:
                Message(value, number)
                # value and number iterate if score
                # entered was valid
                if value >= 0 and value <= 100:
                    total  = total + value
                    number += 1
        # print total grades and class total
        # or print message if no grades entered
        Average(total, number)

# Message gives the user their letter grade,
# and a comment on it. It also checks
# and reasks if the grade is negative, but
# not -1, or over 100
def Message(value, number):
    if value != -1 and value < 0:
        print("You can't really have gotten a negative score, right?")
        print("Since my instructions don't cover what to do in this case, " + \
                "I'll just ask again:\n")
    elif value < 60:
        print('You made an F! Obviously you did not study!\n')
    elif value < 70:
        print('You made a D! Lousy, but at least you passed!\n')
    elif value < 80:
        print("You made a C! That's totally average!\n")
    elif value < 90:
        print('You made a B! Hurray! Good job!\n')
    elif value <= 100:
        print('You made an A! You must have studied hard! Excellent work!\n')
    else:
        print("Maybe you did some extra credit, but I wasn't told anything about that.")
        print("Since my instructions don't cover what to do in this case, " + \
                "I'll just ask again:\n")

# Average either prints total number of grades and a numeric
# average, or prints a message saying there is no average.
def Average(total, number):
    if number > 0:
        print('There were a total of', number, 'grades entered.\n')
        print('The class average is:', format(total/number, '.2f'), '\n')
    else:
        print('Since you have no class, there is no average!\n')
        
main()
