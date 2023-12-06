'''
This is the main file of the calculator application.
'''
import tkinter as tk
from calculator import Calculator
def main():
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
if __name__ == "__main__":
    main()