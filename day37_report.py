import csv

"""
report.py
Exercise 2.4
Using this code as a rough guide, create a new file report.py. In that file, define a function 
read_portfolio(filename) that opens a given portfolio file and reads it into a list of tuples. 
To do this, you’re going to make a few minor modifications to the above code.
First, instead of defining total_cost = 0, you’ll make a variable that’s initially set to an empty list. 

Next, instead of totaling up the cost, you’ll turn each row into a tuple exactly 
as you just did in the last exercise and append it to this list

Finally, you’ll return the resulting portfolio list

"""


def read_portfolio(filename):
    listOfTuples = []
    with open(filename, "r") as files: # files b=must be first opened before we can perform operation on it
        rows = csv.reader(files) # csv.reader() makes reading into csv file easier to work with
        header = next(rows) # this returns the file starting from the second line since it has header
        for row in rows:
            tempvalue = (row[0], int(row[1]), float(row[2])) # This is packing each row as a tuple
            listOfTuples.append(tempvalue)
        
        return listOfTuples # Return statrement is inside with() before closing the file


print(read_portfolio('Data/portfolio.csv'))

# [('AA', 100, 32.2), ('IBM', 50, 91.1), ('CAT', 150, 83.44), ('MSFT', 200, 51.23), ('GE', 95, 40.37), ('MSFT', 50, 65.1), ('IBM', 100, 70.44)]





