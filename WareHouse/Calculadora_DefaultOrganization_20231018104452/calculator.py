import tkinter as tk
#from math import eval
class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.entry = tk.Entry(self.root, width=30)
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        buttons = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "=", "+"
        ]
        row = 1
        col = 0
        for button in buttons:
            tk.Button(self.root, text=button, width=5, command=lambda button=button: self.button_click(button)).grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col > 3:
                col = 0
                row += 1
    def button_click(self, button):
        current = self.entry.get()
        if button == "=":
            try:
                result = eval(current)
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, f"Error: {str(e)}")
        else:
            self.entry.insert(tk.END, button)