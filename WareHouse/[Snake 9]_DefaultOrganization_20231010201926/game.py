'''
Game class for Snake Game
'''
import pygame
import sys
from snake import Snake
from apple import Apple
class Game:
    def __init__(self):
        self.width = 800
        self.height = 600
        self.grid_size = 20
        self.grid_width = self.width // self.grid_size
        self.grid_height = self.height // self.grid_size
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()
        self.snake = Snake(self.grid_width // 2, self.grid_height // 2, self.grid_size)
        self.apple = Apple(self.grid_width, self.grid_height, self.grid_size)
        self.score = 0
    def run(self):
        while True:
            self.clock.tick(10)
            self.handle_events()
            self.update()
            self.draw()
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.snake.change_direction("UP")
                elif event.key == pygame.K_DOWN:
                    self.snake.change_direction("DOWN")
                elif event.key == pygame.K_LEFT:
                    self.snake.change_direction("LEFT")
                elif event.key == pygame.K_RIGHT:
                    self.snake.change_direction("RIGHT")
    def update(self):
        self.snake.move()
        if self.snake.collides_with_apple(self.apple):
            self.snake.grow()
            self.apple.generate_new_position(self.grid_width, self.grid_height)
            self.score += 1
        if self.snake.collides_with_self() or self.snake.collides_with_wall(self.grid_width, self.grid_height):
            self.game_over()
    def draw(self):
        self.screen.fill((0, 0, 0))
        self.snake.draw(self.screen)
        self.apple.draw(self.screen)
        self.draw_score()
        pygame.display.flip()
    def draw_score(self):
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))
    def game_over(self):
        self.score = 0
        self.snake.reset()
        self.apple.generate_new_position(self.grid_width, self.grid_height)