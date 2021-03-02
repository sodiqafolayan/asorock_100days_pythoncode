"""
numberOfPoolBallRows(balls)
This problem is the inverse of the previous problem. Write the function 
numberOfPoolBallRows(balls) that takes a non-negative int number of pool balls, 
and returns the smallest int number of rows required for the given number of pool balls. 
Thus, numberOfPoolBallRows(6) returns 3. Note that if any balls must be in a row, 
then you count that row, and so numberOfPoolBallRows(7) returns 4 (since the 4th row 
must have a single ball in it). Hint: you may want to briefly read about Triangular Numbers, 
and also think about how this problem relates to the numberOfPoolBalls problem above.

"""

def numberOfPoolBalls(rows):
    ans = rows*(rows+1)/2
    return ans