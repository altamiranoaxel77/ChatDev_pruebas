'''
Apple class for Snake Game
'''
import pygame
import random
class Apple:
    def __init__(self, grid_width, grid_height, size):
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.size = size
        self.position = self.generate_new_position(grid_width, grid_height)
    def generate_new_position(self, grid_width, grid_height):
        x = random.randint(0, grid_width - 1) * self.size
        y = random.randint(0, grid_height - 1) * self.size
        self.position = [x, y]
    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), (self.position[0], self.position[1], self.size, self.size))