"""
Write the function distance(x1, y1, x2, y2) that takes four int or float 
values x1, y1, x2, y2 that represent the two points (x1, y1) and (x2, y2), 
and returns the distance between those points as a float.
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