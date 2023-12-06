'''
This file contains the Snake class and related functions.
'''
import pygame
class Snake:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.x_change = 0
        self.y_change = 0
        self.snake_list = []
        self.snake_length = 1
    def move(self):
        self.x += self.x_change
        self.y += self.y_change
    def draw(self, window, snake_block_size, green):
        for x in self.snake_list:
            pygame.draw.rect(window, green, [x[0], x[1], snake_block_size, snake_block_size])
    def check_collision(self, window_width, window_height):
        return self.x >= window_width or self.x < 0 or self.y >= window_height or self.y < 0
    def check_self_collision(self):
        for segment in self.snake_list[1:]:
            if segment == [self.x, self.y]:
                return True
        return False
    def update_snake_list(self):
        self.snake_list.append([self.x, self.y])
        if len(self.snake_list) > self.snake_length:
            del self.snake_list[0]
    def increase_length(self):
        self.snake_length += 1
    def set_direction(self, x_change, y_change):
        self.x_change = x_change
        self.y_change = y_change