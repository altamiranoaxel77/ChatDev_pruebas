'''
This file contains the Chessboard class which represents the game board.
'''
import tkinter as tk
from piece import Piece
class Chessboard(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.create_board()
    def create_board(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        for row in range(8):
            for col in range(8):
                piece = Piece(row, col)
                self.board[row][col] = piece
                piece.grid(row=row, column=col)
    def move_piece(self, piece, new_row, new_col):
        current_row, current_col = piece.row, piece.col
        if self.is_valid_move(piece, new_row, new_col):
            self.board[current_row][current_col] = None
            self.board[new_row][new_col] = piece
            piece.move(new_row, new_col)
    def get_piece(self, row, col):
        return self.board[row][col]
    def is_valid_move(self, piece, new_row, new_col):
        current_row, current_col = piece.row, piece.col
        # Check if the move is within the bounds of the chessboard
        if new_row < 0 or new_row >= 8 or new_col < 0 or new_col >= 8:
            return False
        # Check if there is a piece blocking the path
        if self.board[new_row][new_col] is not None:
            return False
        # Implement the logic to check if the move is allowed for the specific piece type
        # You can add specific logic for each piece type (e.g., pawn, rook, etc.) here
        return True