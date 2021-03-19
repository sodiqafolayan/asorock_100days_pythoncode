# mortgage.py
"""
Dave has decided to take out a 30-year fixed rate mortgage of $500,000 with Guido’s 
Mortgage, Stock Investment, and Bitcoin trading corporation. The interest rate is 5% 
and the monthly payment is $2684.11.
Here is a program that calculates the total amount that Dave will have to pay over the life of the mortgage:

# N M SOLUTION

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0

while principal > 0:
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment

print('Total paid', total_paid)



Suppose Dave pays an extra $1000/month for the first 12 months of the mortgage?
Modify the program to incorporate this extra payment and have it print the total amount paid 
along with the number of months required.
When you run the new program, it should report a total payment of 929,965.62 over 342 months

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0
extra_payment = 1000.0
extra_payment_start_month = 1 # this can be changed to another start date
extra_payment_end_month = 12 # this can be changed to another end date

while principal > 0:
    month = month + 1
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment
    # Soon as the above code run, the below code checks month, if condition in the if statement below
    # returns tru, it will run the code below, then go back up to run the above code. As you will notice,
    # month is only increased above and not below. Hence, the extra payment month need not be counted separately
    if month >= extra_payment_start_month and month <= extra_payment_end_month:
        principal = principal - extra_payment
        total_paid = total_paid + extra_payment
    print(month, round(total_paid,2), round(principal, 2))
    
print('Total paid', round(total_paid, 2))
print('Months', month)
"""


# How much will Dave pay if he pays an extra $1000/month for 4 years starting in year 5 of the mortgage?
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0
month_per_year = 12
extra_payment_year_duration = 4
extra_payment_year_start = 5
extra_payment_end_year = extra_payment_year_start + extra_payment_year_duration
extra_payment = 1000.0
extra_payment_start_month = 1 # this can be changed to another start date
extra_payment_end_month = 12 # this can be changed to another end date

while principal > 0:
    month = month + 1
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment
    

    # Soon as the above code run, the below code checks month, if condition in the if statement below
    # returns tru, it will run the code below, then go back up to run the above code. As you will notice,
    # month is only increased above and not below. Hence, the extra payment month need not be counted separately
    if month >= (extra_payment_year_start * month_per_year) and month <= (extra_payment_end_year * month_per_year):
        principal = principal - extra_payment
        total_paid = total_paid + extra_payment
        print(month, round(total_paid,2), round(principal, 2))
    
print('Total paid', round(total_paid, 2))
print('Months', month)

# Modify the program to print out a table showing the month, total paid so far, and the remaining principal