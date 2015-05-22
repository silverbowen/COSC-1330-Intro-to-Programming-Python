## I used global constants for ease of modding
## in case we return to this program later

## START, END,and INCREMENT set the
## dimensions of the pyramid
START = 10
END = 1
INCREMENT = -1

## SYMBOL sets what the pyramid is made of
## I added spaces on either side of
## the star, to make it nicer
SYMBOL = ' * '

## main is a nested loop that prints
## a pyramid of SYMBOLS
def main():
    ## first loop, sets terms for each row
    for count in range(START, END - 1, INCREMENT):
        ## second loop, nested
        ## sets number of stars in row,
        ## based on inverse column number 
        for count in range(count, END - 1, INCREMENT):
            ## print each individual symbol
            print(SYMBOL , end='')
        ## back to first loop, new line
        ## to make it prettier
        print('\n')

## call main
main()
