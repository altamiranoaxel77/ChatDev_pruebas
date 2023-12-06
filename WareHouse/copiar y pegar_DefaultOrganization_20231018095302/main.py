'''
This is the main file of the application.
'''
import tkinter as tk
from gui import GUI
def main():
    root = tk.Tk()
    app = GUI(root)
    root.mainloop()
if __name__ == "__main__":
    main()