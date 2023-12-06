'''
This file contains the Game class that manages the snake game.
'''
import pygame
from snake import Snake
from food import Food
class Game:
    def __init__(self, window_width, window_height):
        self.window_width = window_width
        self.window_height = window_height
        self.snake = Snake(window_width, window_height)
        self.food = Food(window_width, window_height)
    def update(self):
        self.snake.update()
        self.check_collision()
    def render(self, window):
        window.fill((0, 0, 0))
        self.snake.render(window)
        self.food.render(window)
    def check_collision(self):
        if self.snake.head.colliderect(self.food.rect):
            self.snake.grow()
            self.food.generate()
        if self.snake.is_colliding():
            self.snake.reset()
        if self.snake.is_colliding():  # Perform collision check again after the snake grows
            self.snake.reset()
    def reset(self):
        self.snake.reset()
        self.food.generate()