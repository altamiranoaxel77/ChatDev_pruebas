import tkinter as tk
from tkinter import filedialog
def save_file():
    '''
    Opens a file dialog to save the text content to a file with the specified file path.
    '''
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(text_area.get("1.0", tk.END))
# Create the main window
window = tk.Tk()
# Create a text area
text_area = tk.Text(window)
text_area.pack()
# Create a save button
save_button = tk.Button(window, text="Save", command=save_file)
save_button.pack()
# Run the main window loop
window.mainloop()