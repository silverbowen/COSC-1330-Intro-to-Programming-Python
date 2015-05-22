## This is a payroll program for employees of SoftwarePirates Inc.
## It calculates base pay plus commision/bonuses minus reductions.

## global variables
BASE_SALARY = 2000
VACATION_DEDUCTION = float(200.00)
FIVEYEAR_BONUS = 1000

def main():
    ## get input:
    
    ## get name
    name = input('Please enter the name of the salesperson: ')
    print('')

    ## get longevity, end program if employee hasn't worked for at least a month
    longevity = int(input('How long have they worked for SoftwarePirates Inc. (in months)? '))
    print('')
    if longevity < 1:
        print('This employee is not eligible for pay yet!\n')
    else:
        
        ## get sales
        sales = float(input('What were their sales (no commas, please)? $'))
        print('')

        ## get vacation days
        vacation_days = int(input('How many vacation days did they take this month? '))
        print('')

        ##call functions
        Name(name)
        Longevity(longevity)
        Commission(sales)
        Bonus(longevity, sales)
        Additional_Bonus(longevity, sales)
        Deductions(vacation_days)
        Gross(longevity, sales, vacation_days, name)

## define name - prints name and leads into breakdown       
def Name(name):
    print('For employee', name, 'here is the payroll breakdown:\n')
    
## define Longevity - prints time worked at company
def Longevity(longevity):
    if longevity == 1 or longevity == 2:
        print('They have worked for SoftwarePirates Inc. for less than three months.\n')
    elif longevity > 2 and longevity < 61:
        print('They have worked for SoftwarePirates Inc. for at least three months, but not over five years.\n')
    else:
        print('They have worked for SoftwarePirates Inc. for over five years.\n')

## define Commission - prints whether and what commission percent was earned        
def Commission(sales):
    if sales < 1000:
        print('They did not generate a commision.\n')
    elif sales > 999 and sales < 100001:
        print('They generated a 2% commission of: $', format(sales * .02, ',.2f'), '\n', sep='')
    elif sales > 100000 and sales < 500001:
        print('They generated a 15% commission of: $', format(sales * .15, ',.2f'), '\n', sep='')
    elif sales > 500000 and sales < 1000001:
        print('They generated a 28% commission of: $', format(sales * .28, ',.2f'), '\n', sep='')
    else:
        print('They generated a 35% commission of: $', format(sales * .35, ',.2f'), '\n', sep='')

## define Bonus - prints whether and what bonus was earned
def Bonus(longevity, sales):
    if longevity < 3 or sales < 100001:
        print('They are not eligible for a bonus.\n')
    elif sales > 100000 and sales < 500001:
        print('Bonus is: $1,000.00\n')
    elif sales > 500000 and sales < 1000001:
        print('Bonus is: $5,000.00\n')
    else:
        print('Bonus is: $100,000.00\n')

## define Additional_Bonus - prints additional bonus, if any
def Additional_Bonus(longevity, sales):
    if longevity > 60 and sales > 100000:
        print('Additional bonus is: $', FIVEYEAR_BONUS, '\n', sep='')

## define Deduction - prints deduction, if any
def Deductions(vacation_days):
    if vacation_days > 3:
        print('Deduction is: -$', format(VACATION_DEDUCTION, ',.2f'), '\n', sep='')

## define Gross - calculates gross pay, taking into account commissions, bonuses, and deductions
def Gross(longevity, sales, vacation_days, name):

    ##calculate longevity bonus based on sales commission
    if longevity < 3 or sales < 100001:
        bonus = 0
    elif sales > 100000 and sales < 500001:
        bonus = 1000
    elif sales > 500000 and sales < 1000001:
        bonus = 5000
    else:
        bonus = 100000

    ##start a running total
    total = BASE_SALARY + bonus

    ##calculate commission based on sales and continue running total
    if sales < 1000:
        commission = 0
    elif sales > 999 and sales < 100001:
        commission = .02
    elif sales > 100000 and sales < 500001:
        commission = .15
    elif sales > 500000 and sales < 1000001:
        commission = .28
    else:
        commission = .35
    total = total + (sales * commission)

    ##calculate additional bonus and continue running total
    if longevity > 60 and sales > 100000:
        total = total + FIVEYEAR_BONUS
        
    ##calculate deductions and continue running total
    if vacation_days > 3:
        total = total - VACATION_DEDUCTION
        
    ##print total
    print('Total pay earned by ', name, ' is: $', format(total, ',.2f'), '\n', sep='')

##call main    
main()
