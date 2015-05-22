## Define main

def main():
    ## get measurements to convert, checking for useability
    miles = float(input('How many miles would you like to convert? '))
    if miles < 0:
        print('\nError! You must enter a positive number of miles!\n')
    else:
        print('')
        fahren = float(input('How many fahrenheit degrees would you like to convert? '))
        if fahren > 1000:
            print('\nError! You must enter fahrenheit degrees equal to or less than 1,000!\n')
        else:
            print('')
            gallon = float(input('How many gallons would you like to convert? '))
            if gallon < 0:
                print('\nError! You must enter a positive number of gallons!\n')
            else:
                print('')
                lbs = float(input('How many pounds would you like to convert? '))
                if lbs < 0:
                    print('\nError! You must enter a positive number of pounds!\n')
                else:
                    print('')
                    inch = float(input('How many inches would you like to convert? '))
                    if inch < 0:
                        print('\nError! You must enter a positive number of inches!\n')
                    else:
                        print('')
                        ## call all the conversion/printing functions
                        MilesToKm(miles)
                        FahToCel(fahren)
                        GalToLit(gallon)
                        PoundsToKg(lbs)
                        InchesToCm(inch)

#calculate and print result for miles to km
def MilesToKm(miles):
    kilos = miles * 1.6
    print('It turns out that', miles, 'miles =', kilos, 'kilometers!\n')

#calculate and print result for fahrenheit to celsius
def FahToCel(fahren):
    celsi = (fahren - 32) * 5/9
    print('It turns out that', fahren, 'fahrenheit =', celsi, 'celsius!\n')

#calculate and print result for gallons to liters
def GalToLit(gallon):
    liters = gallon * 3.9
    print('It turns out that', gallon, 'gallons =', liters, 'liters!\n')

#calculate and print result for pounds to kilograms
def PoundsToKg(lbs):
    kgrams = lbs * .45
    print('It turns out that', lbs, 'pounds =', kgrams, 'kilograms!\n')

#calculate and print result for inches to centimeters
def InchesToCm(inch):
    centi = inch * 2.54
    print('It turns out that', inch, 'inches =', centi, 'centimeters!\n')

main()
