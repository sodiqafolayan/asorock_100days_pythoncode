"""
Write the function isFactor(f, n) that takes two int values f and n, and returns True 
if f is a factor of n, and False otherwise. Note that every integer is a factor of 0
"""

def isFactor(f, n):
    # Since every integer is a factor of Zero and Python cannot divide by Zero, this line prevents ZeroDivisionError
    if n == 0:
        return True
    # This captures the posibility of the factor being Zero and prevents ZeroDivisionError
    elif f == 0:
        return False
    return n % f == 0
