## This program imports the Student class, which holds: name, student ID #,
## GPA, expected grade for course, and full/part-time (as name, ID, GPA, grade,
## and time). It also imports the pickle and list_tool modules.
## It uses a menu to allow the following tasks:
## 1. Look up and print the student GPA
## 2. Add a new student to the class
## 3. Change the GPA of a student
## 4. Change the expected grade of a student
## 5. Print the data of all the students in a tabular format
## 6. Quit the program
## (Notice that there is no way to change student name, ID, or time attributes once a student
## has been created, nor is there a way to delete a student.)

import student
import pickle
import list_tool

# FILE is the global variable used for the file created with William_Bowen_lab10a.py.

FILE = 'APT.dat'

# menu returns one of the 6 menu options
def menu(FILE):

    # while/try loop ensures valid input
    loop = False
    while loop == False:
        try:
            # show/get choices
            choice = int(input('Please choose a number from the following options:\n\n'+\
                                '1. Look up and print the student GPA\n'+\
                                '2. Add a new student to the class\n'+\
                                '3. Change the GPA of a student\n'+\
                                '4. Change the expected grade of a student\n'+\
                                '5. Print the data of all the students in a tabular format\n'+\
                                '6. Quit the program\n\nChoice: '))
        

            print('')
            # if input is valid set loop to true and return the choice
            if choice in range (1, 7):
                loop = True
                return choice
            else:
                print('Please enter a number between 1 and 6, inclusive.\n')
        # this exception is for choice
        except:
            print('\nOopsy. Please just enter a valid number.\n')
            
# choice_1 displays a student GPA
def choice_1(stu_list):
                  
    # initialize loop
    loop = False

    # while loop makes sure we get valid input
    while loop == False:

        # try handles exceptions
        try:

            # get input
            stu_num = int(input("Which student's GPA would you like to see? Enter their index number "+\
                                "(from 1 to "+str(len(stu_list))+"): "))-1

           # check for valid input
            if stu_num in range (len(stu_list)):
                # display GPA
                student = stu_list[stu_num]
                print("\nThat student's GPA is:", student.get_GPA(), '\n')
                loop = True

            # for invalid input
            else:
                print("\nPlease enter a valid student index number (from 1 to ", str(len(stu_list)), "): \n", sep='')                 

        # for errors
        except:
            print("\nPlease enter a valid student index number (from 1 to ", str(len(stu_list)), "): \n", sep='')
        
# choice_2 adds a student to the end of the list
def choice_2(stu_list):

    # call add_to_list
    stu_list = list_tool.add_to_list(stu_list)

    # help message
    print("I've added that student to the list.\n")

# choice_3 changes a student's GPA
def choice_3(stu_list):

    # initialize loop
    loop = False

    # while loop makes sure we get valid input
    while loop == False:

        # try handles errors
        try:

            # get input
            stu_num = int(input("Which student's GPA would you like to change? Enter their index number "+\
                                "(from 1 to "+str(len(stu_list))+"): "))-1

            # check for valid input
            if stu_num in range (len(stu_list)):
                loop = True

            # for invalid input
            else:
                print("\nPlease enter a valid student index number (from 1 to ", str(len(stu_list)), "): \n", sep='')                 

        # for errors
        except:
            print("\nPlease enter a valid student index number (from 1 to ", str(len(stu_list)), "): \n", sep='')

    print('')

    # reup loop
    loop = False
    while loop == False:
                               
        # try handles errors
        try:

            # get new GPA
            new_GPA = float(input('Enter the new GPA: '))
                                      
            # verify valid input
            if int(new_GPA) in range (0, 101):
    
                # change GPA
                student = stu_list[stu_num]
                student.set_GPA(new_GPA)

                # confirm changes
                print('\nHere is the new entry:\n\n', 'Name: ', student.get_name(), '\n', 'ID: ', student.get_ID(), '\n', \
                      'GPA: ', student.get_GPA(), '\n', 'Expected grade: ', student.get_grade(), '\n', \
                      'Full/part-time: ', student.get_time(), '\n', sep='')

                # end loop
                loop = True

            # for invalid input
            else:
                print('\nPlease enter a valid GPA containing only digits. It must be between 0 and 100, inclusive.\n')

        # except for errors
        except:
            print('\nPlease enter a valid GPA containing only digits. It must be between 0 and 100, inclusive.\n')

# choice_4 changes a student's expected grade
def choice_4(stu_list):

    # initialize loop
    loop = False

    # while loop makes sure we get valid input
    while loop == False:

        # try handles errors
        try:

            # get input
            stu_num = int(input("Which student's grade would you like to change? Enter their index number "+\
                                "(from 1 to "+str(len(stu_list))+"): "))-1

            # check for valid input
            if stu_num in range (len(stu_list)):
                loop = True

            # for invalid input
            else:
                print("\nPlease enter a valid student index number (from 1 to ", str(len(stu_list)), "): \n", sep='')                 

        # for errors
        except:
            print("\nPlease enter a valid student index number (from 1 to ", str(len(stu_list)), "): \n", sep='')

    print('')

    # reup loop
    loop = False
    while loop == False:
                               
        # try handles errors
        try:

            # get new GPA
            new_grade = float(input('Enter the new expected grade: '))
                                      
            # verify valid input
            if int(new_grade) in range (0, 101):
    
                # change GPA
                student = stu_list[stu_num]
                student.set_grade(new_grade)

                # confirm changes
                print('\nHere is the new entry:\n\n', 'Name: ', student.get_name(), '\n', 'ID: ', student.get_ID(), '\n', \
                      'GPA: ', student.get_GPA(), '\n', 'Expected grade: ', student.get_grade(), '\n', \
                      'Full/part-time: ', student.get_time(), '\n', sep='')

                # end loop
                loop = True

            # for invalid input
            else:
                print('\nPlease enter a valid grade containing only digits. It must be between 0 and 100, inclusive.\n')

        # except for errors
        except:
            print('\nPlease enter a valid grade containing only digits. It must be between 0 and 100, inclusive.\n')

# choice_5 prints the list
def choice_5(stu_list):
                                  
    # initialize done
    done = False

    # initialize index, for automated counting
    index = 0

    # help message
    print('Here is the list:\n')
        
    # while/try loop reads to end of file
    while done == False:

        # try loop ensures error handling
        try:

            # set current student
            student = stu_list[index]

            # print attributes
            print ('Student #', index+1, ':\n', 'Name: ', student.get_name(), '\n', 'ID: ', student.get_ID(), '\n', \
                  'GPA: ', student.get_GPA(), '\n', 'Expected grade: ', student.get_grade(), '\n', \
                  'Full/part-time: ', student.get_time(), '\n', sep='')

            # iterate index
            index += 1

        # exception at IndexError ends loop
        except IndexError:
            done = True
        
# define main
def main():

    # get the list we will be working with
    stu_list = list_tool.list_debrine(FILE)

    # initialize done
    done = False
    print('')

    # show file name
    print('We are working with the student object list serialized in ', FILE, '.\n', sep='')

    # while loop keeps it going
    while done == False:

        # call list_names
        list_tool.list_names(stu_list)

        # get new choice from menu
        choice = menu(FILE)
        
        # call appropriate function
        if choice == 1:
            choice_1(stu_list)

        elif choice == 2:
            choice_2(stu_list)
            
        elif choice == 3:
            choice_3(stu_list)

        elif choice == 4:
            choice_4(stu_list)

        elif choice == 5:
            choice_5(stu_list)

        else:
            done = True

    # rebrine the list for safekeeping
    list_tool.list_brine(FILE, stu_list)

    # help message
    print("I've pickled the list as ", FILE, '. Bye bye!\n', sep ='')

# call main
main()
    
