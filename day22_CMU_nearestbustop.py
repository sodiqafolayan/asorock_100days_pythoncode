"""
nearestBusStop(street)
Write the function nearestBusStop(street) that takes a non-negative int street number, 
and returns the nearest bus stop to the given street, where buses stop every 8th street, 
including street 0, and ties go to the lower street, so the nearest bus stop to 12th 
street is 8th street, and the nearest bus stop to 13 street is 16th street. The function 
returns an integer, so for example, nearestBusStop(5) returns 8.
"""

def nearestBusStop(street):
    c = street % 8 # 2
    d = (street+c) % 8
    if c < d:
        return street - c
    else:
        return (8-c) + street

def assertnearestBusStop():
    assert(nearestBusStop(25) == 24)
    assert(nearestBusStop(22) == 24)
    assert(nearestBusStop(17) == 16)
    print("Passed!!!")

assertnearestBusStop()