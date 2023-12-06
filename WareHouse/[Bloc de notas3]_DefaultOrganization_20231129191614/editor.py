import tkinter as tk
from tkinter import filedialog
def save_file(file_path, text_content):
    '''
    Saves the text content to a file with the specified file path.
    '''
    from tkinter import filedialog
    with open(file_path, "w") as file:
        file.write(text_content)
    return True