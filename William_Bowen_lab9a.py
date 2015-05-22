## This program gets a series of English measurements and converts them
## into Metric measurements. It uses error checking to prevent invalid inputs,
## and in the event of an invalid input it ends.

## In addition, this version asks the user for their name and their email address
## before displaying the results of the conversions. It searches the input string for
## the @ symbol. If the symbol is not found, it asks the user to re-enter their email
## address. Finally, it includes the user’s name in the conversion output.


# Define main

def main():
    # get measurements to convert, checking for useability
    miles = float(input('How many miles would you like to convert? '))
    # miles must be positive
    if miles < 0:
        print('\nError! You must enter a positive number of miles!\n')
    else:
        print('')
        fahren = float(input('How many fahrenheit degrees would you like to convert? '))
        # fahren must b => 1000
        if fahren > 1000:
            print('\nError! You must enter fahrenheit degrees equal to or less than 1,000!\n')
        else:
            print('')
            gallon = float(input('How many gallons would you like to convert? '))
            # gallon must be positive
            if gallon < 0:
                print('\nError! You must enter a positive number of gallons!\n')
            else:
                print('')
                lbs = float(input('How many pounds would you like to convert? '))
                # lbs must be positive
                if lbs < 0:
                    print('\nError! You must enter a positive number of pounds!\n')
                else:
                    print('')
                    inch = float(input('How many inches would you like to convert? '))
                    # inch must be positive
                    if inch < 0:
                        print('\nError! You must enter a positive number of inches!\n')
                    else:
                        print('')
                        name = input('Please enter your name: ' )
                        # name must include at least one character
                        while len(name) < 1:
                            print('\nError! You must enter at least one character (so I have something to display with your results)!\n')
                            name = input('Please enter your name: ' )
                        print('')
                        email = input('Please enter your email address: ')
                        exists_at = email.find('@')
                        # email must include the '@' symbol
                        while exists_at == -1:
                            print('\nError! You must enter a valid email adress (valid email adresses contain the "@" symbol)!\n')
                            email = input('Please enter your email address: ')
                            exists_at = email.find('@')
                            
                        print('')
                        ## call all the conversion/printing functions
                        YourName(name)
                        MilesToKm(miles)
                        FahToCel(fahren)
                        GalToLit(gallon)
                        PoundsToKg(lbs)
                        InchesToCm(inch)

# define YourName
def YourName(name):
    print('Here are all of your English to Metric conversions, ', name, '.\n', sep='')

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
