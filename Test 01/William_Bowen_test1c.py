## this program asks the user to enter the weight
## of a package, then displays the shipping charges


## define main - all main does is call getWeight

def main():
    
    ## call function
    getWeight()
                
## define other functions
                
## getWeight gets the weight of the package
## and calls getCharge
def getWeight():
    weight = float(input('How many pounds does the package weigh? '))
    print('')
    getCharge(weight)
    
## getCharge calculates and prints the shipping charges
def getCharge(weight):
    if weight <= 0:
        print('Please enter a weight greater than zero!\n')
    elif weight <= 2:
        shipCharge = weight * 1.10
        print('The shipping charge for ', weight, ' lbs is: $'
        + format(shipCharge, ',.2f'), '\n', sep='')
    elif weight > 2 and weight <= 6:
        shipCharge = weight * 2.20
        print('The shipping charge for ', weight, ' lbs is: $'
        + format(shipCharge, ',.2f'), '\n', sep='')
    elif weight > 6 and weight <= 10:
        shipCharge = weight * 3.70
        print('The shipping charge for ', weight, ' lbs is: $'
        + format(shipCharge, ',.2f'), '\n', sep='')
    else:
        shipCharge = weight * 3.80
        print('The shipping charge for ', weight, ' lbs is: $'
        + format(shipCharge, ',.2f'), '\n', sep='')

##call main
main()
