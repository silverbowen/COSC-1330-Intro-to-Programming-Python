# This program asks users to enter five test scores.
# It then displays a letter grade for each score
# and the average of the scores.

# Main calls get_grades, calc_average and determine_grade
def main():
    # ask user for grades
    print('\nPlease enter five grades.\n(Integers from 1 to 100, please.)\n')
    # initialize total
    total = 0
    for count in range(5):
        # send count to get_grade and get back grade
        grade = get_grade(count)
        # send grade to determine_grade and get back letter
        letter = determine_grade(grade)
        # display letter grade
        print('\nYour letter grade for grade #', (count+1), ' is: ', letter, '\n', sep='')
        # send total and grade to average and get back total and average
        total, average = calc_average(total, grade)
        # iterate count
        count += 1
    # display the average
    print('Your average score is:', average, '\n')

def get_grade(count):    
    # initialize grade
    grade = 101
    # while loop ensures we keep asking until we get a valid grade
    while grade not in range(0, 101):
        # try/except loop prevents ValueError
        try:
            # get grade
            grade = int(input('Please enter grade #'+str(count+1)+': '))
            # check if grade is valid
            if grade not in range(0, 101):
                print('\nI need a number from 0 to 100.\n')
        # handle exceptions
        except ValueError:
            print('\nI need an integer, please.\n')
    # return grade
    return grade

def calc_average(total, grade):
    # accumulate total
    total = total + grade
    # calculate average
    average = total/5
    # return total and average
    return total, average

def determine_grade(grade):
    # if/elif/else structure assigns letter
    if grade < 60:
        letter = 'F'
    elif grade < 70:
        letter = 'D'
    elif grade < 80:
        letter = 'C'
    elif grade < 90:
        letter = 'B'
    else:
        letter = 'A'
    # return letter
    return letter

# call main
main()
    
            
    
