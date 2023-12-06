'''
This is the main file of the book management application. It contains the GUI implementation and handles user interactions.
'''
import tkinter as tk
from tkinter import messagebox
import json
class Book:
    def __init__(self, name, author, edition):
        """
        Initializes a Book object with the given name, author, and edition.
        """
        self.name = name
        self.author = author
        self.edition = edition
class BookManager:
    def __init__(self):
        self.books = []
    def add_book(self, name, author, edition):
        """
        Adds a new book to the book manager with the given name, author, and edition.
        """
        book = Book(name, author, edition)
        self.books.append(book)
    def save_books(self):
        """
        Saves the list of books to a JSON file.
        """
        with open('books.json', 'w') as file:
            json.dump([book.__dict__ for book in self.books], file)
    def load_books(self):
        """
        Loads the list of books from a JSON file.
        """
        try:
            with open('books.json', 'r') as file:
                data = json.load(file)
                self.books = [Book(book['name'], book['author'], book['edition']) for book in data]
        except FileNotFoundError:
            self.books = []
    def find_book(self, name):
        """
        Finds a book with the given name in the list of books.
        Returns the book if found, None otherwise.
        """
        for book in self.books:
            if book.name == name:
                return book
        return None
class BookManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Book Manager")
        self.book_manager = BookManager()
        self.book_manager.load_books()
        self.name_label = tk.Label(root, text="Name:")
        self.name_label.pack()
        self.name_entry = tk.Entry(root)
        self.name_entry.pack()
        self.author_label = tk.Label(root, text="Author:")
        self.author_label.pack()
        self.author_entry = tk.Entry(root)
        self.author_entry.pack()
        self.edition_label = tk.Label(root, text="Edition:")
        self.edition_label.pack()
        self.edition_entry = tk.Entry(root)
        self.edition_entry.pack()
        self.add_button = tk.Button(root, text="Add Book", command=self.add_book)
        self.add_button.pack()
        self.search_label = tk.Label(root, text="Search by Name:")
        self.search_label.pack()
        self.search_entry = tk.Entry(root)
        self.search_entry.pack()
        self.search_button = tk.Button(root, text="Search", command=self.search_book)
        self.search_button.pack()
    def add_book(self):
        """
        Adds a new book to the book manager when the "Add Book" button is clicked.
        """
        name = self.name_entry.get()
        author = self.author_entry.get()
        edition = self.edition_entry.get()
        if name and author and edition:
            self.book_manager.add_book(name, author, edition)
            self.book_manager.save_books()
            messagebox.showinfo("Success", "Book added successfully.")
            self.name_entry.delete(0, tk.END)
            self.author_entry.delete(0, tk.END)
            self.edition_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please fill in all fields.")
    def search_book(self):
        """
        Searches for a book by name when the "Search" button is clicked.
        """
        name = self.search_entry.get()
        if name:
            book = self.book_manager.find_book(name)
            if book:
                messagebox.showinfo("Book Found", f"Name: {book.name}\nAuthor: {book.author}\nEdition: {book.edition}")
            else:
                messagebox.showinfo("Book Not Found", "No book found with the given name.")
        else:
            messagebox.showerror("Error", "Please enter a book name.")
root = tk.Tk()
app = BookManagerApp(root)
root.mainloop()