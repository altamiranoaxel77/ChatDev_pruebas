'''
This file contains the Menu class which represents the menu in the game.
'''
import pygame
class Menu:
    def __init__(self, window_width, window_height):
        self.window_width = window_width
        self.window_height = window_height
        self.font = pygame.font.Font(None, 36)
        self.title = self.font.render("Snake Game", True, (255, 255, 255))
        self.start_text = self.font.render("Press SPACE to start", True, (255, 255, 255))
        self.quit_text = self.font.render("Press Q to quit", True, (255, 255, 255))
    def draw(self, window):
        window.blit(self.title, (self.window_width // 2 - self.title.get_width() // 2, self.window_height // 2 - 50))
        window.blit(self.start_text, (self.window_width // 2 - self.start_text.get_width() // 2, self.window_height // 2))
        window.blit(self.quit_text, (self.window_width // 2 - self.quit_text.get_width() // 2, self.window_height // 2 + 50))