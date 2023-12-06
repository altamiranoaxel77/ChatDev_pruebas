'''
This is the main file of the application. It contains the GUI implementation and handles user input and output.
'''
import tkinter as tk
from percentage_calculator import calculate_percentage
class PercentageCalculatorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Percentage Calculator")
        self.geometry("400x200")
        self.value_label = tk.Label(self, text="Value:")
        self.value_label.pack()
        self.value_entry = tk.Entry(self)
        self.value_entry.pack()
        self.percentage_label = tk.Label(self, text="Percentage:")
        self.percentage_label.pack()
        self.percentage_entry = tk.Entry(self)
        self.percentage_entry.pack()
        self.calculate_button = tk.Button(self, text="Calculate", command=self.calculate_percentage)
        self.calculate_button.pack()
        self.result_label = tk.Label(self, text="")
        self.result_label.pack()
    def calculate_percentage(self):
        try:
            value = float(self.value_entry.get())
            percentage = float(self.percentage_entry.get())
            result = calculate_percentage(value, percentage)
            if result is not None:
                self.result_label.config(text=f"Result: {result}")
            else:
                self.result_label.config(text="Invalid input")
        except ValueError:
            self.result_label.config(text="Invalid input")
if __name__ == "__main__":
    app = PercentageCalculatorApp()
    app.mainloop()