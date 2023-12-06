'''
This file contains the Game class that manages the game logic.
'''
from board import Board
from player import Player, Move
class Game:
    def __init__(self):
        self.board = Board()
        self.player1 = Player("Player 1", "white")
        self.player2 = Player("Player 2", "black")
        self.current_player = self.player1
    def start(self):
        while not self.board.is_game_over():
            self.board.display()
            print(f"It's {self.current_player.name}'s turn.")
            move = self.current_player.get_move()
            self.board.make_move(move)
            self.current_player = self.player2 if self.current_player == self.player1 else self.player1
        self.board.display()
        winner = self.board.get_winner()
        if winner:
            print(f"{winner.name} wins!")
        else:
            print("It's a draw!")
class Move:
    def __init__(self, start_pos, end_pos):
        self.start_pos = start_pos
        self.end_pos = end_pos