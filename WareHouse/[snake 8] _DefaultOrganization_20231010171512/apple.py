'''
Apple class for Snake Game
'''
import pygame
import random
from pygame.locals import *
class Apple:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.size = 20
        self.color = (255, 0, 0)
        self.position = [self.size * random.randint(0, (self.width - self.size) // self.size),
                         self.size * random.randint(0, (self.height - self.size) // self.size)]
    def generate(self):
        self.position = [self.size * random.randint(0, (self.width - self.size) // self.size),
                         self.size * random.randint(0, (self.height - self.size) // self.size)]
    def draw(self, display):
        pygame.draw.rect(display, self.color, (self.position[0], self.position[1], self.size, self.size))