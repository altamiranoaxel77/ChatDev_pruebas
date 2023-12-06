'''
Snake Game - Apple Class
'''
import pygame
import random
class Apple:
    def __init__(self, window_width, window_height, color):
        self.window_width = window_width
        self.window_height = window_height
        self.color = color
        self.size = 20
        self.move()
    def move(self):
        self.x = random.randint(0, (self.window_width - self.size) // self.size) * self.size
        self.y = random.randint(0, (self.window_height - self.size) // self.size) * self.size
        return self.x, self.y
    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.size, self.size))