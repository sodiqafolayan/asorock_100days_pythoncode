"""
Modify your pcost.py program so that it uses the csv module for parsing and try running earlier examples.
"""
import csv
import sys

def totalShares(file):
    with open(file, "r") as portfolio:
        # next() will return same file but from the next line
        portfolioCSV = csv.reader(portfolio)
        portfolioheader = next(portfolioCSV)
    
        totalSharesCost = 0.0
        for row in portfolioCSV:
            try:
                shares = int(row[1])
                price = float(row[2]) # using int() gave me error: ValueError: invalid literal for int() with base 10: '32.20\n'
                totalSharesCost = totalSharesCost + (shares*price)
            except ValueError:
                print("Bad Row: ", row)
    return totalSharesCost

if len(sys.argv) == 2:
    file = sys.argv[1]
else:
    file = "Data/portfolio.csv"


print(totalShares("Data/portfolio.csv"))