# This program calculates a preset number
# of conversions between Standard and Metric.
# It writes these conversion to a .txt file.

# Set global variables
FILE = 'conversions.txt'
LOOP = 10

def main():
    # Open FILE for writing
    converted = open(FILE, 'w')
    # Get a menu letter for measurement to convert
    conversion = input('\nWhat would you like to convert?\n' + \
                                '-------------------------------------------------\n' + \
                                'a) Miles to Kilometers\n' +\
                                'b) Fahrenheit degrees to Celsius degrees\n' + \
                                'c) Gallons to Liters\n' + \
                                'd) Pounds to Kilograms\n' + \
                                'e) Inches to Centimeters\n\n' + \
                                '(Please choose a menu letter from a to e)\n\n')
    # Check checks whether to get a new conversion
    while Check(conversion):
        # Display an error message if conversion isn't a through e
        # and ask again
        conversion = input("\n'"+conversion+"' "'is invalid! Please ' + \
                                      'choose a menu letter.\n\n(a,  b, c, d, or e)? ')
    # Unit converts menu letter to actual unit
    unit, unit2, factor, factorb = Unit(conversion)
    # Initialize not_oops - an iterator to weed out
    # measure input errors (so we always write
    # LOOP good values to our .txt) 
    not_oops = 0
    # Start measure getting loop
    while not_oops != LOOP:
            # Try/except to handle Value Errors
            try:
                # Get a measurement
                measure = float(input('\nHow many '+unit+' would you' + \
                                                   ' like to convert? '))
                # Validate_Measurement validates the measurement
                if Validate_Measure(conversion, measure):
                    # Convert the measure and copy the result to FILE
                    # (answer is assigned for ease of reading from the file later)
                    answer = format((measure - factorb) * factor, ',.2f')
                    converted.write(str(measure) + '\n')
                    converted.write(unit + '\n')
                    converted.write(str(answer) + '\n')
                    converted.write(unit2 + '\n')
                    # Tell user it's written to file
                    print('\nI wrote the original unit and measurement plus ' + \
                            'the conversion unit and measurement to ', FILE, '.', sep='')
                    not_oops += 1
                # When measure is invalid
                else:
                    # Invalid_Measure displays an error message if
                    # measure is invalid
                    Invalid_Measure(unit)
            # If a nonumerical character is entered
            except ValueError:
                print("\nError: I can only accept numbers, not letters or symbols.")
    # End the program nicely
    print('\nThanks for letting me convert that stuff for you!\n\n' + \
            "I'll close", FILE, 'now. Bye-bye!\n')
    # close FILE
    converted.close()

# Check returns True when conversion
# is invalid, so ask for conversion loop iterates
def Check(conversion):
    if conversion in ('a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E'):
        status = False
    else:
        status = True
    return status


# Validate_Conversion validates input to conversion
def Validate_Conversion(conversion):
    if conversion in ('a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E'):
        status = True
    else:
        status = False
    return status

# Unit converts menu letter and returns unit,
# unit2, factor, and factorb
def Unit(conversion):
    factorb = 0
    if conversion == 'a':
        unit = 'miles'
        unit2 = 'kilometers'
        factor = 1.6
    elif conversion == 'b':
        unit = 'Fahrenheit degrees'
        unit2 = 'Celsius degrees'
        factor = 5/9
        factorb= 32
    elif conversion == 'c':
        unit = 'gallons'
        unit2 = 'liters'
        factor = 3.9
    elif conversion == 'd':
        unit = 'pounds'
        unit2 = 'kilograms'
        factor = .45
    else:
        unit = 'inches'
        unit2 = 'centimeters'
        factor = 2.54
    return unit, unit2, factor, factorb

# Validate_Measure checks that measure is valid
def Validate_Measure(conversion, measure):
    if conversion == 'b' and measure > 1000:
        status = False
    elif conversion != 'b' and measure < 0:
        status = False
    else:
        status = True
    return status

# Invalid_Measure sends an error message
def Invalid_Measure(unit):
    if unit == 'Fahrenheit degrees':
        special = 'one thousand or less'
    else:
        special = 'a nonnegative number of'
    print('\nError! You must enter', special, unit+"!\n\nLet's try again.")

main()
