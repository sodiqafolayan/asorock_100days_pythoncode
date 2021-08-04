from pprint import pprint
import csv

# Exercise 2.5: List of Dictionaries
# Take the function you wrote in Exercise 2.4 and modify to represent each stock in the
# portfolio with a dictionary instead of a tuple. In this dictionary use the field names
# of "name", "shares", and "price" to represent the different columns in the input file.

# Experiment with this new function in the same manner as you did in Exercise 2.4


def read_portfolio(filename):
    list_of_dict = []
    with open(filename) as f:
        data = csv.reader(f)
        header = next(data)
        # print(header) -> ['name', 'shares', 'price']
        # each row is now a list and items are strings
        for row in data:
            # we turn each row to dictionary and change shares and prices to int and float respectively
            holding = {header[0]: row[0], header[1]: int(row[1]), header[2]: float(row[2])}
            # appending tupples to our list
            list_of_dict.append(holding)
    return list_of_dict


portfolio = read_portfolio('Data/portfolio.csv')


# Write a function read_prices(filename) that reads a set of prices such as
# this into a dictionary where the keys of the dictionary are the stock names
# and the values in the dictionary are the stock prices.


def read_prices(filename):
    price_dict = {}
    with open(filename) as prices_file:
        prices = csv.reader(prices_file)
        for item in prices:
            try:
                price_dict[item[0]] = round(float(item[1]), 2)
            except IndexError:
                pass

    return price_dict


current_prices = read_prices("Data/prices.csv")


# Exercise 2.7: Finding out if you can retire
# Tie all of this work together by adding a few additional statements to your report.py
# program that computes gain/loss. These statements should take the list of stocks in
# Exercise 2.5 and the dictionary of prices in Exercise 2.6 and compute the current
# value of the portfolio along with the gain/loss.

# Exercise 2.9: Collecting Data
# In Exercise 2.7, you wrote a program called report.py that computed the gain/loss of a
# stock portfolio. In this exercise, you're going to start modifying it to produce a table
# like this:

# Name     Shares      Price     Change
# ---------- ---------- ---------- ----------
#        AA        100       9.22     -22.98
#       IBM         50     106.28      15.18
#       CAT        150      35.46     -47.98
#     MSFT        200      20.89     -30.34
#       GE         95      13.48     -26.89
#      MSFT         50      20.89     -44.21
#       IBM        100     106.28      35.84


def gain_loss(portfolio_value: list, latest_price: dict) -> dict:
    gain_loss_list = []
    for item in portfolio_value:
        holding = (item["name"], item["shares"], str(item["price"],
                   round(latest_price[item["name"]] - item["price"], 2))
        gain_loss_list.append(holding)

    return gain_loss_list


gain_and_loss=gain_loss(portfolio, current_prices)


def make_report(report):
    headers=('Name', 'Shares', 'Price', 'Change')
    print(
        f"{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[-1]:>10s}")
    print("-" * 10, "-" * 10, "-" * 10, "-" * 10)
    for item in report:
        print(
            f"{item[0]:>10s} {item[1]:10d} {tem[2]:10,.2f} {item[-1]:10,.2f}")
    return "Done"


print(make_report(gain_and_loss))
