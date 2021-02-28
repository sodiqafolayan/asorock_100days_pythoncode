"""
fabricExcess(inches) [standard, 10 pts]
Write the function fabricExcess(inches) that takes the number of inches of fabric 
desired and returns the minimum number of inches of excess fabric that must be 
purchased (as purchases must be in whole yards). Hint: you may want to use fabricYards, 
which you just wrote!
"""

def fabricExcess(inches):
    c = inches % 36
    if not c == 0:
        return 36 - c
    return c