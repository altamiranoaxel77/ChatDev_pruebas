'''
This is the main file that runs the snake game.
'''
import pygame
import sys
import random
from pygame.locals import *
# Initialize pygame
pygame.init()
# Set up the window
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
window_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Snake Game')
# Set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
# Set up the game clock
clock = pygame.time.Clock()
# Set up the font
font = pygame.font.SysFont(None, 48)
# Set up the snake and apple
snake_position = [(100, 50), (90, 50), (80, 50)]
snake_body = pygame.Surface((10, 10))
snake_body.fill(GREEN)
apple_position = (200, 50)
apple = pygame.Surface((10, 10))
apple.fill(RED)
# Set up the game variables
direction = 'RIGHT'
change_to = direction
score = 0
def game_over():
    '''
    Display game over message and return to start menu.
    '''
    game_over_text = font.render('Game Over!', True, WHITE)
    game_over_rect = game_over_text.get_rect()
    game_over_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
    window_surface.blit(game_over_text, game_over_rect)
    pygame.display.flip()
    pygame.time.wait(2000)
    start_menu()
def start_menu():
    '''
    Display start menu and wait for user input to start the game.
    '''
    start_menu_text = font.render('Press SPACE to start', True, WHITE)
    start_menu_rect = start_menu_text.get_rect()
    start_menu_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
    window_surface.blit(start_menu_text, start_menu_rect)
    pygame.display.flip()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    waiting = False
def update_snake():
    '''
    Update the snake's position and check for collisions.
    '''
    global snake_position, snake_body, apple_position, score
    if direction == 'UP':
        snake_position.insert(0, (snake_position[0][0], snake_position[0][1] - 10))
    elif direction == 'DOWN':
        snake_position.insert(0, (snake_position[0][0], snake_position[0][1] + 10))
    elif direction == 'LEFT':
        snake_position.insert(0, (snake_position[0][0] - 10, snake_position[0][1]))
    elif direction == 'RIGHT':
        snake_position.insert(0, (snake_position[0][0] + 10, snake_position[0][1]))
    if snake_position[0] == apple_position:
        score += 1
        apple_position = (random.randint(1, (WINDOW_WIDTH // 10) - 1) * 10,
                          random.randint(1, (WINDOW_HEIGHT // 10) - 1) * 10)
    else:
        snake_position.pop()
    if (snake_position[0][0] < 0 or snake_position[0][0] >= WINDOW_WIDTH or
        snake_position[0][1] < 0 or snake_position[0][1] >= WINDOW_HEIGHT or
        snake_position[0] in snake_position[1:]):
        game_over()
def draw_snake():
    '''
    Draw the snake on the window surface.
    '''
    for pos in snake_position:
        window_surface.blit(snake_body, pos)
def draw_apple():
    '''
    Draw the apple on the window surface.
    '''
    window_surface.blit(apple, apple_position)
def update_score():
    '''
    Update the score on the window surface.
    '''
    score_text = font.render('Score: {}'.format(score), True, WHITE)
    score_rect = score_text.get_rect()
    score_rect.topleft = (10, 10)
    window_surface.blit(score_text, score_rect)
# Start the game
start_menu()
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_UP and direction != 'DOWN':
                change_to = 'UP'
            elif event.key == K_DOWN and direction != 'UP':
                change_to = 'DOWN'
            elif event.key == K_LEFT and direction != 'RIGHT':
                change_to = 'LEFT'
            elif event.key == K_RIGHT and direction != 'LEFT':
                change_to = 'RIGHT'
    # Update direction
    direction = change_to
    # Update snake and apple
    update_snake()
    # Clear the window surface
    window_surface.fill(BLACK)
    # Draw snake and apple
    draw_snake()
    draw_apple()
    # Update score
    update_score()
    # Update the display
    pygame.display.flip()
    # Set the game speed
    clock.tick(15)