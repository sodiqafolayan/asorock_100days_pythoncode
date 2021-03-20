import csv
from pprint import pprint

"""
Write a function read_prices(filename) that reads a set of prices such as this 
into a dictionary where the keys of the dictionary are the stock names and the 
values in the dictionary are the stock prices. To do this, start with an empty 
dictionary and start inserting values into it just as you did above. However, 
you are reading the values from a file now.
We’ll use this data structure to quickly lookup the price of a given stock name.
A few little tips that you’ll need for this part. First, make sure you use the 
csv module just as you did before—there’s no need to reinvent the wheel here.
"""

 
def read_prices(filename):
    reportDict = {}
    with open(filename, "r") as files:
        rows = csv.reader(files) 
        for row in rows:
            reportDict.update({row[0]: float(row[1])})
        
        return reportDict # Return statrement is inside with() before closing the file


pprint(read_prices('Data/prices.csv'))

    





