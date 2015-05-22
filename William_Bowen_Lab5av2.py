# This program uses semi-recursive loops
# to calculate conversions between
# Standard and Metric measurements

def main():
    # initializes variables and calls GetMeasure
    errorcount = 0
    miles = -1
    fahren = 1001
    gallon = -1
    lbs = -1
    inch = -1
    GetMeasure(errorcount, miles, fahren, gallon, lbs, inch)

# GetMeasure asks how many units to convert,
# then calls ErrorCheck to validate.
# When all units are valid, it prints results.
def GetMeasure(errorcount, miles, fahren, gallon, lbs, inch):
    # check whether to call ThreeStrikes
    if errorcount == 3:
        ThreeStrikes()
    else:
        # call Question for each measurement
        if miles < 0:
            Question('miles')
            miles = float(input(''))
            ErrorCheck(errorcount, 'miles', miles, miles, fahren, gallon, lbs, inch)
        elif fahren > 1000:
            Question('Fahrenheit degrees')
            fahren = float(input(''))
            ErrorCheck(errorcount, 'Fahrenheit degrees', fahren, miles, fahren, gallon, lbs, inch)
        elif gallon < 0:
            Question('gallons')
            gallon = float(input(''))
            ErrorCheck(errorcount, 'gallons', gallon, miles, fahren, gallon, lbs, inch)
        elif lbs < 0:
            Question('pounds')
            lbs = float(input(''))
            ErrorCheck(errorcount, 'pounds', lbs, miles, fahren, gallon, lbs, inch)
        elif inch < 0:
            Question('inches')
            inch = float(input(''))
            ErrorCheck(errorcount, 'inches', inch, miles, fahren, gallon, lbs, inch)

        # calculate and print answers
        else:
            Results('miles', 'kilometers', miles, miles * 1.6)
            Results('Fahrenheit degrees', 'Celsius degrees', fahren, (fahren-32) * 5/9)
            Results('gallons', 'liters', gallon, gallon * 3.9)
            Results('pounds', 'kilograms', lbs, lbs * .45)
            Results('inches', 'centimeters', inch, inch * 2.54)
            print('\n', end='')

# Question asks for input
def Question(unit):
    print('\nHow many', unit, 'would you like to convert? ', end='')

# Error prints error message for incorrect input
# allowing for a syntax difference for degrees
def Error(unit):
    if unit == 'fahrenheit degrees':
        special = 'one thousand or less'
    else:
        special = 'a nonnegative number of'
    print('\nError! You must enter', special, unit, end='')
    print('!')

# ErrorCheck validates input. If invalid, it
# iterates errorcount. Then it calls GetMeasure.
def ErrorCheck(errorcount, unit, value, miles, fahren, gallon, lbs, inch):
    if unit == 'Fahrenheit degrees'  and value > 1000:
        Error(unit)
        errorcount += 1
        GetMeasure(errorcount, miles, fahren, gallon, lbs, inch)
    elif unit !=  'fahrenheit degrees' and value < 0: 
        Error(unit)
        errorcount += 1
        GetMeasure(errorcount, miles, fahren, gallon, lbs, inch)
    else:
        errorcount = 0
        GetMeasure(errorcount, miles, fahren, gallon, lbs, inch)

# Results prints the calculation for
# each measurement set
def Results(unit, unit2, value, value2):
    print('\nIt turns out that', value, unit, '=', value2, unit2, end ='')
    print('!')

# ThreeStrikes is triggered if three unusable
# values are entered for one variable
def ThreeStrikes():
    print("\nThree strikes; you're out!\n")

# Call the main function.
main()
