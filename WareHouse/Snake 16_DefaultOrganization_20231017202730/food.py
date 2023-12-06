'''
This file contains the Food class that represents the food in the game.
'''
import pygame
import random
class Food:
    def __init__(self, window_width, window_height):
        self.window_width = window_width
        self.window_height = window_height
        self.size = 20
        self.rect = pygame.Rect(0, 0, self.size, self.size)
        self.generate()
    def render(self, window):
        pygame.draw.rect(window, (255, 0, 0), self.rect)
    def generate(self):
        x = random.randint(0, self.window_width // self.size - 1) * self.size
        y = random.randint(0, self.window_height // self.size - 1) * self.size
        self.rect.topleft = (x, y)