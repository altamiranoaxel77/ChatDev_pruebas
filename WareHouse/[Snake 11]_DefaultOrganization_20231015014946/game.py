'''
This file contains the Game class, which handles the game logic and interactions between the snake and the food.
'''
import pygame
from snake import Snake
from food import Food
class Game:
    def __init__(self, snake_block_size, screen_width, screen_height):
        self.snake = Snake(screen_width / 2, screen_height / 2, snake_block_size)
        self.food = Food(snake_block_size, screen_width, screen_height)
    def update(self):
        game_over = False
        self.snake.move()
        # Check for collision with food
        if self.snake.x == self.food.x and self.snake.y == self.food.y:
            self.snake.length += 1
            self.food = Food(self.snake.snake_block_size, screen_width, screen_height)
        # Check for collision with boundaries
        if self.snake.x >= screen_width or self.snake.x < 0 or self.snake.y >= screen_height or self.snake.y < 0:
            game_over = True
        # Check for collision with snake's body
        for segment in self.snake.snake_list[1:]:
            if segment[0] == self.snake.x and segment[1] == self.snake.y:
                game_over = True
        # Update snake's body segments
        self.snake.snake_list.append([self.snake.x, self.snake.y])
        if len(self.snake.snake_list) > self.snake.length:
            del self.snake.snake_list[0]
        return game_over
    def draw(self):
        screen.fill(black)
        self.snake.draw()
        self.food.draw()
        pygame.display.update()