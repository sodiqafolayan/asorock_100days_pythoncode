"""
numberOfPoolBalls(rows)
Pool balls are arranged in rows where the first row contains 1 pool ball and 
each row contains 1 more pool ball than the previous row. Thus, for example, 
3 rows contain 6 total pool balls (1+2+3). With this in mind, write the function 
numberOfPoolBalls(rows) that takes a non-negative int value, the number of rows, 
and returns another int value, the number of pool balls in that number of full rows. 
For example, numberOfPoolBalls(3) returns 6. We will not limit our analysis to a "rack" 
of 15 balls. Rather, our pool table can contain an unlimited number of rows. 
Hint: you may want to briefly read about Triangular Numbers. Also, remember not to use loops!

"""

def nearestBusStop(street):
    if not street % 8 == 0:
        lower_street = street - (street % 8)
        upper_street = (8 - (street % 8)) + street
        lower_street_diff = street - lower_street
        upper_street_diff = upper_street - street
        if lower_street_diff <= upper_street_diff:
            return lower_street
        elif lower_street_diff > upper_street_diff:
            return upper_street
    return street