## get input about measurements to convert
## (this would be much less clunky with if/then loops!!)

miles = float(input('How many miles would you like to convert?\n'))
faren = float(input('How many fanrenheit degrees would you like to convert?\n'))
gallon = float(input('How many gallons would you like to convert?\n'))
lbs = float(input('How many pounds would you like to convert?\n'))
inch = float(input('How many inches would you like to convert?\n'))

## convert measurements

kilos = miles * 1.6
celsi = (faren - 32) * 5/9
liters = gallon * 3.9
kgrams = lbs * .45
centi = inch * 2.54

## print result in a pithy manner

print('Cheerio, old chap!\n', miles, 'miles is', kilos, 'kilos!\n', \
         faren, 'fanrenheit degrees is', celsi, 'celsius degrees!\n', \
         gallon, 'gallons is', liters, 'liters!\n', \
          lbs, 'pounds is', kgrams, 'kilograms!\n', \
          inch, 'inches is', centi, 'centimeters!\n', \
          'Pip, pip...\nHurray!!!')
