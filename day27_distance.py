from math import sqrt

"""
Write the function distance(x1, y1, x2, y2) that takes four int or float 
values x1, y1, x2, y2 that represent the two points (x1, y1) and (x2, y2), 
and returns the distance between those points as a float.

"""
# Option 1: Verbose
def distance(x1, y1, x2, y2):
    # Get change in x axis
    change_in_x = x2 - x1 
    print(change_in_x)
    # Square the difference
    change_in_x_squared = change_in_x ** 2
    print(change_in_x_squared)
    # Get change in y axis
    change_in_y = y2 - y1 
    print(change_in_y)
    # Square the difference 
    change_in_y_squared = change_in_y ** 2
    print(change_in_y_squared)
    # Add change_in_x_squared and change_in_y_squared
    sum_change_x_y_squared = change_in_x_squared + change_in_y_squared
    print(sum_change_x_y_squared)
    # Get the square root of sum_change_x_y_squared
    square_root = sqrt(change_in_x_squared + change_in_y_squared)
    print(square_root)
    # Return the int value
    return int(square_root)



# option 2: Single line code
def distance2(x1, y1, x2, y2):
    return int(sqrt((x2 - x1)**2 + (y2 - y1)**2))



#print(distance(0, 0, 3, 4))
#print(distance(-1, -2, 3, 1))
#print(distance(-.5, .5, .5, -.5))
print(distance(5, 3, 7, 9))

#print(distance2(0, 0, 3, 4))
#print(distance2(-1, -2, 3, 1))
#print(distance2(-.5, .5, .5, -.5))
print(distance2(5, 3, 7, 9))
   