'''
This is the main file of the Snake Game application. It contains the main game loop and handles user input.
'''
import pygame
import sys
from snake import Snake
from food import Food
# Initialize pygame
pygame.init()
# Set up the game window
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")
# Define colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
# Define game variables
clock = pygame.time.Clock()
snake_block_size = 20
snake_speed = 15
# Define game functions
def draw_snake(snake_block_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, green, [x[0], x[1], snake_block_size, snake_block_size])
def game_loop():
    game_over = False
    game_quit = False
    # Initialize snake position and movement
    snake = Snake(screen_width / 2, screen_height / 2, snake_block_size)
    while not game_quit:
        while game_over:
            # Game over screen
            screen.fill(black)
            font_style = pygame.font.SysFont(None, 50)
            message = font_style.render("Game Over! Press Q-Quit or C-Play Again", True, white)
            screen.blit(message, [screen_width / 6, screen_height / 3])
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_quit = True
                    game_over = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_quit = True
                        game_over = False
                    if event.key == pygame.K_c:
                        game_loop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_quit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake.change_direction("LEFT")
                elif event.key == pygame.K_RIGHT:
                    snake.change_direction("RIGHT")
                elif event.key == pygame.K_UP:
                    snake.change_direction("UP")
                elif event.key == pygame.K_DOWN:
                    snake.change_direction("DOWN")
        # Update snake position
        snake.move()
        # Check for collision with boundaries
        if snake.x >= screen_width or snake.x < 0 or snake.y >= screen_height or snake.y < 0:
            game_over = True
        screen.fill(black)
        draw_snake(snake_block_size, snake.snake_list)
        pygame.display.update()
        clock.tick(snake_speed)
    pygame.quit()
    sys.exit()
# Start the game loop
game_loop()