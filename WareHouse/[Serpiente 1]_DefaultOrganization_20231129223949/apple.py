'''
This file contains the Apple class, which represents the apple in the game.
'''
import pygame
import random
class Apple:
    def __init__(self, window_width, window_height):
        self.window_width = window_width
        self.window_height = window_height
        self.size = 20
        self.position = self.generate_position()
    def generate_position(self):
        # Generate a random position for the apple
        x = random.randint(0, (self.window_width - self.size) // self.size) * self.size
        y = random.randint(0, (self.window_height - self.size) // self.size) * self.size
        return x, y
    def move(self):
        # Move the apple to a new random position
        self.position = self.generate_position()
    def reset(self):
        # Reset the apple to its initial position
        self.position = self.generate_position()
    def draw(self, window):
        # Draw the apple on the window
        pygame.draw.rect(window, (255, 0, 0), (self.position[0], self.position[1], self.size, self.size))