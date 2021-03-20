import csv
from pprint import pprint

"""
Take the function you wrote in Exercise 2.4 and modify to represent each stock in 
the portfolio with a dictionary instead of a tuple. In this dictionary use the 
field names of "name", "shares", and "price" to represent the different columns 
in the input file.
"""


def read_portfolio(filename):
    listOfDict = []
    with open(filename, "r") as files: # files b=must be first opened before we can perform operation on it
        rows = csv.reader(files) # csv.reader() makes reading into csv file easier to work with
        header = next(rows) # this returns the file starting from the second line since it has header
        for row in rows:

            tempvalue = {"name": row[0], "shares": int(row[1]), "price": float(row[2])} # This is packing each row as a tuple
            listOfDict.append(tempvalue)
        
        return listOfDict # Return statrement is inside with() before closing the file


pprint(read_portfolio('Data/portfolio.csv'))



    





