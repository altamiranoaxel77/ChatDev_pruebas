'''
This is the main file of the text editor application.
'''
import tkinter as tk
from tkinter import filedialog
import os
from tkinter import messagebox
class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Text Editor")
        self.text_area = tk.Text(self.root)
        self.text_area.pack()
        self.create_menu()
    def create_menu(self):
        menu_bar = tk.Menu(self.root)
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_command(label="Save As", command=self.save_file_as)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        menu_bar.add_cascade(label="File", menu=file_menu)
        self.root.config(menu=menu_bar)
    def new_file(self):
        self.text_area.delete(1.0, tk.END)
    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "r") as file:
                content = file.read()
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, content)
    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if file_path:
            content = self.text_area.get(1.0, tk.END)
            with open(file_path, "w") as file:
                file.write(content)
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
if __name__ == "__main__":
    root = tk.Tk()
    text_editor = TextEditor(root)
    root.mainloop()