## this program asks for totals sales, then calculates
## and displays the county sales tax, state sales tax,
## and total sales tax.


## define main - get input and call functions

def main():
    sales = float(input('What were the total monthly sales? '))
    print('')

    ## call functions
    County(sales)
    State(sales)
    Total(sales)

## define functions

## County calculates and prints county sales tax
def County(sales):
    countyTax = sales * .02
    print('The total county sales tax collected for the month is: $', format(countyTax, ',.2f'), '\n', sep='')

## State calculates and prints state sales tax
def State(sales):
    stateTax = sales * .04
    print('The total state sales tax collected for the month is: $', format(stateTax, ',.2f'), '\n', sep='')

## Total calculates and prints total sales tax
def Total(sales):
    totalTax = sales * .06
    print('The total sales tax (county plus state) collected for the month is: $', format(totalTax, ',.2f'), '\n', sep='')

##call main
main()
