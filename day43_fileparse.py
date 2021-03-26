import csv
# fileparse.py
# This function reads a CSV file into a list of dictionaries while hiding the details of opening the file, 
# wrapping it with the csv module, ignoring blank lines, and so forth
# Exercise 3.3
def parse_csv(filename, types=None):
    '''
    Parse a CSV file into a list of records
    '''
    with open(filename) as f:
        rows = csv.reader(f)

        # Read the file headers
        headers = next(rows)

        records = []
        for row in rows:

            if type:
                row[0] = types[0](row[0])
                row[1] = types[1](row[1])
                row[2] = types[2](row[2])

            if not row:    # Skip rows with no data
                continue
            record = dict(zip(headers, row))
            records.append(record)

    return records


portfolio = parse_csv('Data/portfolio.csv', types=[str, int, float])
print(portfolio)

print("+++++++++++++++++++++++++++++++++++++++++++++++++")
"""
In many cases, you’re only interested in selected columns from a CSV file, not all of the data. 
Modify the parse_csv() function so that it optionally allows user-specified columns to be picked 
out as follows:
"""
def parse_csv2(filename, select=None, types=[str, int]):
    '''
    Parse a CSV file into a list of records
    '''
    with open(filename) as f:
        rows = csv.reader(f)

        # Read the file headers
        headers = next(rows)

        # If a column selector was given, find indices of the specified columns.
        # Also narrow the set of headers used for resulting dictionaries
        if select:
            indices = [headers.index(colname) for colname in select] # This gets the index/indices of the items supplied in "select"
            print("indices", indices)
            headers = select
        else:
            indices = []

        records = []
        for row in rows:
            if not row:    # Skip rows with no data
                continue
            # Filter the row if specific columns were selected
            if indices:
                row = [ row[index] for index in indices ]


            # Make a dictionary
            record = dict(zip(headers, row))
            records.append(record)

    return records

shares_held = parse_csv2('Data/portfolio.csv', select=['name','shares'], types=[str, int])
print(shares_held)