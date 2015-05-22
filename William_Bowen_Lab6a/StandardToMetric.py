# this module contains functions that convert
# Standard measurements to Metric

# Validate_Call checks whether call is valid
def Validate_Call(conversion, errorcount):
    if conversion != 6 and errorcount != 3:
        status = True
    else:
        status = False
    return status

# Conversion asks which type of measurement to convert
# conversion = 6 is the sentinel
def Conversion():
    conversion = int(input('\nWhat would you like to convert?\n\n' + \
                                        '1) Miles to Kilometers\n' +\
                                        '2) Fahrenheit degrees to Celsius degrees\n' + \
                                        '3) Gallons to Liters\n' + \
                                        '4) Pounds to Kilograms\n' + \
                                        '5) Inches to Centimeters\n' + \
                                        "6) I'm done, thanks!\n\n"))
    return conversion

# Validate_Conversion validates input to conversion
def Validate_Conversion(conversion):
    if conversion > 0 and conversion < 6:
        status = True
    else:
        status = False
    return status

# Invalid_Conversion sends an error message if
# needed and resets loop or passes on the sentinel
def Invalid_Conversion(conversion):
    if conversion != 6:
        print(conversion, 'is invalid! Please choose a menu number from 1 to 6.')
        return conversion
    else:
        conversion = 6
    return conversion

# Unit converts menu number to actual unit,
# unit2, factor, and factorb
def Unit(conversion):
    factorb = 0
    if conversion == 1:
        unit = 'miles'
        unit2 = 'kilometers'
        factor = 1.6
    elif conversion == 2:
        unit = 'Fahrenheit degrees'
        unit2 = 'Celsius degrees'
        factor = 5/9
        factorb= 32
    elif conversion == 3:
        unit = 'gallons'
        unit2 = 'liters'
        factor = 3.9
    elif conversion == 4:
        unit = 'pounds'
        unit2 = 'kilograms'
        factor = .45
    else:
        unit = 'inches'
        unit2 = 'centimeters'
        factor = 2.54
    return unit, unit2, factor, factorb

# Validate_Loop validates the errorcount and conversion
def Validate_Loop(errorcount, conversion):
    if errorcount != 3 and conversion != 0:
        status = True
    else:
        status = False
    return status

# Measure asks how many measures to convert
def Measure(unit):
    print('\nHow many', unit, 'would you like to convert? ', end='')
    measure = float(input(''))
    return measure

# Validate_Measure checks that measure is valid
def Validate_Measure(conversion, measure):
    if conversion == 2 and measure > 1000:
        status = False
    elif conversion != 2 and measure < 0:
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
    print('\nError! You must enter', special, unit+'!')

# Errorcount iterates the errorcount
def Errorcount(errorcount):
    errorcount += 1
    return errorcount

# Results calculates and displays the results
def Results(unit, unit2, measure, factor, factorb):
        print('\nIt turns out that', measure, unit, '= ' + \
                format((measure - factorb) * factor, ',.2f') + \
                '', unit2+'!')
        
# Total iterates a running total of measurements converted
def Total(total):
    total += 1
    return total

# Reset resets errorcountand conversion
def Reset():
    errorcount = 0
    conversion = 0
    return errorcount, conversion

# Validate_End validates the end condition
def Validate_End(conversion):
    if conversion == 6:
        status = True
    else:
        status = False
    return status

# All_Done displays a nice end message
def All_Done(total):
    if total > 0:
        print('\nThanks for letting me convert that stuff for you!\n' + \
                'That was', total, "measurement(s). Wow!\n(I didn't " + \
                'count oopsies, of course.)\nI hope this helped. Bye-bye!\n')
    else:
        print("\nBummer. I didn't convert anything!\n" +\
                 'I feel so useless. Maybe next time?\n')

# ThreeStrikes is triggered if three unusable
# values are entered for one variable
def ThreeStrikes():
    print("\nThree strikes; you're out!\n")
