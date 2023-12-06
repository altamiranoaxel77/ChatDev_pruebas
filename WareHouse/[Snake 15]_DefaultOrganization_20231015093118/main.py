'''
Snake Game - Main File
'''
import pygame
from snake import Snake
from apple import Apple
from menu import StartMenu
# Initialize Pygame
pygame.init()
# Set up the game window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake Game")
# Set up the clock to control the game's frame rate
clock = pygame.time.Clock()
# Set up the colors
background_color = (0, 0, 0)
snake_color = (0, 255, 0)
apple_color = (255, 0, 0)
# Set up the game objects
snake = Snake(window_width, window_height, snake_color)
apple = Apple(window_width, window_height, apple_color)
# Set up the start menu
menu = StartMenu(window_width, window_height)
# Game loop
running = True
game_over = False
in_menu = True
while running:
    while in_menu:
        menu.draw(window)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                in_menu = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    in_menu = False
    while not game_over:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.change_direction("UP")
                elif event.key == pygame.K_DOWN:
                    snake.change_direction("DOWN")
                elif event.key == pygame.K_LEFT:
                    snake.change_direction("LEFT")
                elif event.key == pygame.K_RIGHT:
                    snake.change_direction("RIGHT")
        # Update game objects
        snake.move()
        snake.check_collision(apple)
        game_over = snake.check_game_over(window_width, window_height)
        # Draw game objects
        window.fill(background_color)
        snake.draw(window)
        apple.draw(window)
        pygame.display.update()
        # Control the game's frame rate
        clock.tick(10)
pygame.quit()