'''
This file contains the Food class, which represents the food that the snake can eat.
'''
import pygame
import random
class Food:
    def __init__(self, snake_block_size, screen_width, screen_height):
        self.x = random.randint(0, screen_width - snake_block_size) // snake_block_size * snake_block_size
        self.y = random.randint(0, screen_height - snake_block_size) // snake_block_size * snake_block_size
    def draw(self):
        pygame.draw.rect(screen, white, [self.x, self.y, snake_block_size, snake_block_size])