# This program imports a module that uses
# value-returning functions to calculate
# conversions between Standard and Metric

import StandardToMetric

def main():
    # total will keep track of how many measurements we convert
    total = 0
    # Reset resets errorcount and conversion to 0
    errorcount, conversion = StandardToMetric.Reset()
    # Validate call checks whether to call functions
    while StandardToMetric.Validate_Call(conversion, errorcount):
        # Conversion gets a menu number for measurement to convert
        conversion = StandardToMetric.Conversion()
        # Validate_Conversion validates conversion
        if StandardToMetric.Validate_Conversion(conversion):
            # Unit converts menu number to actual unit
            unit, unit2, factor, factorb = StandardToMetric.Unit(conversion)
            # Validate_Loop validates the errorcount and conversion
            while StandardToMetric.Validate_Loop(errorcount, conversion):
                # Measure gets a measurement
                measure = StandardToMetric.Measure(unit)
                # Validate_Measurement validates the measurement
                if StandardToMetric.Validate_Measure(conversion, measure):
                    # Results converts the measure and displays the result
                    StandardToMetric.Results(unit, unit2, measure, factor, factorb)
                    # Reset again
                    errorcount, conversion = StandardToMetric.Reset()
                    # Total iterates a running total
                    total = StandardToMetric.Total(total)
                # when measure is invalid:
                else:
                    # Invalid_Measure displays an error message
                    StandardToMetric.Invalid_Measure(unit)
                    # Errorcount iterates errorcount
                    errorcount = StandardToMetric.Errorcount(errorcount)
        # Invalid Conversion displays an error message
        else:
            conversion = StandardToMetric.Invalid_Conversion(conversion)
    #Validate_End checks if it's time for AllDone
    if StandardToMetric.Validate_End(conversion):
        # All_Done ends the program when the user inputs 6
        # for the menu item
        StandardToMetric.All_Done(total)
    # ThreeStrikes ends the program in the event of
    # three invalid inputs for the same measurement
    else:
        StandardToMetric.ThreeStrikes()

main()
