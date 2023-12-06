'''
Snake Game
'''
import pygame
import random
# Initialize pygame
pygame.init()
# Window dimensions
window_width = 800
window_height = 600
# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
# Snake dimensions
snake_size = 20
snake_speed = 15
# Fonts
font_style = pygame.font.SysFont(None, 50)
score_font = pygame.font.SysFont(None, 35)
# Create the game window
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Snake Game')
# Function to display the score
def show_score(score):
    score_text = score_font.render("Score: " + str(score), True, black)
    window.blit(score_text, [10, 10])
# Function to display the snake
def draw_snake(snake_size, snake_pixels):
    for pixel in snake_pixels:
        pygame.draw.rect(window, green, [pixel[0], pixel[1], snake_size, snake_size])
# Function to run the game
def run_game():
    game_over = False
    game_close = False
    # Initial position of the snake
    x1 = window_width / 2
    y1 = window_height / 2
    # Movement of the snake
    x1_change = 0
    y1_change = 0
    # Snake body
    snake_pixels = []
    snake_length = 1
    # Apple position
    apple_x = round(random.randrange(0, window_width - snake_size) / 20.0) * 20.0
    apple_y = round(random.randrange(0, window_height - snake_size) / 20.0) * 20.0
    # Game loop
    while not game_over:
        while game_close:
            window.fill(white)
            game_over_text = font_style.render("Game Over", True, red)
            window.blit(game_over_text, [window_width / 2.7, window_height / 3])
            show_score(snake_length - 1)
            pygame.display.update()
            # Restart the game or quit
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        run_game()
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
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
        # Check if the snake hits the boundaries
        if x1 >= window_width or x1 < 0 or y1 >= window_height or y1 < 0:
            game_close = True
        # Update the snake position
        x1 += x1_change
        y1 += y1_change
        window.fill(white)
        # Draw the apple
        pygame.draw.rect(window, red, [apple_x, apple_y, snake_size, snake_size])
        # Update the snake body
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_pixels.append(snake_head)
        if len(snake_pixels) > snake_length:
            del snake_pixels[0]
        # Check if the snake hits itself
        for pixel in snake_pixels[:-1]:
            if pixel == snake_head:
                game_close = True
        # Draw the snake
        draw_snake(snake_size, snake_pixels)
        # Check if the snake eats the apple
        if x1 == apple_x and y1 == apple_y:
            apple_x = round(random.randrange(0, window_width - snake_size) / 20.0) * 20.0
            apple_y = round(random.randrange(0, window_height - snake_size) / 20.0) * 20.0
            snake_length += 1
        # Display the score
        show_score(snake_length - 1)
        # Update the display
        pygame.display.update()
        # Set the game speed
        clock = pygame.time.Clock()
        clock.tick(snake_speed)
    # Quit pygame
    pygame.quit()
# Run the game
run_game()