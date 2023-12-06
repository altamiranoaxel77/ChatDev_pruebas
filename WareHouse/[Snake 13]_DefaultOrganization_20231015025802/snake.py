'''
This file contains the Snake class and its methods.
'''
import pygame
import sys
class Snake:
    def __init__(self):
        self.pos = [[100, 50], [90, 50], [80, 50]]
        self.direction = "RIGHT"
    def move(self):
        if self.direction == "UP":
            self.pos[0][1] -= 20
        elif self.direction == "DOWN":
            self.pos[0][1] += 20
        elif self.direction == "LEFT":
            self.pos[0][0] -= 20
        elif self.direction == "RIGHT":
            self.pos[0][0] += 20
    def change_direction(self, new_direction):
        if new_direction == "UP" and self.direction != "DOWN":
            self.direction = new_direction
        elif new_direction == "DOWN" and self.direction != "UP":
            self.direction = new_direction
        elif new_direction == "LEFT" and self.direction != "RIGHT":
            self.direction = new_direction
        elif new_direction == "RIGHT" and self.direction != "LEFT":
            self.direction = new_direction
    def check_collision(self):
        if self.pos[0][0] < 0 or self.pos[0][0] >= 800 or self.pos[0][1] < 0 or self.pos[0][1] >= 600:
            pygame.quit()
            sys.exit()