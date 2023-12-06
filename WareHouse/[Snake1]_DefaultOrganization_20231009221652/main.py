'''
Snake Game
- The snake grows every time it eats an apple.
- The game ends if the snake hits the window borders or itself.
- The game keeps track of the number of apples eaten.
'''
import pygame
import random
import sys
# Initialize the game
pygame.init()
# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
# Set the width and height of the game window
window_width = 800
window_height = 600
window_size = (window_width, window_height)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("Snake Game")
# Set the clock for the game
clock = pygame.time.Clock()
# Define the snake class
class Snake:
    def __init__(self):
        self.size = 1
        self.segments = [(window_width // 2, window_height // 2)]
        self.direction = random.choice(['up', 'down', 'left', 'right'])
    def move(self):
        x, y = self.segments[0]
        if self.direction == 'up':
            y -= 10
        elif self.direction == 'down':
            y += 10
        elif self.direction == 'left':
            x -= 10
        elif self.direction == 'right':
            x += 10
        new_head = (x, y)
        if new_head in self.segments[1:]:
            # Snake collided with itself, game over
            return False
        self.segments.insert(0, new_head)
        if len(self.segments) > self.size:
            self.segments.pop()
        return True
    def change_direction(self, direction):
        if direction == 'up' and self.direction != 'down':
            self.direction = 'up'
        elif direction == 'down' and self.direction != 'up':
            self.direction = 'down'
        elif direction == 'left' and self.direction != 'right':
            self.direction = 'left'
        elif direction == 'right' and self.direction != 'left':
            self.direction = 'right'
    def draw(self):
        for segment in self.segments:
            pygame.draw.rect(window, GREEN, (segment[0], segment[1], 10, 10))
    def check_collision(self):
        head = self.segments[0]
        if head[0] < 0 or head[0] >= window_width or head[1] < 0 or head[1] >= window_height:
            return True
        for segment in self.segments[1:]:
            if segment == head:
                return True
        return False
    def check_apple_collision(self, apple):
        head = self.segments[0]
        if head[0] == apple.x and head[1] == apple.y:
            self.size += 1
            return True
        return False
# Define the apple class
class Apple:
    def __init__(self):
        self.x = random.randint(0, window_width // 10 - 1) * 10
        self.y = random.randint(0, window_height // 10 - 1) * 10
    def draw(self):
        pygame.draw.rect(window, RED, (self.x, self.y, 10, 10))
# Initialize the snake and apple
snake = Snake()
apple = Apple()
# Initialize the score
score = 0
# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.change_direction('up')
            elif event.key == pygame.K_DOWN:
                snake.change_direction('down')
            elif event.key == pygame.K_LEFT:
                snake.change_direction('left')
            elif event.key == pygame.K_RIGHT:
                snake.change_direction('right')
    # Move the snake
    if not snake.move():
        running = False
    # Check collision with apple
    if snake.check_apple_collision(apple):
        apple = Apple()
        score += 1
    # Check collision with borders or itself
    if snake.check_collision():
        running = False
    # Clear the window
    window.fill(BLACK)
    # Draw the snake and apple
    snake.draw()
    apple.draw()
    # Update the display
    pygame.display.flip()
    # Set the game speed
    clock.tick(20)
# Game over
print("Game Over")
print("Score:", score)
# Quit the game
pygame.quit()