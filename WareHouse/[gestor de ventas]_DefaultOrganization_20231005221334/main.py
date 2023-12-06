'''
This is the main file of the supermarket sales management system.
'''
from tkinter import Tk, Label, Button
from employees import Employees
from sales import Sales
from stock import Stock
from prices import Prices
from visual import Visual
class SalesManager:
    def __init__(self):
        self.window = Tk()
        self.window.title("Supermarket Sales Management System")
        self.title_label = Label(self.window, text="Welcome to the Supermarket Sales Management System")
        self.title_label.pack()
        self.sales_button = Button(self.window, text="Sales", command=self.open_sales)
        self.sales_button.pack()
        self.stock_button = Button(self.window, text="Check Stock", command=self.open_stock)
        self.stock_button.pack()
        self.price_button = Button(self.window, text="Check Prices", command=self.open_prices)
        self.price_button.pack()
        self.employee_button = Button(self.window, text="Register Employees", command=self.open_employees)
        self.employee_button.pack()
        self.image_button = Button(self.window, text="Display Product Image", command=self.display_image)
        self.image_button.pack()
        self.window.mainloop()
    def open_sales(self):
        sales = Sales()
        sales.make_sale()  # Call the make_sale method
    def open_stock(self):
        stock = Stock()
        stock.check_stock()  # Call the check_stock method
        # Code to open the stock window
    def open_prices(self):
        prices = Prices()
        prices.check_prices()  # Call the check_prices method
        # Code to open the prices window
    def open_employees(self):
        employees = Employees()
        employees.register_employee()
    def display_image(self):
        visual = Visual()
        visual.display_product_image("verduras")  # Replace "verduras" with the actual product name
if __name__ == "__main__":
    sales_manager = SalesManager()