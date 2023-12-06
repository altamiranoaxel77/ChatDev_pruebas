'''
Game class for Snake Game
'''
import pygame
import sys
from pygame.locals import *
from snake import Snake
from apple import Apple
class Game:
    def __init__(self):
        self.width = 800
        self.height = 600
        self.display = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Snake Game')
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)
        self.score = 0
        self.timer = 0
        self.is_game_over = False
        self.is_in_menu = True
        self.snake = Snake(self.width, self.height)
        self.apple = Apple(self.width, self.height)
    def start_game(self):
        self.is_in_menu = False
        self.is_game_over = False
        self.score = 0
        self.timer = pygame.time.get_ticks()
        self.snake.reset()
    def update(self):
        if not self.is_in_menu and not self.is_game_over:
            current_time = pygame.time.get_ticks()
            if current_time - self.timer >= 1000:
                self.timer = current_time
                self.snake.move()
            keys = pygame.key.get_pressed()
            if keys[K_UP] and self.snake.direction != 'down':
                self.snake.direction = 'up'
            elif keys[K_DOWN] and self.snake.direction != 'up':
                self.snake.direction = 'down'
            elif keys[K_LEFT] and self.snake.direction != 'right':
                self.snake.direction = 'left'
            elif keys[K_RIGHT] and self.snake.direction != 'left':
                self.snake.direction = 'right'
            if self.snake.check_collision(self.apple):
                self.snake.grow()
                self.score += 1
                self.apple.generate()
            if self.snake.check_self_collision() or self.snake.check_boundary_collision(self.width, self.height):
                self.is_game_over = True
    def draw(self):
        self.display.fill((0, 0, 0))
        if self.is_in_menu:
            self.draw_menu()
        elif self.is_game_over:
            self.draw_game_over()
        else:
            self.snake.draw(self.display)
            self.apple.draw(self.display)
        self.draw_score()
        self.draw_timer()
    def draw_menu(self):
        title_text = self.font.render('Snake Game', True, (255, 255, 255))
        play_text = self.font.render('Play', True, (255, 255, 255))
        quit_text = self.font.render('Quit', True, (255, 255, 255))
        self.display.blit(title_text, (self.width // 2 - title_text.get_width() // 2, self.height // 2 - 100))
        self.display.blit(play_text, (self.width // 2 - play_text.get_width() // 2, self.height // 2))
        self.display.blit(quit_text, (self.width // 2 - quit_text.get_width() // 2, self.height // 2 + 50))
    def draw_game_over(self):
        game_over_text = self.font.render('Game Over', True, (255, 255, 255))
        play_again_text = self.font.render('Play Again', True, (255, 255, 255))
        quit_text = self.font.render('Quit', True, (255, 255, 255))
        self.display.blit(game_over_text, (self.width // 2 - game_over_text.get_width() // 2, self.height // 2 - 100))
        self.display.blit(play_again_text, (self.width // 2 - play_again_text.get_width() // 2, self.height // 2))
        self.display.blit(quit_text, (self.width // 2 - quit_text.get_width() // 2, self.height // 2 + 50))
    def draw_score(self):
        score_text = self.font.render(f'Score: {self.score}', True, (255, 255, 255))
        self.display.blit(score_text, (10, 10))
    def draw_timer(self):
        elapsed_time = (pygame.time.get_ticks() - self.timer) // 1000
        timer_text = self.font.render(f'Time: {elapsed_time}', True, (255, 255, 255))
        self.display.blit(timer_text, (self.width - timer_text.get_width() - 10, 10))