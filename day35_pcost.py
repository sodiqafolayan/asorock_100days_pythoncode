"""
The columns in portfolio.csv correspond to the stock name, number of shares, 
and purchase price of a single stock holding. Write a program called pcost.py 
that opens this file, reads all lines, and calculates how much it cost to 
purchase all of the shares in the portfolio.

"""

with open("Data/portfolio.csv", "r") as portfolio:
    # next() will return same file but from the next line
    portfolioHeader = next(portfolio).split(',')
    # This is a placeholder for the current totalSharesCost
    totalSharesCost = 0.0
    for row in portfolio:
        # This turns each row into a list
        row = row.split(',')
        # I already know the data i need are index 1 and 2
        shares = int(row[1])
        price = float(row[2]) # using int() gave me error: ValueError: invalid literal for int() with base 10: '32.20\n'
        totalSharesCost = totalSharesCost + (shares*price)

print(totalSharesCost)
