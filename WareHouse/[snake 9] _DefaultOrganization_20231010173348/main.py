'''
Snake Game
'''
import pygame
import sys
import time
import random
# Initialize Pygame
pygame.init()
# Set window dimensions
window_width = 800
window_height = 600
# Set colors
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)
# Set snake properties
snake_size = 20
snake_speed = 15
# Set font properties
font_style = pygame.font.SysFont(None, 50)
score_font = pygame.font.SysFont(None, 35)
# Create window
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Snake Game')
# Function to display score
def show_score(score):
    score_text = score_font.render("Score: " + str(score), True, green)
    window.blit(score_text, [10, 10])
# Function to display game over message
def game_over():
    message = font_style.render("Game Over", True, red)
    window.blit(message, [window_width/2 - 100, window_height/2 - 50])
    pygame.display.update()
    time.sleep(2)
# Function to create snake
def draw_snake(snake_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(window, green, [x[0], x[1], snake_size, snake_size])
# Function to run the game
def game():
    game_ended = False
    game_close = False
    # Set initial snake position
    x1 = window_width/2
    y1 = window_height/2
    # Set initial snake movement
    x1_change = 0
    y1_change = 0
    # Create snake list and snake length
    snake_list = []
    snake_length = 1
    # Set initial apple position
    apple_x = round(random.randrange(0, window_width - snake_size) / 20.0) * 20.0
    apple_y = round(random.randrange(0, window_height - snake_size) / 20.0) * 20.0
    # Set initial score
    score = 0
    # Set initial timer
    start_time = time.time()
    while not game_ended:
        while game_close:
            window.fill(black)
            game_over()
            show_score(score)
            pygame.display.update()
            # Ask player to play again or exit
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_j:
                        game()
                    elif event.key == pygame.K_s:
                        game_ended = True
                        game_close = False
                    elif event.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_size
                    x1_change = 0
        # Check if snake hits the boundaries
        if x1 >= window_width or x1 < 0 or y1 >= window_height or y1 < 0:
            game_close = True
        # Update snake position
        x1 += x1_change
        y1 += y1_change
        window.fill(black)
        pygame.draw.rect(window, red, [apple_x, apple_y, snake_size, snake_size])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        # Remove extra snake segments
        if len(snake_list) > snake_length:
            del snake_list[0]
        # Check if snake hits itself
        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True
        # Draw snake and display score
        draw_snake(snake_size, snake_list)
        show_score(score)
        # Check if snake eats the apple
        if x1 == apple_x and y1 == apple_y:
            apple_x = round(random.randrange(0, window_width - snake_size) / 20.0) * 20.0
            apple_y = round(random.randrange(0, window_height - snake_size) / 20.0) * 20.0
            snake_length += 1
            score += 1
        # Update window
        pygame.display.update()
        # Set game speed
        clock = pygame.time.Clock()
        clock.tick(snake_speed)
    pygame.quit()
    sys.exit()
# Run the game
game()