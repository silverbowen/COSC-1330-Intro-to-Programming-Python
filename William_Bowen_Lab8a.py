# This program calculates a preset number of conversions between Standard and Metric.
# It writes each conversion set to a two-dimensional table [before, after], then displays the table.
# It's set up to convert values from START to (START + INTERVAL(COL-1)), by INTERVAL, inclusive.

# Set global variables
COL = 12                                       # number of columns in table = COL-1
ROW = 2                                        # number of rows in tables = ROW-1
START = -10                                  # start point for to-be-converted values
INTERVAL = 10                             # interval to increment to-be-converted values 

# define populate - populates all rows according to ROW/COL/INTERVAL values set globally
def populate(tab_to_pop):
    # use nested for loop to iterate through each row and column
    for r in range(ROW):
        for c in range(COL):
            # write element to to-be-converted value
            tab_to_pop[r][c] = c * INTERVAL + START
    return tab_to_pop

# define conversion - converts all rows except the first by column
def conversion(value, factor1, factor2):
    # use nested for loop to iterate through  each row and column after the first set of rows
    for r in range (1, ROW):
          for c in range(COL):
              # write element to converted value
              value[r][c] = round((value[r][c] + factor1) * factor2, 2)
    return value

# define main
def main():
    
    # create tables - uses global COL so each table is the same
    fah_table = populate([[0] * COL, [0] * COL])
    mile_table = populate([[0] * COL, [0] * COL])
    gal_table = populate([[0] * COL, [0] * COL])
    lbs_table = populate([[0] * COL, [0] * COL])
    inch_table = populate([[0] * COL, [0] * COL])

    # convert tables - passes 2 additional variables so only one fnctin is needed
    fah_table = conversion(fah_table, -32, 5/9)
    mile_table = conversion(mile_table, 0, 1.6)
    gal_table = conversion(gal_table, 0, 3.9)
    lbs_table = conversion(lbs_table, 0, .45)
    inch_table = conversion(inch_table, 0, 2.45)

    # display tables
    print('Fahrenheit to Celsius table:\n', fah_table, '\n')
    print('Miles to Kilometers table:\n', mile_table, '\n')
    print('Gallons to Liters table:\n', gal_table, '\n')
    print('Pounds to Kilograms table:\n', lbs_table, '\n')
    print('Inches to Centimeters table:\n', inch_table, '\n')
    
# call main
main()
