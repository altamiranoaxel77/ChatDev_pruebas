'''
Snake class for Snake Game
'''
import pygame
from pygame.locals import *
class Snake:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.size = 20
        self.head_color = (0, 255, 0)
        self.body_color = (0, 200, 0)
        self.head = [self.width // 2, self.height // 2]
        self.body = [self.head]
        self.direction = 'right'
    def reset(self):
        self.head = [self.width // 2, self.height // 2]
        self.body = [self.head]
        self.direction = 'right'
    def move(self):
        if self.direction == 'up':
            self.head[1] -= self.size
        elif self.direction == 'down':
            self.head[1] += self.size
        elif self.direction == 'left':
            self.head[0] -= self.size
        elif self.direction == 'right':
            self.head[0] += self.size
        self.body.insert(0, list(self.head))
        self.body.pop()
    def grow(self):
        self.body.append([])
    def check_collision(self, apple):
        return self.head == apple.position
    def check_self_collision(self):
        return self.head in self.body[1:]
    def check_boundary_collision(self, width, height):
        return (
            self.head[0] < 0 or
            self.head[0] >= width or
            self.head[1] < 0 or
            self.head[1] >= height
        )
    def draw(self, display):
        for segment in self.body:
            pygame.draw.rect(display, self.body_color, (segment[0], segment[1], self.size, self.size))
        pygame.draw.rect(display, self.head_color, (self.head[0], self.head[1], self.size, self.size))