'''
This file contains the Player class that represents a player in the game.
'''
class Player:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    def get_move(self):
        start_pos = input("Enter the starting position of your piece (row col): ")
        end_pos = input("Enter the ending position of your piece (row col): ")
        return Move(tuple(map(int, start_pos.split())), tuple(map(int, end_pos.split())))
class Move:
    def __init__(self, start_pos, end_pos):
        self.start_pos = start_pos
        self.end_pos = end_pos