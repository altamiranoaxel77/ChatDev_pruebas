'''
This file contains the Snake class, which represents the snake in the game.
'''
import pygame
class Snake:
    def __init__(self, x, y, snake_block_size):
        self.x = x
        self.y = y
        self.x_change = 0
        self.y_change = 0
        self.length = 1
        self.snake_list = []
        self.snake_block_size = snake_block_size
    def move(self):
        self.x += self.x_change
        self.y += self.y_change
    def change_direction(self, direction):
        if direction == "LEFT":
            self.x_change = -self.snake_block_size
            self.y_change = 0
        elif direction == "RIGHT":
            self.x_change = self.snake_block_size
            self.y_change = 0
        elif direction == "UP":
            self.y_change = -self.snake_block_size
            self.x_change = 0
        elif direction == "DOWN":
            self.y_change = self.snake_block_size
            self.x_change = 0
    def draw(self):
        for x in self.snake_list:
            pygame.draw.rect(screen, green, [x[0], x[1], self.snake_block_size, self.snake_block_size])