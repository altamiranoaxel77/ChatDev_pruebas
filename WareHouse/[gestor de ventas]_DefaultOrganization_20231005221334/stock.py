'''
This file contains the Stock class for managing stock in the supermarket.
'''
class Stock:
    def __init__(self):
        # Code to initialize the stock class
        self.stock = {"verduras": 10}  # Initialize stock with vegetables
    def check_stock(self):
        # Code to check the stock
        print("Checking stock...")
        for product, quantity in self.stock.items():
            print(f"{product}: {quantity}")
    def update_stock(self, product, quantity):
        # Code to update the stock
        if product in self.stock:
            self.stock[product] += quantity
        else:
            self.stock[product] = quantity