## This program asks the user to input a date in numeric format e.g. mm/dd/yy.
## If the month entered is larger than 12 or smaller than 1 it issues an error message
## and asks for input again. It likewise validates the date and year. Year must not be
## less than 2013 or larger than 2013 (as per assignment instructions). In addition, the
##year must only be two digits long. Finally, it outputs the string in long date format,
##ie -- 06/01/13 == June 1, 2013.

# YEAR is my only global variable. If I ever want to come back and allow a broader range
# of inputs for year, this will make it easier to do so.

YEAR = [13]


# define invalid
def invalid():
    # saves a lot of copy pasta to make this a function
    print('The date you entered was invalid or incorrectly formatted! Integers and "/" only, please.\n')

# define get_date
def get_date():
    # set flag
    valid = False
    # use while loop to validate input and re-ask if needed
    while valid != True:
        # use try for error/exception handling
        try:
            # get input
            date_string = input('Please input a date (from 2013 only) in numeric format (e.g. mm/dd/yy): ')
            print('')
            # ensure the string is at least the correct length
            if len(date_string) == 8:
                valid = True
            # if not = invalid!
            else:
                invalid()
                print('Your input was either too long or too short! Months/days less than 10 should have a leading 0!\n')
        # any exceptions also throw invalid() and keep the input loop going
        except:
            Invalid()
    # return date_string
    return date_string
    
# define validate(date_string)
def validate(date_string):
    # set flag again
    valid = False
    # try loop uses error catching for validation (correct number of / chars, formatting, etc.)
    try:
        # convert input string into list for easier processing (faster and simpler than find/slice methods
        # of removing the '/' characters).
        date_list = date_string.split('/')
        # divide elements into usable variables
        # index assignment throws errors if not enough indexes
        mon = date_list[0]
        day = date_list[1]
        year = date_list[2]
        # check that each variable is exactly 2 digits, if not, invalid!
        if len(mon) != 2 or len(day) != 2 or len(year) != 2:
            Invalid()
        # move on down the checking chain
        else:
            # int() conversion throws errors if the elements aren't numeric
            mon = int(mon)
            day = int(day)
            year = int(year)
            #check that the correct digits are in the correct places 
            if year not in (YEAR):
                invalid()
                print("The year must be 2013 ('13')!\n")
            elif mon not in range (1, 13):
                invalid()
                print('The month must be from 01 to 12!\n')
            elif day not in range (1, 32):
                invalid()
                print('The day must be from 01 to 31!\n')
            # here we check that the number entered for day is actually possible for that
            # particular month. Since 2013 did not have a leap day, everything is accounted for.
            elif mon == 2 and day not in range (1, 29):
                invalid()
                # February only has 28 days
                print('That month only has 28 days!\n')
            elif mon in (4, 6, 9, 11) and day not in range (1, 31):
                invalid()
                # and April, June, September, and November only have 30
                print('That month only has 30 days!\n')
            # the rest all have 31, so: accept and return input
            else:
                valid = True
    # this exception catches any errors thrown by any of the operations above
    except:
        invalid()
    # let main know if the string is valid
    return valid

# define show_date(date_string)
def show_date(date_string):
    # first we make a list of all the months
    mon_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    # then we print out our results, using sections of the original string as indexes for the month list, etc.
    print('In long form that date is: ', mon_list[int(date_string[0:2])-1], ' ', int(date_string[3:5]), ', 20', int(date_string[6:9]), '\n',sep='')
                   
# define main
def main():
    
    #call get_date() to get intitial input and do some validation
    date_string = get_date()
                      
    # validate input thoroughly if it comes back invalid, call get_date() again
    while validate(date_string) != True:
        date_string = get_date()

    # display result using show_date()
    show_date(date_string)

# call main
main()
    
