"""
Dave has decided to take out a 30-year fixed rate mortgage of $500,000 with Guido’s Mortgage, 
Stock Investment, and Bitcoin trading corporation. The interest rate is 5% and the monthly 
payment is $2684.11.

Here is a program that calculates the total amount that Dave will have to pay over the life of the mortgage:
"""

# mortgage.py

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0

while principal > 0:
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment

print('Total paid', total_paid)

# QUESTIONS
"""
==================================================================================================
1.  Suppose Dave pays an extra $1000/month for the first 12 months of the mortgage?
    Modify the program to incorporate this extra payment and have it print the total amount paid along 
    with the number of months required. When you run the new program, it should report a total payment 
    of 929,965.62 over 342 months.
"""
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0
extrapay = 1000
extrapay_start_month = 1
extrapay_end_month = 12


while principal > 0:
    month = month + 1
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment

    if month >= extrapay_start_month and month <= extrapay_end_month:
        principal = principal - extrapay
        total_paid = total_paid + extrapay
    

print('Total months:', month, 'Total paid', total_paid) # Total months: 342 Total paid 929965.6199999959

"""
==================================================================================================
2.  Modify the program so that extra payment information can be more generally handled. Make it so that 
    the user can set these variables:

        extra_payment_start_month = 61
        extra_payment_end_month = 108
        extra_payment = 1000
"""

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0
extrapay = 1000
extrapay_start_month = 61
extrapay_end_month = 108


while principal > 0:
    month = month + 1
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment

    if month >= extrapay_start_month and month <= extrapay_end_month:
        principal = principal - extrapay
        total_paid = total_paid + extrapay

print('Total months:', month, 'Total paid', total_paid) # Total months: 310 Total paid 880074.0999999964

"""
==================================================================================================
3. How much will Dave pay if he pays an extra $1000/month for 4 years starting in year 5 of the mortgage?
"""
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0
extrapay = 1000
months_per_year = 12
extra_payment_year_starts = 5
extrapay_start_month = months_per_year * extra_payment_year_starts
extra_pay_duration = 4
extra_pay_end_month = (extra_pay_duration * months_per_year) + extrapay_start_month
#extrapay_end_month = 12


while principal > 0:
    month = month + 1
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment

    if month >= extrapay_start_month and month <= extra_pay_end_month:
        principal = principal - extrapay
        total_paid = total_paid + extrapay
    

print('Total months:', month, 'Total paid', total_paid)

"""
==================================================================================================
4. Modify the program to print out a table showing the month, total paid so far, and the remaining principal. 
   The output should look something like this:
                1 2684.11 499399.22
                2 5368.22 498795.94
                3 8052.33 498190.15
                4 10736.44 497581.83
                5 13420.55 496970.98
                ...
                308 874705.88 3478.83
                309 877389.99 809.21
                310 880074.1 -1871.53
                Total paid 880074.1
                Months 310
"""
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0
extrapay = 1000
months_per_year = 12
extra_payment_year_starts = 5
extrapay_start_month = months_per_year * extra_payment_year_starts
extra_pay_duration = 4
extra_pay_end_month = (extra_pay_duration * months_per_year) + extrapay_start_month
#extrapay_end_month = 12


while principal > 0:
    month = month + 1
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment

    if month >= extrapay_start_month and month <= extra_pay_end_month:
        principal = principal - extrapay
        total_paid = total_paid + extrapay
    print(month, total_paid, principal)
    

print('Total months:', month, 'Total paid', total_paid)

"""
==================================================================================================
5. While you’re at it, fix the program to correct for the overpayment that occurs in the last month.

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0
extrapay = 1000
months_per_year = 12
extra_payment_year_starts = 5
extrapay_start_month = months_per_year * extra_payment_year_starts
extra_pay_duration = 4
extra_pay_end_month = (extra_pay_duration * months_per_year) + extrapay_start_month
#extrapay_end_month = 12

"""
while principal > 0:
    if principal <= payment:
        month = month + 1
        principal = principal - principal
    else:
        month = month + 1
        principal = principal * (1+rate/12) - payment
        total_paid = total_paid + payment

        if month >= extrapay_start_month and month <= extra_pay_end_month:
            principal = principal - extrapay
            total_paid = total_paid + extrapay
    print(month, total_paid, principal)


print('Total months:', month, 'Total paid', total_paid)

