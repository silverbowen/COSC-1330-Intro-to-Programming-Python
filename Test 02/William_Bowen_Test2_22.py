# this program creates a file, writes numbers 1-10 to it,
# then calculates the total and displays everything
# it then adds 11-20 to the file, deletes 16-18 using a temp file
# and changes 10 to 50

# create global variable
FILE = 'numbers.txt'
TEMP = 'temp.txt'

# define main
def main():
    # part 1
    # create and open file
    file = open(FILE, 'w')
    # write 1 - 10 using for loop
    for count in range (10):
        file.write(str(count+1) + '\n')
    # verify all numbers written to file
    print('\n\nValues 1 through 10 have been written to numbers.txt\n\n') 
    # close file
    file.close()

    # part 2
    # reopen file to read numbers
    file = open(FILE, 'r')
    # initiate total
    total = 0
    # read and accumulate 1 - 10
    for count in range (10):
        # assign number to each line as it's read
        number = int(file.readline().rstrip('\n'))
        # print that number
        print('Readline', count+1, 'is', number, '\n')
        # add that number to the running total
        total = number + total
    # print the final total
    print('\nTotal is', total, '\n\n')
    # close the file
    file.close()

    # part 3
    # open the file in append mode
    file = open(FILE, 'a')
    # append 11-20 using for loop
    for count in range (11, 21):
        file.write(str(count) + '\n')
        # display verification that number was written to file
        print(count, 'was written to number.txt\n')
    # verify all new numbers were written to file
    print('\nValues 11 through 20 have been appended to numbers.txt\n\n')
    # close file
    file.close()

    # part 4
    # open temp.txt file
    tempfile = open(TEMP, 'w')
    # open FILE in read mode
    file = open(FILE, 'r')
    # write entries to temp, leaving out 16-18
    for count in range (20):
        # assign each line to number as it's read
        number = int(file.readline().rstrip('\n'))
        # write to tempfile if it isn't 16-18
        if number not in (16, 17, 18):
            tempfile.write(str(number) + '\n')
            # display verification that number was written to tempfile
            print(number, 'was read from number.txt and written to temp.txt\n')
    # close file
    file.close()
    # close tempfile
    tempfile.close()
    # reopen file in writemode, erasing it
    file = open(FILE, 'w')
    # reopen tempfile in read mode
    tempfile = open(TEMP, 'r')
    # write contents of tempfile to file
    file.write(tempfile.read())
    # display verification
    print('\nThe contents of temp.txt were used to overwrite numbers.txt\n\n')
    # close tempfile
    tempfile.close()
    # close file
    file.close()

    # part 5
    # open temp.txt file
    tempfile = open(TEMP, 'w')
    # open FILE in read mode
    file = open(FILE, 'r')
    # write entries to temp, changing 10 to 50
    for count in range (17):
        # assign each line to number as it's read
        number = int(file.readline().rstrip('\n'))
        # if number isn't 10
        if number != 10:
            # write to tempfile
            tempfile.write(str(number) + '\n')
            # display verification that number was written to tempfile
            print(number, 'was read from number.txt and written to temp.txt\n')
        # if number is 10
        else:
            # change number to 50
            number = 50
            # write to tempfile
            tempfile.write(str(number) + '\n')
            # display verification that number was written to tempfile
            print('\n', number, ' was read from number.txt, changed to 50, and written to temp.txt\n\n', sep='')   
    # close file
    file.close()
    # close tempfile
    tempfile.close()
    # reopen file in writemode, erasing it
    file = open(FILE, 'w')
    # reopen tempfile in read mode
    tempfile = open(TEMP, 'r')
    # write contents of tempfile to file
    file.write(tempfile.read())
    # display verification
    print('\nThe contents of temp.txt were used to overwrite numbers.txt\n\n')
    # close tempfile
    tempfile.close()
    # close file
    file.close()
    # final verification
    print('All files closed\n')

# call main
main()
