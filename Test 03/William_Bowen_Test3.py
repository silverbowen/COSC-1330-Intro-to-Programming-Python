## This program reads the list of names from employees_names.tx. It takes input for each employees
## hours worked, which it stores in the employee_names.txt file. It rereads that data from the file
## and stores it in a list. It then uses those values to display gross pay (hourly rate is 12) and
## overtime (18).

# global used for working file to save typing and allow easy changes
FILE = ('employee_names.txt')

# read_file converts FILE into a list by way of split
def read_file(infile):

    # open FILE
    file = open(FILE, 'r')

    # convert file to string
    string = file.read()

    #remove last newline so we don't get an extra entry in our list
    string = string.rstrip('\n')

    # make list w/ split
    use_list = string.split('\n')


    # close file
    file.close()

    # return list
    return use_list

# print list prints a list in a column format
def print_list(use_list):

    # initialize index
    index = 0

    # while loop iterates through use_list indices using the length of use_list
    while index in range (len(use_list)):
        print(use_list[index])
        index += 1
        
# get_new asks for input and then appends that input to create a new list
def get_new(use_list):

    # initialize new_list
    new_list = []

    # initialize index
    index = 0

    # while loop iterates through the new_list indices using the length of the use_list
    while index in range (len(use_list)):

        # try loop to handle exceptions
        try:

            # get input
            entry = float(input('\nPlease enter hours worked for '+(use_list[index])+': '))

            # ensure input is valid
            if entry >= 0:

                # append to new_list
                new_list.append(entry)

                # iterate index
                index += 1

            # for invalid input
            else:
                print('\nTime only moves in one direction, McFly. Hours must be >= 0!')

        # for exceptions
        except ValueError:
            print('\nPlease enter a number!')

    # return new_list
    return new_list

# write_file writes 2 lists into FILE, interweaving them
def write_file(use_list, use_list2):

    # open file
    file = open(FILE, 'w')

    # intialize index
    index = 0

    # iterate through index of use_list
    while index in range (len(use_list)):

        # write use_list element, then use_list2 element
        file.write(use_list[index]+'\n'+str(use_list2[index])+'\n')

        # iterate index
        index += 1

    # close file
    file.close()
    
# gross calculates the gross pay
def gross(use_list):

    # initialize index
    index = 0

    # while loop iterates through use_list index in multiples of 2
    while index in range (len(use_list)):

        # set variables to save processing
        hrs_worked = float(use_list[index+1])
        overtime = hrs_worked - 40
        
        # check for overtime and calculate accordingly
        if overtime > 0:
            gross = 480 + (16 * overtime)
        else:
            gross = 12 * hrs_worked

        # display formatted results
        print('The gross pay for', use_list[index], 'is', format(gross, '.2f'), '\n')


        #iterate index
        index += 2

# revert_file is a help function used to reset FILE to the given file. Very useful if testing
# has wreaked havoc on the initial file. Also good because our customer might want to use
# this program again, and it doesn't work very well on a file that's already been added to.
def revert_file(use_list):

    # open file
    file = open(FILE, 'w')

    # initialize index
    index = 0

    # while loop iterates through Use_list index
    while index in range (len(use_list)):

        # write the element to the file
        file.write(use_list[index]+'\n')

        # iterate index
        index += 1

    # close the file
    file.close()

    
# define main
def main():

    # call read_file, read initial FILE, getting a list in return
    employees = read_file(FILE)

    # call print_list, display contents of the list
    print('Here are the employees in ', FILE, ':\n')
    print_list(employees)   

    # call get_new, get input for hours worked, creating a second list
    hours = get_new(employees)
       
    # call write_file, write both lists to FILE, interweaving them so data stay organized
    write_file(employees, hours)
    print('\nI wrote those values to ', FILE, '.\n', sep='')

    # call read_file, read file into a 3rd list
    emp_n_hours = read_file(FILE)

    # display contents of the 3rd list, which reflects the current FILE contents
    print('Here are the employees and their hours worked in ', FILE, ':\n', sep='')
    print_list(emp_n_hours)

    # call gross, calculate/display pay using 3rd list
    print('\nHere is the gross pay for each employee:\n')
    gross(emp_n_hours)

    # and finally, ask if user wants to revert, writing the 1st list to FILE and undoing all our 'progress'
    revert = input('Would you like me to revert '+(FILE)+' to the same as when we started? (helpful for testing this program again): ')

    # process input
    if revert.lower() in ('y', 'yes'):


        # if yes, call revert_file
        revert_file(employees)

        # help message
        print('\nOkay, I reverted it.')

    # warn foolish users
    else:
        print('\nOkay. Please remember to make a fresh copy of', FILE, 'before you run this program again, then.\n')

# call main
main()
