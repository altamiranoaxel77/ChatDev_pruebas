'''
This file contains the Menu class and related functions.
'''
import pygame
import sys
class Menu:
    def __init__(self):
        self.selected_option = 0
        self.options = ["Play", "Quit"]
    def draw(self, window, window_width, window_height, green, white):
        font_style = pygame.font.SysFont(None, 50)
        for i, option in enumerate(self.options):
            if i == self.selected_option:
                text = font_style.render(option, True, green)
            else:
                text = font_style.render(option, True, white)
            window.blit(text, [window_width / 3, window_height / 3 + i * 50])
    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.selected_option = (self.selected_option - 1) % len(self.options)
            elif event.key == pygame.K_DOWN:
                self.selected_option = (self.selected_option + 1) % len(self.options)
            elif event.key == pygame.K_RETURN:
                if self.selected_option == 0:
                    game_loop()
                elif self.selected_option == 1:
                    pygame.quit()
                    sys.exit()
        elif event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
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
# Create menu instance
menu = Menu()
# Game loop
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
                menu.handle_input(event)
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