'''
This file contains the Snake class, which represents the snake in the game.
'''
import pygame
class Snake:
    def __init__(self, window_width, window_height):
        self.window_width = window_width
        self.window_height = window_height
        self.size = 20
        self.speed = 20
        self.direction = "right"
        self.body = [(window_width // 2, window_height // 2)]
    def update(self):
        # Move the snake
        head = self.body[0]
        x, y = head
        if self.direction == "up":
            y -= self.speed
        elif self.direction == "down":
            y += self.speed
        elif self.direction == "left":
            x -= self.speed
        elif self.direction == "right":
            x += self.speed
        self.body.insert(0, (x, y))
        self.body.pop()
    def check_collision(self, apple):
        # Check if the snake has collided with the apple
        head = self.body[0]
        if head == apple.position:
            return True
        # Check if the snake has collided with itself or the window edges
        if head in self.body[1:] or not (0 <= head[0] < self.window_width) or not (0 <= head[1] < self.window_height):
            return True
        return False
    def grow(self):
        # Make the snake grow by adding a new segment to the body
        tail = self.body[-1]
        x, y = tail
        if self.direction == "up":
            y += self.size
        elif self.direction == "down":
            y -= self.size
        elif self.direction == "left":
            x += self.size
        elif self.direction == "right":
            x -= self.size
        self.body.append((x, y))
    def reset(self):
        # Reset the snake to its initial state
        self.direction = "right"
        self.body = [(self.window_width // 2, self.window_height // 2)]
    def draw(self, window):
        # Draw the snake on the window
        for segment in self.body:
            pygame.draw.rect(window, (0, 255, 0), (segment[0], segment[1], self.size, self.size))
    def is_game_over(self):
        # Check if the game is over
        return self.check_collision(None)