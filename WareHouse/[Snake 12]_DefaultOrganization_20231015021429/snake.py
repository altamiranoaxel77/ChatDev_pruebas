'''
This file contains the Snake class which represents the snake in the game.
'''
import pygame
class Snake:
    def __init__(self, window_width, window_height):
        self.window_width = window_width
        self.window_height = window_height
        self.x = window_width // 2
        self.y = window_height // 2
        self.size = 20
        self.speed = 20
        self.direction = "RIGHT"
        self.body = [(self.x, self.y)]
    def update(self):
        if self.direction == "RIGHT":
            self.x += self.speed
        elif self.direction == "LEFT":
            self.x -= self.speed
        elif self.direction == "UP":
            self.y -= self.speed
        elif self.direction == "DOWN":
            self.y += self.speed
        self.body.append((self.x, self.y))
        if len(self.body) > 1:
            del self.body[0]
    def check_collision(self, food):
        if self.x == food.x and self.y == food.y:
            food.generate_new_position()
            self.body.append((self.x, self.y))
    def draw(self, window):
        for segment in self.body:
            pygame.draw.rect(window, (0, 255, 0), (segment[0], segment[1], self.size, self.size))