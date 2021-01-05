
# Write a simple python function that accepts a list as an arguemnent and returns
# a new list of elements less than any input for the user

n = [111, 222, 333, 444, 555, 200, 34]


def smaller_than_x(a):
    x = int(input("Enter a number"))
    b = []
    for i in a:
        if i < x:
            b.append(a)
    return b


print(smaller_than_x(n))
