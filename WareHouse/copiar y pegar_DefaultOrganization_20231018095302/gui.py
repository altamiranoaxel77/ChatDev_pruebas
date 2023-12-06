import tkinter as tk
class GUI:
    def __init__(self, root):
        self.root = root
        self.text_entry = tk.Entry(self.root)
        self.text_entry.pack()
        self.copy_button = tk.Button(self.root, text="Copy", command=self.copy_text)
        self.copy_button.pack()
        self.paste_entry = tk.Entry(self.root)
        self.paste_entry.pack()
    def copy_text(self):
        text = self.text_entry.get()
        self.paste_entry.delete(0, tk.END)
        self.paste_entry.insert(tk.END, text)