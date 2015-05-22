# This program is for Professor Polanco at Austin Community College.
# It allows him to input student names into a list called students.
# It uses functions to take 12 student's names, then sorts the names alphabetically,
# then sorts them in reverse, then appends Professor Polanco's name to the end,
# then inserts my name to the beginning, then writes the list to a file,
# and displays the contents of the file as a list, then as a file, then converts the list to a Tuple.

# define main
def main():
    
    # create list
    students = create()
    print("Here is the freshly created list:\n\n", students, '\n', sep='')

    # insert names
    students = add_students(students)
    print("Here is the list with all 12 students:\n\n", students, '\n', sep='')

    # sort the list
    students = aphabetize(students)
    print("Here is the alphabetized list:\n\n", students, '\n', sep='')

    # reverse the list
    students = backwards(students)
    print("Here is the reversed list:\n\n", students, '\n', sep='')

    # append instructors name to list
    students = instructor(students)
    print("Here is the list with the instructor's name appended:\n\n", students, '\n', sep='')

    # insert my name at the top of the list
    students = mefirst(students)
    print("Here is the list with my name inserted at the beginning:\n\n", students, '\n', sep='')

    # write list to a file
    writelist(students)
    print('I created a file called students.txt. You can look at it if you want!\n')

    # display the file as list
    print("I'll display the contents of that file for you (as a list):\n")
    display()
    print('')

    # display the file as file
    print('(Fine. If you really want to see it, this is what the actual file looks like:)\n')
    display2()
    
    # make the list a Tuple
    students = maketup(students)
    print('I made the list into a Tuple so nobody can mess with it! Sweet!\n')
    print("Here is the list as a Tuple:\n\n", students, '\n', sep='')

    
# define create
def create():
    # populate w/ 12 zeros
    list_name = [0] * 12
    return list_name

# define add_students
def add_students(twelve):
    # use for loop to get input
    for n in range(12):
        twelve[n] = input('What is the name of student '+str(n+1)+'? ')
    print('')
    return twelve

# define aphabetize
def aphabetize(ordered):
    # use sort method to alphabetize
    ordered.sort()
    return ordered

# define backwards
def backwards(reordered):
    # use reverse method to reverse the order
    reordered.reverse()
    return reordered

# define instructor
def instructor(teacher):
    # use append method to add on Prof name
    teacher.append('Polanco')
    return teacher

# define mefirst
def mefirst(myname):
    # use insert method to insert my name at zeroeth index
    myname.insert(0, 'William Bowen')
    return myname

# define writelist
def writelist(writestud):
    # open file for writing
    outfile = open('names.txt', 'w')
    # use for loop to write each element of list plus newline
    for item in writestud:
        outfile.writelines(item + '\n')
    # close file for data safety
    outfile.close()

# define display
def display():
    # open file for reading
    infile = open('names.txt', 'r')
    # write elements to students list (overwriting old values, which are identical)
    students = infile.readlines()
    # close file for data safety
    infile.close()
    # initialize index
    index = 0
    # use while loop to strip newline
    while index < len(students):
        students[index] = students[index].rstrip('\n')
        index += 1
    # display list
    print(students)

# define display2 - displays names.txt how in a more file-like form
def display2():
    # open file for reading
    infile = open('names.txt', 'r')
    # rad file into string variable called studentsfile
    studentsfile = infile.read()
    # close file for data safety
    infile.close()
    # display string copied from file
    print(studentsfile)

# define maketup
def maketup(armor):
    # use tuple function to convert list to a tuple
    armor = tuple(armor)
    return armor
    
# call main
main()
