"""
Write the function getInRange(x, bound1, bound2) which takes 3 int or float values -- x, bound1, and bound2, 
where bound1 is not necessarily less than bound2. If x is between the two bounds, just return it unmodified. 
Otherwise, if x is less than the lower bound, return the lower bound, or if x is greater than the upper bound, 
return the upper bound. For example:
getInRange(1, 3, 5) returns 3 (the lower bound, since 1 lies to the left of the range [3,5])
getInRange(4, 3, 5) returns 4 (the original value, since 4 is in the range [3,5])
getInRange(6, 3, 5) returns 5 (the upper bound, since 6 lies to the right of the range [3,5])
getInRange(6, 5, 3) also returns 5 (the upper bound, since 6 lies to the right of the range [3,5])
"""


# Option 1
def getInRange(x, bound1, bound2):
    # low sets a variable for the smaller number since the question isn't clear on this
    low = min(bound1, bound2)
    # high sets a vairable for the higher number since the question isn't clear on this
    high = max(bound1, bound2)
    # If x is smaller than "low", "low" is reassigned to x and it will be returned
    if x < low: x = low
    # If x is greater than "high", "high" is reassigned to x and it will be returned
    if x > high: x = high
    # If x isn't less than low or higher than high, then it is within range and it will be returned
    return x

# Option 2
def getInRange(x, bound1, bound2):
    # low sets a vairable for the smaller number since the question isn't clear on this
    low = min(bound1, bound2)
    # high sets a vairable for the higher number since the question isn't clear on this
    high = max(bound1, bound2)
    """
    The code below simply does the following:....executing the code from the inner most...
    1. It checks the max between x and low and returned a value
    2. It check the minimum between the value returned and high and finally return it

    """
    return min(max(x, low), high)