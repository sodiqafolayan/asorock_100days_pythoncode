"""
fabricYards(inches)
Fabric must be purchased in whole yards, so purchasing just 1 inch of fabric requires 
purchasing 1 entire yard. With this in mind, write the function fabricYards(inches) 
that takes the number of inches of fabric desired, and returns the smallest number 
of whole yards of fabric that must be purchased. Note: 36 inches equals 1 yard.
"""

def fabricYards(inches):
    c = inches % 36
    if not c == 0:
        return (((36 - c) + inches) / 36)
    return (inches / 36)