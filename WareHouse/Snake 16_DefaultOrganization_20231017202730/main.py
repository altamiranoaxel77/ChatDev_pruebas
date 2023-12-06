'''
This is the main file that runs the snake game.
'''
import pygame
from game import Game
# Initialize the game
pygame.init()
# Set up the game window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake Game")
# Create a game instance
game = Game(window_width, window_height)
# Game loop
running = True
clock = pygame.time.Clock()  # Create a clock object for controlling the frame rate
while running:
    # Process events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                game.reset()  # Reset the game if Enter key is pressed
    # Update game state
    game.update()
    # Check if the snake is lost
    if game.snake.is_lost():
        game.reset()  # Reset the game if the snake is lost
    # Render game
    game.render(window)
    # Update display
    pygame.display.flip()
    clock.tick(10)  # Set the frame rate to 10 frames per second
# Quit the game
pygame.quit()