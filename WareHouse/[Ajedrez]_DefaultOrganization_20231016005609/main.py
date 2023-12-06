'''
This is the main file of the chess game.
'''
import tkinter as tk
from chessboard import *
class ChessGame:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Chess Game")
        self.chessboard = Chessboard(self.root)
        self.chessboard.pack()
        self.root.mainloop()
if __name__ == "__main__":
    game = ChessGame()