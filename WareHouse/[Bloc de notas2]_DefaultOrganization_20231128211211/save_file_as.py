'''
This method saves the file with a specified file path and ensures it has the ".txt" extension.
'''
import tkinter as tk
from tkinter import filedialog
import os
from tkinter import messagebox
def save_file_as(self):
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if file_path:
        base_name, extension = os.path.splitext(file_path)
        if extension != ".txt":
            messagebox.showerror("Invalid File Extension", "Please enter a file path with the '.txt' extension.")
            return
        content = self.text_area.get(1.0, tk.END)
        confirmation = messagebox.askyesno("Confirmation", "Are you sure you want to save the file?")
        if confirmation:
            with open(file_path, "w") as file:
                file.write(content)