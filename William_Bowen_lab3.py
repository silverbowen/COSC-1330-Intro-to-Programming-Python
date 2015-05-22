## the whole enchilada

def main():
    ## get measurements to convert
    miles = float(input('How many miles would you like to convert? '))
    print('')
    fahren = float(input('How many fahrenheit degrees would you like to convert? '))
    print('')
    gallon = float(input('How many gallons would you like to convert? '))
    print('')
    lbs = float(input('How many pounds would you like to convert? '))
    print('')
    inch = float(input('How many inches would you like to convert? '))  
    print('')
    ## call all the conversion/printing functions
    milesToKm(miles)
    FahToCel(fahren)
    GalToLit(gallon)
    PoundsToKg(lbs)
    InchesToCm(inch)

#calculate and print result for miles to km
def milesToKm(miles):
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
