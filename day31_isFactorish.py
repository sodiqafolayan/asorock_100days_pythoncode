"""
isFactorish(n)
Write the function isFactorish(n) that takes a value n that can be of any type, and returns True 
if n is a (possibly-negative) integer with exactly 3 unique digits (so no two digits are the same), 
where each of the digits is a factor of the number n itself. In all other cases, the function returns False
without crashing). For example:
assert(isFactorish(412) == True)      # 4, 1, and 2 are all factors of 412
assert(isFactorish(-412) == True)     # Must work for negative numbers!
assert(isFactorish(4128) == False)    # 4128 has more than 3 digits
assert(isFactorish(112) == False)     # 112 has duplicate digits (two 1's)
assert(isFactorish(420) == False)     # 420 has a 0 (no 0's allowed)
assert(isFactorish(42) == False)      # 42 has a leading 0 (no 0's allowed)
assert(isFactorish(412.0) == False)   # 412.0 is not an int
assert(isFactorish('nope!') == False) # don't crash on strings
"""

def isFactor(f, n):
    if n == 0:
        return True
    elif f == 0:
        return False
    return n % f == 0

def isFactorish(n):
    # This ensure its (positibly-negative) integer with not more than 3 digits
    if isinstance(n, int) and abs(n) < 1000 and abs(n) > 99:
        # this check if digits are unique
        left = int(abs(n))//100
        mid = int((abs(n)//10))%10
        right = int(abs(n))%10
        if (left != mid and left != right) and (mid != right):
            left_check = isFactor(left, n)
            mid_check = isFactor(mid, n)
            right_check = isFactor(right, n)
            result = (left_check == mid_check and left_check == right_check) and (mid_check == right_check)
            return result == True
    return False


assert(isFactorish(412) == True)      # 4, 1, and 2 are all factors of 412
assert(isFactorish(-412) == True)     # Must work for negative numbers!
assert(isFactorish(4128) == False)    # 4128 has more than 3 digits
assert(isFactorish(112) == False)     # 112 has duplicate digits (two 1's)
assert(isFactorish(420) == False)     # 420 has a 0 (no 0's allowed)
assert(isFactorish(42) == False)      # 42 has a leading 0 (no 0's allowed)
assert(isFactorish(412.0) == False)   # 412.0 is not an int
