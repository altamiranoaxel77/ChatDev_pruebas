'''
Snake class for Snake Game
'''
import pygame
class Snake:
    def __init__(self, start_x, start_y, size):
        self.size = size
        self.head = [start_x, start_y]
        self.body = [[start_x, start_y]]
        self.direction = "RIGHT"
    def move(self):
        if self.direction == "UP":
            self.head[1] -= self.size
        elif self.direction == "DOWN":
            self.head[1] += self.size
        elif self.direction == "LEFT":
            self.head[0] -= self.size
        elif self.direction == "RIGHT":
            self.head[0] += self.size
        self.body.insert(0, list(self.head))
        self.body.pop()
    def change_direction(self, direction):
        if direction == "UP" and self.direction != "DOWN":
            self.direction = direction
        elif direction == "DOWN" and self.direction != "UP":
            self.direction = direction
        elif direction == "LEFT" and self.direction != "RIGHT":
            self.direction = direction
        elif direction == "RIGHT" and self.direction != "LEFT":
            self.direction = direction
    def grow(self):
        self.body.append(list(self.head))
    def collides_with_self(self):
        return self.head in self.body[1:]
    def collides_with_wall(self, grid_width, grid_height):
        return (
            self.head[0] < 0
            or self.head[0] >= grid_width
            or self.head[1] < 0
            or self.head[1] >= grid_height
        )
    def collides_with_apple(self, apple):
        return self.head == apple.position
    def draw(self, screen):
        for segment in self.body:
            pygame.draw.rect(screen, (0, 255, 0), (segment[0], segment[1], self.size, self.size))
    def reset(self):
        self.head = [self.body[0][0], self.body[0][1]]
        self.body = [self.head]
        self.direction = "RIGHT"