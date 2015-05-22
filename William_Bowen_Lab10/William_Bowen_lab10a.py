## This program is a bulk entry tool. It uses the Student class, which holds: name, student ID #,
## GPA, expected grade for course, and full/part-time (as name, ID, GPA, grade,  and time). It
## asks for input to create size instances of the student object, then pickles them in a file chosen
## by the user. The list_tool module does most of the work.

import pickle
import student
import list_tool

# define main
def main():

    # done flag and while loop ensures valid input
    done = False
    while done == False:
        # try loop handles exceptions and gets valid input
        try:
            size = int(input("I'm ready to make a list for you. How many students are we adding? "))
            if size > 0:
                done = True
            else:
                print('\nI need an integer greater than 0.\n')
        except:
            print('\nI need an integer greater than 0.\n')
        
    # call make_list
    object_list = list_tool.make_list(size)

    # get name of file to pickle the list to
    use_file =  str(input("\nI'm ready to pickle your list. What would you like to name the file? "))

    # ensure file ending conventions are followed
    if use_file.endswith('.dat') == False:
        use_file += '.dat'
        print("\nI've appended .dat to your file name.\n")
                  
    # call list_brine
    list_tool.list_brine(use_file, object_list)

    # confirmation message
    print("I've pickled your list in", use_file, "\n")

    # help message
    print("I'll pull that data back up and let you see it just to double-check.\n")

    # call get_file
    list_tool.get_file(use_file)


# call main
main()
    
