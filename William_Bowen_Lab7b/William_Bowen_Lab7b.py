# This program takes LOOP students average grades
# and writes them to FILE. It then reads those
# records back from FILE.

# set global variables
FILE = 'grades.txt'
LOOP = 12

def main():
    # Open FILE to write
    averages = open(FILE, 'w')
    # Start asking for grades
    for count in range(LOOP):
        # A greeting and explanation for the user
        print('\nHello, student #', count+1, '! ' + \
                "It's time to enter your name and average grade.\n", sep='')
        # Get name
        name = input("What's your name?\n\n")
        # Use while loop to prevent a student not
        # entering anything for their name
        while name == '':
                print('\nI need more than that, student #', count+1, "!\n", sep='')
        # Get a grade
        print("\nWhat's your average grade?")
        # Initialize grade
        grade = -1
        # While loop prevents invalid grade input
        while grade not in range(0, 101):
            # use try/except to handle ValueErrors
            try:
                grade = int(input('\n(Please enter an integer between' + \
                                            ' 1 and 100.)\n\n'))
            except ValueError:
                print("\nError: that's not an integer!")
        # Copy the input to FILE
        averages.write(name + '\n')
        averages.write(str(grade) + '\n')
        # Tell user it's written to file
        print('\nI wrote your name and grade to ', FILE, '.', sep='')
    # Close FILE
    averages.close()
    # Reopen FILE to read
    # using try/except to handle IOErrors
    try:
        averages = open(FILE, 'r')
        # Explain what we are printing
        print('\nHere are the average grades for all twelve students:\n')
        # Print contents of FILE
        # Doing it with a loop plus line by
        # line makes it more readable
        for count in range(0, LOOP):
            print(averages.readline().rstrip('\n'))
            print(averages.readline())
        # Close FILE
        averages.close()
    except IOError:
        print("I can't find the file I just wrote!")

# Call main
main ()
