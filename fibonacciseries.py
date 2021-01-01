# This accepts input from a user which will be converted to Fibonacci series
n = int(input("Enter a number: "))

# first and second stores the variable as the starting point of our series
# We created these variables because the series can only start after adding
# two preceeding numbers. Hence, 0 and 1. This could be any number too. However,
# since i used the range() function, it will make sense to start as stated
first = 0
second = 1

# This is simply saying "for every number in the range of the number inputed by the user as requested above"
for i in range(n):
    # This prints the value of first which is 0.
    print(first)
    # Here we store the value of first (remeber it is 0) inside of temp
    # so at this point, temp == 0
    temp = first
    # first = second is just like writing first = 1, because second in our code == 1 for now
    first = second
    # This implies 0 + 1
    second = temp+first

# So this iteration goes on until range(n) and the value for the variables increment.
# I hope this isn't confusing. I can explain better if not clear
# just let me know
