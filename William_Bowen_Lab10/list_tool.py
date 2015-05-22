# This module consists of tools for making, altering, and pickling lists of objects. It uses
# the Student Class and the pickle module.

# include functions:
# make_list - accepts size argument - returns a list of student object
# add_to_list - accepts a use_list argument - adds a student object and returns the list
# list_brine - accepts a use_file and list_to_brine argument - pickles the list in the file
# list_debrine - accepts a use_file argument - depickles the file into a list
# get_file - accepts a use_file argument - depickles and displays entire list of objects
# list_names - accepts a use_list argument - displays names only

import student
import pickle

# make_list accepts a size argument and creates a list of size students
def make_list(size):
    
    # create an empty list
    new_list = []

    # get input for five student
    if size == 1:
        print('Enter the attributes for the student.\n')
    else:
        print('Enter the attributes for', size, 'students.\n')
    
    # use a while loop for each instance
    count = 0
    while count in range (size):

        # use try loop to get valid input
        try:

            # get name
            name = str(input('Enter the name of student #'+(str(count+1))+': '))
            # verify valid input
            while name.replace(' ', '').isalpha() == False:
                print('\nPlease enter a valid name containing only letters and spaces.\n')
                name = str(input('Enter the name of student #'+(str(count+1))+': '))

            # get ID    
            ID = str(input('\nEnter the ID number of student #'+(str(count+1))+': '))
            # verify valid input
            while ID.isdigit() == False:
                print('\nPlease enter a valid ID containing only numbers.\n')
                ID = str(input('Enter the ID number of student #'+(str(count+1))+': '))

            # get GPA
            GPA = float(input('\nEnter the GPA of student #'+(str(count+1))+': '))
            # verify valid input
            while int(GPA) not in range (0, 101):
                print('\nPlease enter a valid GPA containing only digits. It must be between 0 and 100, inclusive.\n')
                GPA = float(input('Enter the GPA of student #'+(str(count+1))+': '))

            # get grade           
            grade = float(input('\nEnter the expected grade for student #'+(str(count+1))+': '))
            # verify valid input
            while int(grade) not in range (0, 101):
                print('\nPlease enter a valid expected grade between 0 and 100, inclusive.\n')
                grade = float(input('Enter the expected grade for student #'+(str(count+1))+': '))

            # get time
            time = str(input("\nType 'full' or 'part' to enter full-time or part-time status for student #"+(str(count+1))+": "))
            # verify valid input
            while time.lower() not in ('full', 'part'):
                print('\nPlease enter either "full" or "part" for full-time or part-time.\n')
                time = str(input("Type 'full' or 'part' to enter full-time or part-time status for student #"+(str(count+1))+": "))

            # spacer
            print ('')

            #  create a new object using Student   
            entry = student.Student(name, ID, GPA, grade, time)

            # add new object to the list
            new_list.append(entry)

            # iterate loop
            count += 1

        # exception triggers redux
        except:
            print("\nOopsy, your input wasn't valid. Let's try this from the top.\n")
        
    # return the list
    return new_list

# add_to_list accepts a use_list argument and adds to a list, then returns the list
def add_to_list(use_list):
    
    # initialize done
    done = False

    # use a while loop for each instance
    while done== False:

        # use try loop to get valid input
        try:

            # get name
            name = str(input('Enter the name of student #'+(str(len(use_list)+1))+': '))
            # verify valid input
            while name.replace(' ', '').isalpha() == False:
                print('\nPlease enter a valid name containing only letters and spaces.\n')
                name = str(input('Enter the name of student #'+(str(len(use_list)+1))+': '))
                
            # get ID    
            ID = str(input('\nEnter the ID number of student #'+(str(len(use_list)+1))+': '))
            # verify valid input
            while ID.isdigit() == False:
                print('\nPlease enter a valid ID containing only numbers.\n')
                ID = str(input('Enter the ID number of student #'+(str(len(use_list)+1))+': '))

            # get GPA
            GPA = float(input('\nEnter the GPA of student #'+(str(len(use_list)+1))+': '))
            # verify valid input
            while int(GPA) not in range (0, 101):
                print('\nPlease enter a valid GPA containing only digits. It must be between 0 and 100, inclusive.\n')
                GPA = float(input('Enter the GPA of student #'+(str(len(use_list)+1))+': '))

            # get grade           
            grade = float(input('\nEnter the expected grade for student #'+(str(len(use_list)+1))+': '))
            # verify valid input
            while int(grade) not in range (0, 101):
                print('\nPlease enter a valid expected grade between 0 and 100.\n')
                grade = float(input('Enter the expected grade for student #'+(str(len(use_list)+1))+': '))

            # get time
            time = str(input("\nType 'full' or 'part' to enter full-time or part-time status for student #"+(str(len(use_list)+1))+": "))
            # verify valid input
            while time.lower() not in ('full', 'part'):
                print('\nPlease enter either "full" or "part" for full-time or part-time.\n')
                time = str(input("Type 'full' or 'part' to enter full-time or part-time status for student #"+(str(len(use_list)+1))+": "))

            # spacer
            print ('')

            #  create a new object using Student   
            entry = student.Student(name, ID, GPA, grade, time)

            # add new object to the list
            use_list.append(entry)

            # end loop
            done = True

        # exception triggers redux
        except:
            print("\nOopsy, your input wasn't valid. Let's try this from the top.\n")
        
    # return the list
    return use_list

# list_brine accepts a list and file argument and pickles the list
def list_brine(use_file, list_to_brine):

    # initialize index, done
    index = 0
    done = False

    # open file to write to
    outfile = open(use_file, 'wb')
    
    while done == False:
        # while/try loop pickles each entry in list_to_brine
        try:
           pickle.dump(list_to_brine[index], outfile)

           # iterate index
           index += 1

        except IndexError:
            done = True
           
    # close file to preserve data
    outfile.close()

# list_debrine accepts file argument and depickles it as a list, which it returns
def list_debrine(use_file):

    # initialize index, done
    index = 0
    done = False

    # open file to read from
    infile = open(use_file, 'rb')
    
    # create empty list
    list_debrined = []
    
    # while/try loop reads file until EOFError
    while done == False:

        # try loop depickles each entry in use_file
        try:
           entry = pickle.load(infile)

           # append to list
           list_debrined.append(entry)

           # iterate index
           index += 1

        except EOFError:
            done = True
           
    # close file to preserve data
    infile.close()

    # return the fruits of our depickling
    return list_debrined

# get_file accepts a use_file argument and reports on the data pickled therein    
def get_file(use_file):

    # initialize done
    done = False

    # initialize index, for automated counting
    index = 0

    # help message
    print('Here is the data pickled in ', use_file,':\n', sep='')
        
    # try loop ensures error handling
    try:

        # open the file
        infile = open(use_file, 'rb')

        # while/try loop reads to end of file
        while done == False:

            # load the object
            student = pickle.load(infile)

            # print attributes
            print ('Student #', index+1, ':\n', 'Name: ', student.get_name(), '\n', 'ID: ', student.get_ID(), '\n', \
                  'GPA: ', student.get_GPA(), '\n', 'Expected grade: ', student.get_grade(), '\n', \
                  'Full/part-time: ', student.get_time(), '\n', sep='')

            # iterate index
            index += 1

    # exception at EOFError
    except EOFError:

        # close the file
        infile.close()

        # end the loop
        done = True

    # exception if no file found
    except IOError:
        print(use_file, 'not found.')
        done = True

# list_names accepts a use_list argument and reports on the names therein    
def list_names(use_list):

    # initialize done
    done = False

    # initialize index
    index = 0

    # help message
    print('Here are the names of the students in the list:\n')

    # while/try loop reads to end of file
    while done == False:

        try:
            # load the object
            student = use_list[index]

            # print the names
            print ('Student #', index+1, ': ', student.get_name(), sep='')

            # iterate index
            index += 1

        # exception at IndexError
        except IndexError:
            print('')

            # end the loop
            done = True
