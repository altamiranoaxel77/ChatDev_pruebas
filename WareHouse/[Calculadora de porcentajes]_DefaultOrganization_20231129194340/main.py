'''
This is the main file of the application. It contains the GUI implementation and handles user input and output.
'''
import tkinter as tk
from calculations import PercentageCalculator
class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Percentage Calculator")
        self.geometry("300x200")
        self.input_label = tk.Label(self, text="Enter a value:")
        self.input_label.pack()
        self.input_entry = tk.Entry(self)
        self.input_entry.pack()
        self.calculate_button = tk.Button(self, text="Calculate", command=self.calculate_percentage)
        self.calculate_button.pack()
        self.result_label = tk.Label(self, text="")
        self.result_label.pack()
    def calculate_percentage(self):
        value = self.input_entry.get()
        if value.isnumeric():
            value = float(value)
            calculator = PercentageCalculator()
            result = calculator.calculate(value)
            self.result_label.config(text=f"The result is: {result}%")
        else:
            self.result_label.config(text="Invalid input")
if __name__ == "__main__":
    app = Application()
    app.mainloop()