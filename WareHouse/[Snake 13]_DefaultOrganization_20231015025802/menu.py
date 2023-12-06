# menu.py
'''
This file contains the Menu class and its methods.
'''
import pygame
import sys
class Menu:
    def __init__(self, width, height):
        self.options = ["Start Game", "High Scores", "Exit"]
        self.selected_option = 0
        self.width = width
        self.height = height
    def select_option(self, option):
        if option == "Start Game":
            # Start the game
            print("Starting the game...")
        elif option == "High Scores":
            # Show high scores
            print("Showing high scores...")
        elif option == "Exit":
            pygame.quit()
            sys.exit()
    def display_menu(self, window):
        BLACK = (0, 0, 0)
        WHITE = (255, 255, 255)
        font = pygame.font.Font(None, 36)
        for i, option in enumerate(self.options):
            if i == self.selected_option:
                text = font.render(f"> {option}", True, WHITE)
            else:
                text = font.render(option, True, WHITE)
            text_rect = text.get_rect(center=(self.width // 2, self.height // 2 + i * 50))
            window.blit(text, text_rect)
    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.selected_option = (self.selected_option - 1) % len(self.options)
                elif event.key == pygame.K_DOWN:
                    self.selected_option = (self.selected_option + 1) % len(self.options)
                elif event.key == pygame.K_RETURN:
                    selected_option = self.options[self.selected_option]
                    self.select_option(selected_option)