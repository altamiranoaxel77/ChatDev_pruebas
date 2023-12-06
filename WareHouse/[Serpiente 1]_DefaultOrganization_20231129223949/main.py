'''
This is the main file of the Snake Game application. It initializes the game and handles the game loop.
'''
import pygame
import sys
from snake import Snake
from apple import Apple
# Initialize the game
pygame.init()
# Set up the game window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake Game")
# Set up the game clock
clock = pygame.time.Clock()
def game_loop():
    # Create the snake and apple objects
    snake = Snake(window_width, window_height)
    apple = Apple(window_width, window_height)
    game_speed = 10  # Initial game speed
    game_over = False  # Variable to track game over state
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    game_speed += 1  # Increase game speed
                elif event.key == pygame.K_DOWN:
                    game_speed -= 1  # Decrease game speed
        # Update the snake and apple
        snake.update()
        if snake.check_collision(apple):
            snake.grow()
            apple.move()
        # Check if the game is over
        if snake.is_game_over():
            game_over = True
        if game_over:
            # Display game over message and ask for restart
            game_over_message()
            # Reset the game
            snake.reset()
            apple.reset()
            game_over = False  # Reset game over state
        # Clear the window
        window.fill((0, 0, 0))
        # Draw the snake and apple
        snake.draw(window)
        apple.draw(window)
        # Update the display
        pygame.display.update()
        # Set the game speed
        clock.tick(game_speed)
def game_over_message():
    # Display game over message and ask for restart
    font = pygame.font.Font(None, 36)
    text = font.render("Game Over! Press R to restart.", True, (255, 255, 255))
    text_rect = text.get_rect(center=(window_width / 2, window_height / 2))
    window.blit(text, text_rect)
    pygame.display.update()
    # Wait for the player to press R to restart
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return
# Start the game loop
game_loop()