'''
Snake Game - Snake Class
'''
import pygame
class Snake:
    def __init__(self, window_width, window_height, color):
        self.window_width = window_width
        self.window_height = window_height
        self.color = color
        self.size = 20
        self.x = window_width // 2
        self.y = window_height // 2
        self.direction = "RIGHT"
        self.body = [(self.x, self.y)]
    def change_direction(self, direction):
        if direction == "UP" and self.direction != "DOWN":
            self.direction = "UP"
        elif direction == "DOWN" and self.direction != "UP":
            self.direction = "DOWN"
        elif direction == "LEFT" and self.direction != "RIGHT":
            self.direction = "LEFT"
        elif direction == "RIGHT" and self.direction != "LEFT":
            self.direction = "RIGHT"
    def move(self):
        if self.direction == "UP":
            self.y -= self.size
        elif self.direction == "DOWN":
            self.y += self.size
        elif self.direction == "LEFT":
            self.x -= self.size
        elif self.direction == "RIGHT":
            self.x += self.size
        self.body.insert(0, (self.x, self.y))
        self.body.pop()
    def check_collision(self, apple):
        if self.x == apple.x and self.y == apple.y:
            self.body.append((self.x, self.y))
            self.x, self.y = apple.move()  # Update the head position
            # Check if the new position of the apple overlaps with the snake's body
            while (self.x, self.y) in self.body:
                self.x, self.y = apple.move()  # Update the head position
    def check_game_over(self, window_width, window_height):
        if self.x < 0 or self.x >= window_width or self.y < 0 or self.y >= window_height:
            return True
        for segment in self.body[1:]:
            if self.x == segment[0] and self.y == segment[1]:
                return True
        return False
    def draw(self, window):
        for segment in self.body:
            pygame.draw.rect(window, self.color, (segment[0], segment[1], self.size, self.size))