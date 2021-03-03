"""
Write the function circlesIntersect(x1, y1, r1, x2, y2, r2) that takes 6 numbers 
(ints or floats) -- x1, y1, r1, x2, y2, r2 -- that describe the circle centered at 
(x1,y1) with radius r1, and the circle centered at (x2,y2) with radius r2, and 
returns True if the two circles intersect and False otherwise.
"""
from math import sqrt

"""
Code Logic
If the distance between two points (x1, y1) and (x2, y2) is larger than
the sum of the 2 radia, the two circles can't intersect. Else, they will intersect
"""
def distance(x1, y1, x2, y2):
    return int(sqrt((x2 - x1)**2 + (y2 - y1)**2))


def circlesIntersect(x1, y1, r1, x2, y2, r2):
    return (distance(x1, y1, x2, y2) <= (r1 + r2))