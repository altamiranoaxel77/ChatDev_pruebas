'''
Desarrolla un juego de la serpiente en Python utilizando la biblioteca Pygame con las siguientes especificaciones:
1) La serpiente debe comenzar con una longitud de 1 y moverse en una ventana con un fondo de color. Cuando la serpiente come una manzana, su longitud debe aumentar en 1. Implementa un contador visible en la parte superior de la ventana que muestre el número de manzanas comidas por la serpiente.
2) Si la serpiente choca con los bordes de la ventana o consigo misma, el juego debe terminar, y se debe mostrar un mensaje de 'Juego terminado'.
3) Agrega un menú inicial que permita al jugador elegir entre las opciones 'Jugar' o 'Salir'. El menú debe ser interactivo y responder a las acciones del jugador.
4) Después de que el jugador pierda el juego, muestra un mensaje de 'Game Over' en la pantalla durante 3 segundos y luego regresa automáticamente al menú inicial.
5) El menú inicial debe ser accesible en cualquier momento, permitiendo al jugador volver al menú principal en cualquier momento.
6) Implementa un sistema de puntuación que muestre la puntuación actual del jugador en la pantalla mientras juega.
7) Agrega un temporizador para llevar un registro del tiempo transcurrido durante la partiddda. Asegúrate de que el juego sea interactivo, responda a las acciones del jugador de manera adecuada y proporcione una experiencia de juego agradable. Elige un esquema de colores atractivo y muestra la longitud actual de la serpiente, el contador de manzanas comidas, el mensaje de 'Game Over' y la puntuación de manera clara en la ventana.
Por favor, proporciona el código necesario para implementar todas estas funcionalidades en Python utilizando Pygame, y asegúrate de que el juego cumpla con las especificaciones mencionadas.
'''
import pygame
import random
# Initialize pygame
pygame.init()
# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
# Set up the game window
width = 800
height = 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")
# Set up the game clock
clock = pygame.time.Clock()
# Define the snake properties
snake_size = 20
snake_speed = 10
snake_x = width // 2
snake_y = height // 2
snake_dx = 0
snake_dy = 0
snake_length = 1
snake_body = []
# Define the apple properties
apple_size = 20
apple_x = random.randint(0, width - apple_size) // 20 * 20
apple_y = random.randint(0, height - apple_size) // 20 * 20
# Define the game variables
score = 0
game_over = False
# Define the font for displaying text
font = pygame.font.Font(None, 36)
# Define the menu options
menu_options = ["Play", "Quit"]
selected_option = 0
# Define the game state
game_state = "menu"
# Define the timer variables
start_time = 0
elapsed_time = 0
# Game loop
while not game_over:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = False
        elif event.type == pygame.KEYDOWN:
            if game_state == "menu":
                if event.key == pygame.K_UP:
                    selected_option = (selected_option - 1) % len(menu_options)
                elif event.key == pygame.K_DOWN:
                    selected_option = (selected_option + 1) % len(menu_options)
                elif event.key == pygame.K_RETURN:
                    if selected_option == 0:
                        game_state = "playing"
                        start_time = pygame.time.get_ticks()
                    else:
                        game_over = False
            elif game_state == "playing":
                if event.key == pygame.K_UP and snake_dy != snake_size:
                    snake_dx = 0
                    snake_dy = -snake_size
                elif event.key == pygame.K_DOWN and snake_dy != -snake_size:
                    snake_dx = 0
                    snake_dy = snake_size
                elif event.key == pygame.K_LEFT and snake_dx != snake_size:
                    snake_dx = -snake_size
                    snake_dy = 0
                elif event.key == pygame.K_RIGHT and snake_dx != -snake_size:
                    snake_dx = snake_size
                    snake_dy = 0
    # Update game state
    if game_state == "playing":
        # Move the snake
        snake_x += snake_dx
        snake_y += snake_dy
        # Check for collisions with the borders
        if snake_x < 0 or snake_x >= width or snake_y < 0 or snake_y >= height:
            game_state = "menu"
        # Check for collisions with the snake body
        snake_head = [snake_x, snake_y]
        if snake_head in snake_body[1:]:
            game_state = "menu"
        # Check if the snake has eaten the apple
        if snake_x == apple_x and snake_y == apple_y:
            score += 1
            snake_length += 1
            apple_x = random.randint(0, width - apple_size) // 20 * 20
            apple_y = random.randint(0, height - apple_size) // 20 * 20
        # Update the snake body
        snake_body.append(snake_head)
        if len(snake_body) > snake_length:
            del snake_body[0]
    # Draw game objects
    window.fill(BLACK)
    if game_state == "menu":
        # Draw menu options
        for i, option in enumerate(menu_options):
            text = font.render(option, True, WHITE if i == selected_option else RED)
            text_rect = text.get_rect(center=(width // 2, height // 2 + i * 50))
            window.blit(text, text_rect)
    elif game_state == "playing":
        # Draw the snake
        for segment in snake_body:
            pygame.draw.rect(window, WHITE, (segment[0], segment[1], snake_size, snake_size))
        # Draw the apple
        pygame.draw.rect(window, RED, (apple_x, apple_y, apple_size, apple_size))
        # Draw the score
        score_text = font.render("Score: " + str(score), True, WHITE)
        window.blit(score_text, (10, 10))
        # Draw the timer
        elapsed_time = (pygame.time.get_ticks() - start_time) // 1000
        timer_text = font.render("Time: " + str(elapsed_time), True, WHITE)
        window.blit(timer_text, (width - 150, 10))
    elif game_state == "game_over":
        # Draw the game over message
        game_over_text = font.render("Game Over", True, WHITE)
        game_over_rect = game_over_text.get_rect(center=(width // 2, height // 2))
        window.blit(game_over_text, game_over_rect)
        # Return to the menu after 3 seconds
        if pygame.time.get_ticks() - start_time >= 3000:
            game_state = "menu"
    # Update the display
    pygame.display.update()
    clock.tick(snake_speed)
# Quit the game
pygame.quit()