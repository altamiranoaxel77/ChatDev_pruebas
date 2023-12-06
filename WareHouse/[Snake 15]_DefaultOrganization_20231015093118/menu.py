'''
Snake Game - StartMenu Class
'''
import pygame
class StartMenu:
    def __init__(self, window_width, window_height):
        self.window_width = window_width
        self.window_height = window_height
        self.font = pygame.font.Font(None, 36)
        self.text = self.font.render("Press SPACE to start", True, (255, 255, 255))
        self.text_rect = self.text.get_rect(center=(window_width // 2, window_height // 2))
    def draw(self, window):
        window.fill((0, 0, 0))
        window.blit(self.text, self.text_rect)