'''
Snake Game
'''
import pygame
import random
# Initialize Pygame
pygame.init()
# Set up the window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake Game")
# Define colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
# Define game variables
snake_size = 20
snake_speed = 15
clock = pygame.time.Clock()
font_style = pygame.font.SysFont(None, 50)
score_font = pygame.font.SysFont(None, 35)
def show_score(score):
    score_text = score_font.render("Score: " + str(score), True, white)
    window.blit(score_text, [10, 10])
def game_over():
    message = font_style.render("Game Over", True, red)
    window.blit(message, [window_width/2 - 100, window_height/2 - 50])
    pygame.display.update()
    pygame.time.wait(3000)
def game_loop():
    game_over = False
    game_close = False
    # Snake initial position
    x1 = window_width / 2
    y1 = window_height / 2
    # Snake movement
    x1_change = 0
    y1_change = 0
    # Apple position
    apple_x = round(random.randrange(0, window_width - snake_size) / 20.0) * 20.0
    apple_y = round(random.randrange(0, window_height - snake_size) / 20.0) * 20.0
    # Score
    score = 0
    while not game_over:
        while game_close:
            window.fill(black)
            game_over()
            show_score(score)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        game_loop()
                    if event.key == pygame.K_ESCAPE:
                        game_over = True
                        game_close = False
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
        if x1 >= window_width or x1 < 0 or y1 >= window_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        window.fill(black)
        pygame.draw.rect(window, green, [apple_x, apple_y, snake_size, snake_size])
        pygame.draw.rect(window, white, [x1, y1, snake_size, snake_size])
        show_score(score)
        pygame.display.update()
        if x1 == apple_x and y1 == apple_y:
            score += 1
            apple_x = round(random.randrange(0, window_width - snake_size) / 20.0) * 20.0
            apple_y = round(random.randrange(0, window_height - snake_size) / 20.0) * 20.0
        clock.tick(snake_speed)
    pygame.quit()
game_loop()