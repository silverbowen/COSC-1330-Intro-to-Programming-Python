## this program asks the user to enter the weight
## of a package, then displays the shipping charges


## define main - get input and call functions

def main():
    weight = float(input('How many pounds does the package weigh? '))
    print('')

    ## call functions
    if weight <= 0:
        print('Please enter a weight greater than zero!\n')
    elif weight <= 2:
        twoOrLess(weight)
    elif weight > 2 and weight <= 6:
        twoToSix(weight)
    elif weight > 6 and weight <= 10:
        sixToTen(weight)
    else:
        overTen(weight)

## define functions

## twoOrLess calculates and prints the shipping
## charges for packages of 2 pounds or less
def twoOrLess(weight):
    shipCharge = weight * 1.10
    print('The shipping charge for ', weight, ' lbs is: $', format(shipCharge, ',.2f'), '\n', sep='')

## twoToSix calculates and prints the shipping
## charges for packages over 2 pounds but no
## more than 6
def twoToSix(weight):
    shipCharge = weight * 2.20
    print('The shipping charge for ', weight, ' lbs is: $', format(shipCharge, ',.2f'), '\n', sep='')

## sixToTen calculates and prints the shipping
## charges for packages over 6 pounds but no
## more than 10
def sixToTen(weight):
    shipCharge = weight * 3.70
    print('The shipping charge for ', weight, ' lbs is: $', format(shipCharge, ',.2f'), '\n', sep='')

## overTen calculates and prints the shipping
## charges for packages over 10 poundsdef twoOrLess(weight):
def overTen(weight):
    shipCharge = weight * 3.80
    print('The shipping charge for ', weight, ' lbs is: $', format(shipCharge, ',.2f'), '\n', sep='')

##call main
main()
