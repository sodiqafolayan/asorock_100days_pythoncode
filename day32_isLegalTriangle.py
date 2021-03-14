"""
isLegalTriangle(s1, s2, s3)
Write the function isLegalTriangle(s1, s2, s3) that takes three int or float values representing 
the lengths of the sides of a triangle, and returns True if such a triangle exists and False 
otherwise. Note from the triangle inequality that the sum of each two sides must be greater than 
the third side, and further note that all sides of a legal triangle must be positive. 
Hint: how can you determine the longest side, and how might that help?

"""
# Step 1: Cretae a helper function to check if all given sides are positive
def absCheck(a, b, c):
    return (a, b, c) == (abs(a), abs(b), abs(c))

# As long as no two sides is less than the longest side, then we can make a triangle
def isLegalTriangle(s1, s2, s3):
    if absCheck(s1, s2, s3):
        #return ((d + e + f) - max(d, e, f)) > max(d, e, f)
        return (((s1 + s2) > s3) and ((s1 + s3) > s2) and ((s2 + s3) > s1))
    return False

print(isLegalTriangle(1, 4, 4))