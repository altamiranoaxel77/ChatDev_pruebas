'''
This is the main file for the Snake game.
'''
import pygame
import sys
# Initialize pygame
pygame.init()
# Set up the game window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake Game")
# Define colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
# Define game variables
clock = pygame.time.Clock()
snake_block_size = 20
snake_speed = 15
# Define functions
def draw_snake(snake_block_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(window, green, [x[0], x[1], snake_block_size, snake_block_size])
def game_loop():
    game_over = False
    game_running = True
    # Initialize snake position and movement
    x1 = window_width / 2
    y1 = window_height / 2
    x1_change = 0
    y1_change = 0
    snake_list = []
    snake_length = 1
    while game_running:
        while game_over:
            # Game over screen
            window.fill(black)
            font_style = pygame.font.SysFont(None, 50)
            message = font_style.render("Game Over! Press Q-Quit or C-Play Again", True, white)
            window.blit(message, [window_width / 6, window_height / 3])
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_running = False
                    game_over = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_running = False
                        game_over = False
                    if event.key == pygame.K_c:
                        game_loop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block_size
                    x1_change = 0
        # Check for boundaries
        if x1 >= window_width or x1 < 0 or y1 >= window_height or y1 < 0:
            game_over = True
        # Update snake position
        x1 += x1_change
        y1 += y1_change
        window.fill(black)
        pygame.draw.rect(window, green, [x1, y1, snake_block_size, snake_block_size])
        pygame.display.update()
        clock.tick(snake_speed)
    pygame.quit()
    sys.exit()
# Start the game loop
game_loop()