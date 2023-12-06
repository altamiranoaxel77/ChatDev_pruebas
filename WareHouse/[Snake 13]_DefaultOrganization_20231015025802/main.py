'''
This is the main file of the Snake game. It contains the main game loop and handles user input.
'''
import pygame
import sys
from snake import Snake
from menu import Menu
# Initialize pygame
pygame.init()
# Set up the game window
width = 800
height = 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")
# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
# Define game variables
cell_size = 20
snake_speed = 10
# Define game objects
snake = Snake()
snake_body = pygame.Surface((cell_size, cell_size))
snake_body.fill(GREEN)
menu = Menu(width, height)
# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # Handle user input
    menu.handle_input()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] or keys[pygame.K_DOWN] or keys[pygame.K_RETURN]:
        continue
    if menu.selected_option == 0:
        snake.change_direction("UP")
    elif menu.selected_option == 1:
        snake.change_direction("DOWN")
    elif menu.selected_option == 2:
        snake.change_direction("LEFT")
    elif menu.selected_option == 3:
        snake.change_direction("RIGHT")
    # Update game state
    snake.move()
    snake.check_collision()
    # Render game objects
    window.fill(BLACK)
    for pos in snake.pos:
        window.blit(snake_body, pos)
    menu.display_menu(window)
    pygame.display.update()