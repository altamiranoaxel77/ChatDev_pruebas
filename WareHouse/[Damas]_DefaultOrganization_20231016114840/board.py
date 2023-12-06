'''
This file contains the Board class that manages the game board.
'''
class Board:
    def __init__(self):
        self.board = [
            [" ", "b", " ", "b", " ", "b", " ", "b"],
            ["b", " ", "b", " ", "b", " ", "b", " "],
            [" ", "b", " ", "b", " ", "b", " ", "b"],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            ["w", " ", "w", " ", "w", " ", "w", " "],
            [" ", "w", " ", "w", " ", "w", " ", "w"],
            ["w", " ", "w", " ", "w", " ", "w", " "]
        ]
    def display(self):
        print("   0 1 2 3 4 5 6 7")
        for i, row in enumerate(self.board):
            print(f"{i}  {' '.join(row)}")
    def is_game_over(self):
        # Check if any player has no more pieces
        white_pieces = 0
        black_pieces = 0
        for row in self.board:
            for piece in row:
                if piece == "w":
                    white_pieces += 1
                elif piece == "b":
                    black_pieces += 1
        return white_pieces == 0 or black_pieces == 0
    def make_move(self, move):
        start_row, start_col = move.start_pos
        end_row, end_col = move.end_pos
        self.board[end_row][end_col] = self.board[start_row][start_col]
        self.board[start_row][start_col] = " "
    def get_winner(self):
        white_pieces = 0
        black_pieces = 0
        for row in self.board:
            for piece in row:
                if piece == "w":
                    white_pieces += 1
                elif piece == "b":
                    black_pieces += 1
        if white_pieces > black_pieces:
            return Player("Player 1", "white")
        elif black_pieces > white_pieces:
            return Player("Player 2", "black")
        else:
            return None