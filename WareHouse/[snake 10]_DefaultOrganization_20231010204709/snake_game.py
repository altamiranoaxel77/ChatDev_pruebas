'''
Snake Game
'''
import pygame
import random
# Initialize the game
pygame.init()
# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
# Set the width and height of the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")
# Set the clock speed
clock = pygame.time.Clock()
# Define the Snake class
class Snake:
    def __init__(self):
        self.size = 1
        self.segments = [(screen_width // 2, screen_height // 2)]
        self.direction = random.choice(["UP", "DOWN", "LEFT", "RIGHT"])
        self.speed = 20
    def move(self):
        x, y = self.segments[0]
        if self.direction == "UP":
            y -= self.speed
        elif self.direction == "DOWN":
            y += self.speed
        elif self.direction == "LEFT":
            x -= self.speed
        elif self.direction == "RIGHT":
            x += self.speed
        self.segments.insert(0, (x, y))
        if len(self.segments) > self.size:
            self.segments.pop()
    def change_direction(self, direction):
        if direction in ["UP", "DOWN", "LEFT", "RIGHT"]:
            if (direction == "UP" and self.direction != "DOWN") or \
               (direction == "DOWN" and self.direction != "UP") or \
               (direction == "LEFT" and self.direction != "RIGHT") or \
               (direction == "RIGHT" and self.direction != "LEFT"):
                self.direction = direction
    def draw(self):
        for segment in self.segments:
            pygame.draw.rect(screen, GREEN, (segment[0], segment[1], self.speed, self.speed))
    def check_collision(self):
        head = self.segments[0]
        if head[0] < 0 or head[0] >= screen_width or head[1] < 0 or head[1] >= screen_height:
            return True
        for segment in self.segments[1:]:
            if segment == head:
                return True
        return False
    def eat_food(self, food):
        if self.segments[0] == food.position:
            self.size += 1
            food.generate_position()
# Define the Food class
class Food:
    def __init__(self):
        self.size = 20
        self.position = (random.randint(0, screen_width - self.size) // self.size * self.size, random.randint(0, screen_height - self.size) // self.size * self.size)
    def draw(self):
        pygame.draw.rect(screen, RED, (self.position[0], self.position[1], self.size, self.size))
    def generate_position(self):
        self.position = (random.randint(0, screen_width - self.size) // self.size * self.size, random.randint(0, screen_height - self.size) // self.size * self.size)
# Create the Snake and Food objects
snake = Snake()
food = Food()
# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.change_direction("UP")
            elif event.key == pygame.K_DOWN:
                snake.change_direction("DOWN")
            elif event.key == pygame.K_LEFT:
                snake.change_direction("LEFT")
            elif event.key == pygame.K_RIGHT:
                snake.change_direction("RIGHT")
    # Game logic
    snake.move()
    if snake.check_collision():
        running = False
    snake.eat_food(food)
    # Drawing
    screen.fill(BLACK)
    snake.draw()
    food.draw()
    pygame.display.flip()
    # Set the frame rate
    clock.tick(10)
# Quit the game
pygame.quit()