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
# Create the window
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake Game")
# Clock to control the game's frame rate
clock = pygame.time.Clock()
# Font for displaying text
font_style = pygame.font.SysFont(None, 30)
def display_score(score):
    '''
    Display the score on the window
    '''
    score_text = font_style.render("Score: " + str(score), True, white)
    window.blit(score_text, [10, 10])
def game_over():
    '''
    Display "Game Over" message on the window
    '''
    game_over_text = font_style.render("Game Over", True, red)
    window.blit(game_over_text, [window_width/2 - 100, window_height/2 - 50])
def snake_game():
    '''
    Main game loop
    '''
    game_over_flag = False
    # Snake initial position
    x1 = window_width/2
    y1 = window_height/2
    # Snake movement
    x1_change = 0
    y1_change = 0
    # Snake body
    snake_body = []
    length_of_snake = 1
    # Apple position
    apple_x = round(random.randrange(0, window_width - snake_size) / 20.0) * 20.0
    apple_y = round(random.randrange(0, window_height - snake_size) / 20.0) * 20.0
    while not game_over_flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over_flag = True
            elif event.type == pygame.KEYDOWN:
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
        # Check if the snake hits the window boundaries or itself
        if x1 >= window_width or x1 < 0 or y1 >= window_height or y1 < 0:
            game_over_flag = True
        x1 += x1_change
        y1 += y1_change
        window.fill(black)
        pygame.draw.rect(window, green, [apple_x, apple_y, snake_size, snake_size])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_body.append(snake_head)
        if len(snake_body) > length_of_snake:
            del snake_body[0]
        for segment in snake_body[:-1]:
            if segment == snake_head:
                game_over_flag = True
        for segment in snake_body:
            pygame.draw.rect(window, white, [segment[0], segment[1], snake_size, snake_size])
        display_score(length_of_snake - 1)
        pygame.display.update()
        if x1 == apple_x and y1 == apple_y:
            apple_x = round(random.randrange(0, window_width - snake_size) / 20.0) * 20.0
            apple_y = round(random.randrange(0, window_height - snake_size) / 20.0) * 20.0
            length_of_snake += 1
        clock.tick(snake_speed)
    game_over()
    pygame.display.update()
    pygame.time.wait(2000)
snake_game()
pygame.quit()