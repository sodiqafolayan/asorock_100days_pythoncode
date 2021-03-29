"""
Create a file called stock.py and define a class Stock that represents a single holding of stock. 
Have the instances of Stock have name, shares, and price attributes
"""

class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    def sell(self, qty):
        return self.shares - qty


a = Stock('GOOG',100,490.10)
b = Stock('AAPL', 50, 122.34)
c = Stock('IBM', 75, 91.75)
