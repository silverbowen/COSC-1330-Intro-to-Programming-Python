## define main
def main():
    ## user input begins here - miles first
    miles = float(input('How many miles would you like to convert? '))
    ## set errorcount
    errorcount = 0
    ## check for errors and repeat input if needed
    ## up to three times, then kaput
    while miles < 0 and errorcount != 2:
            Error('miles')
            miles = float(input('How many miles would you like to convert? '))
            if miles < 0:
                errorcount += 1
    ## if input is good, continue
    if  errorcount != 2:
        print('')
        ## user input for fahren
        fahren = float(input('How many fahrenheit degrees would you like to convert? '))
        ## reset errorcount
        errorcount = 0
        ## check for errors and repeat input if needed
        ## up to three times, then kaput
        while fahren > 1000 and errorcount != 2:
            Error('fahrenheit degrees')
            fahren = float(input('How many fahrenheit degrees would you like to convert? '))
            if fahren > 1000:
                errorcount += 1
    if errorcount != 2:
        print('')
        ## user input for gallons
        gallon = float(input('How many gallons would you like to convert? '))
        ## reset errorcount
        errorcount = 0
        ## check for errors and repeat input if needed
        ## up to three times, then kaput
        while gallon < 0 and errorcount != 2:
            Error('gallons')
            gallon = float(input('How many gallons would you like to convert? '))
            if gallon < 0:
                errorcount += 1
    if errorcount != 2:
        print('')
        ## user input for pounds
        lbs = float(input('How many pounds would you like to convert? '))
        ## reset errorcount
        errorcount = 0
        ## check for errors and repeat input if needed
        ## up to three times, then kaput
        while lbs < 0 and errorcount != 2:
            Error('pounds')
            lbs = float(input('How many pounds would you like to convert? '))
            if lbs < 0:
                errorcount += 1
    if errorcount != 2:
        print('')
         ## user input for inches
        inch = float(input('How many inches would you like to convert? '))
        ## reset errorcount
        errorcount = 0
        ## check for errors and repeat input if needed
        ## up to three times, then kaput
        while inch < 0 and errorcount != 2:
            Error('inches')
            inch = float(input('How many inches would you like to convert? '))
            if inch < 0:
                errorcount += 1
    if errorcount != 2:
        print('')
    
    ## call all the conversion/printing functions
    if errorcount != 2:
        MilesToKm(miles)
        FahToCel(fahren)
        GalToLit(gallon)
        PoundsToKg(lbs)
        InchesToCm(inch)

    ## or end program if user has three strikes
    if errorcount == 2:
        ThreeStrikes()

## more definitions

## error functions:
    
## three strikes
def ThreeStrikes():
    print("\nThree strikes; you're out!\n")

# Error prints error message for incorrect input
# allowing for a syntax difference for degrees
def Error(unit):
    if unit == 'fahrenheit degrees':
        special = 'one thousand or less'
    else:
        special = 'a nonnegative number of'
    print('\nError! You must enter', special, unit, end='')
    print('!\n')

## conversion and print functions:
    
#miles to km
def MilesToKm(miles):
    kilos = miles * 1.6
    print('It turns out that', miles, 'miles =', kilos, 'kilometers!\n')

#fahrenheit to celsius
def FahToCel(fahren):
    celsi = (fahren - 32) * 5/9
    print('It turns out that', fahren, 'fahrenheit =', celsi, 'celsius!\n')

#gallons to liters
def GalToLit(gallon):
    liters = gallon * 3.9
    print('It turns out that', gallon, 'gallons =', liters, 'liters!\n')

#pounds to kilograms
def PoundsToKg(lbs):
    kgrams = lbs * .45
    print('It turns out that', lbs, 'pounds =', kgrams, 'kilograms!\n')

#inches to centimeters
def InchesToCm(inch):
    centi = inch * 2.54
    print('It turns out that', inch, 'inches =', centi, 'centimeters!\n')

main()
