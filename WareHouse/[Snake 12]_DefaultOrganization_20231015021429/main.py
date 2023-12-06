'''
This is the main file of the Snake game. It initializes the game and handles the game loop.
'''
import pygame
import sys
from snake import Snake
from food import Food
from menu import Menu
# Initialize the game
pygame.init()
# Set up the game window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake Game")
# Set up the game clock
clock = pygame.time.Clock()
# Initialize the snake and food
snake = Snake(window_width, window_height)
food = Food(window_width, window_height)
menu = Menu(window_width, window_height)
menu_active = True
# Game loop for menu
while menu_active:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                menu_active = False
            elif event.key == pygame.K_q:
                pygame.quit()
                sys.exit()
    window.fill((0, 0, 0))
    menu.draw(window)
    pygame.display.update()
    clock.tick(10)
# Game loop for the actual game
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake.direction != "DOWN":
                snake.direction = "UP"
            elif event.key == pygame.K_DOWN and snake.direction != "UP":
                snake.direction = "DOWN"
            elif event.key == pygame.K_LEFT and snake.direction != "RIGHT":
                snake.direction = "LEFT"
            elif event.key == pygame.K_RIGHT and snake.direction != "LEFT":
                snake.direction = "RIGHT"
    # Update the snake and food
    snake.update()
    snake.check_collision(food)
    # Clear the window
    window.fill((0, 0, 0))
    # Draw the snake and food
    snake.draw(window)
    food.draw(window)
    # Update the display
    pygame.display.update()
    # Set the game speed
    clock.tick(10)
# Quit the game
pygame.quit()