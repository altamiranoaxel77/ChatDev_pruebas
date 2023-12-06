'''
Main file for Snake Game
'''
import pygame
import sys
import time
# Initialize pygame
pygame.init()
# Set up the window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake Game")
# Define colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
# Define game variables
snake_size = 20
snake_speed = 15
# Define fonts
font_style = pygame.font.SysFont(None, 50)
score_font = pygame.font.SysFont(None, 35)
def game_over():
    '''
    Display "Game Over" message on the screen
    '''
    message = font_style.render("Game Over", True, red)
    window.blit(message, [window_width/2 - 100, window_height/2 - 50])
    pygame.display.update()
    time.sleep(2)
def show_score(score):
    '''
    Display the current score on the screen
    '''
    score_text = score_font.render("Score: " + str(score), True, black)
    window.blit(score_text, [10, 10])
def game_loop():
    '''
    Main game loop
    '''
    game_over_flag = False
    game_exit = False
    # Snake initial position
    x1 = window_width / 2
    y1 = window_height / 2
    # Snake movement
    x1_change = 0
    y1_change = 0
    # Snake length and score
    snake_length = 1
    score = 0
    # Game clock
    clock = pygame.time.Clock()
    while not game_exit:
        while game_over_flag:
            window.fill(white)
            game_over()
            show_score(score)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_exit = True
                    game_over_flag = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        game_loop()
                    if event.key == pygame.K_ESCAPE:
                        game_exit = True
                        game_over_flag = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
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
            game_over_flag = True
        # Update snake position
        x1 += x1_change
        y1 += y1_change
        # Clear the window
        window.fill(white)
        # Draw the snake
        pygame.draw.rect(window, green, [x1, y1, snake_size, snake_size])
        # Update the display
        pygame.display.update()
        # Set the game speed
        clock.tick(snake_speed)
# Start the game
game_loop()
# Quit pygame
pygame.quit()
sys.exit()