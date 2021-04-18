from math import sqrt

# Helper function to be used in is_prime() function
def square_root(n: int) -> int:
    return sqrt(n)


def is_prime(n: int) -> bool:
    # Prime numbers are natural numbers > 1 and not a product of two other natural numbers (eg 3, 5, 7, 11 etc)
    # This line reduces our iteration by excluding all numbers less than 1, negative numbers and even numbers (
    # even numbers cannot be prime)
    if (n < 2 or n % 2 == 0):
        return False
    # With the knowledge that factors of a number (eg n) are two numbers (a * b) you multiply together to get n
    # eg for 24 2*12, 3*8, 4*6, So it is clear that each factor pair contain two numbers one of which is not larger
    # than the square root and the other not smaller than the square root of 24
    # Hence, we only need to iterate from 3 to the squaroot of the number we want to check if its prime or not to the number + 1
    # skipping even numbers
    max_factor = round(square_root(n)) 
    for factor in range(3, max_factor+1, 2):
        if n % factor == 0:
            return False
    return True

def test_square_root():
    print("Testing square root function....")
    assert(square_root(100) == 10)
    assert(square_root(4) == 2)
    print("Passed......")

def test_is_prime():
    print("Testing is_prime function.....")
    assert(is_prime(25) == False)
    assert(is_prime(36) == False)
    assert(is_prime(7) == True)
    assert(is_prime(71) == True)
    print("Passed......")


test_square_root()
test_is_prime()
