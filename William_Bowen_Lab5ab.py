# This program uses recursive loops
# to calculate conversions between
# Standard and Metric measurements

def main():
    count = 0
    errorcount = 0
    miles = 0
    fahren = 0
    gallon = 0
    lbs = 0
    inch = 0
    GetMeasure(count, errorcount, miles, fahren, gallon, lbs, inch)

# GetMeasure asks how many units to convert,
# depending on current count,
# then calls ErrorCheck to validate.
# When count passes 4, it prints results.
def GetMeasure(count, errorcount, miles, fahren, gallon, lbs, inch):
    # check whether to call ThreeStrikes
    if errorcount == 3:
        ThreeStrikes()
    else:
        # set values for Question
        if count == 0:
            unit = 'miles'
            Question(unit)
            miles = float(input(''))
            ErrorCheck(count, errorcount, unit, miles, miles, fahren, gallon, lbs, inch)
        elif count == 1:
            unit = 'Fahrenheit degrees'
            Question(unit)
            fahren = float(input(''))
            ErrorCheck(count, errorcount, unit, fahren, fahren, gallon, lbs, inch, miles)
        elif count == 2:
            unit = 'gallons'
            Question(unit)
            gallon = float(input(''))
            ErrorCheck(count, errorcount, unit, gallon, gallon, lbs, inch, miles, fahren)
        elif count == 3:
            unit = 'pounds'
            Question(unit)
            lbs = float(input(''))
            ErrorCheck(count, errorcount, unit, lbs, lbs, inch, miles, fahren, gallon)
        elif count == 4:
            unit = 'inches'
            Question(unit)
            inch = float(input(''))
            ErrorCheck(count, errorcount, unit, inch, inch, miles, fahren, gallon, lbs)

        # calculate and print answers
        else:
            Results('miles', 'kilometers', miles, miles * 1.6)
            Results('Fahrenheit degrees', 'Celsius degrees', fahren, (fahren-32) * 5/9)
            Results('gallons', 'liters', gallon, gallon * 3.9)
            Results('pounds', 'kilograms', lbs, lbs * .45)
            Results('inches', 'centimeters', inch, inch * 2.54)
            print('\n')

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

# ErrorCheck validates input. If valid,
# it iterates count. Otherwise it iterates
# errorcount. Then it calls GetMeasure.
def ErrorCheck(count, errorcount, unit, value, miles, fahren, gallon, lbs, inch):
    if count == 1 and value > 1000 and errorcount != 3:
        Error(unit)
        errorcount += 1
        GetMeasure(count, errorcount, miles, fahren, gallon, lbs, inch)
    elif count != 1 and value < 0 and errorcount != 3:
        Error(unit)
        errorcount += 1
        GetMeasure(count, errorcount, miles, fahren, gallon, lbs, inch)
    else:
        count += 1
        GetMeasure(count, errorcount, miles, fahren, gallon, lbs, inch)

# Results prints the calculation for
# each unit/unit2 set
def Results(unit, unit2, value, value2):
    print('\nIt turns out that', value, unit, '=', value2, unit2, end ='')
    print('!')

# ThreeStrikes triggers if three unusable
# values are entered for one variable

def ThreeStrikes():
    print("\nThree strikes; you're out!\n")

# Call the main function.
main()
