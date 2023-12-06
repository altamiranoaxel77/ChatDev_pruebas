'''
This is the main file of the application. It initializes the GUI and handles user interactions.
'''
import tkinter as tk
from tkinter import filedialog
from file_operations import open_file, save_file
class NotepadApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Notepad")
        self.text_area = tk.Text(self.root)
        self.text_area.pack(fill=tk.BOTH, expand=True)
        self.menu_bar = tk.Menu(self.root)
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.root.quit)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.root.config(menu=self.menu_bar)
    def open_file(self):
        file_content = open_file()
        if file_content:
            self.text_area.delete(1.0, tk.END)
            self.text_area.insert(tk.END, file_content)
    def save_file(self):
        content = self.text_area.get(1.0, tk.END)
        save_file(content)
    def run(self):
        self.root.mainloop()
if __name__ == "__main__":
    app = NotepadApp()
    app.run()