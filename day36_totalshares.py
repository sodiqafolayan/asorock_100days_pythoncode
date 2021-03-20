"""
Modify your pcost.py program so that it uses the csv module for parsing and try running earlier examples.
"""
import csv

def totalShares(file):
    with open(file, "r") as portfolio:
        portfolioCSV = csv.reader(portfolio)
        # next() will return same file but from the next line
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
    

print(totalShares("Data/missing.csv"))