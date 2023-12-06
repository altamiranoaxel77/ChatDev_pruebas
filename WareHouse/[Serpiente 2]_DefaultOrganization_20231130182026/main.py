'''
This is the main file that runs the snake game.
'''
import tkinter as tk
from snake import SnakeGame
def play_again():
    game.reset()
    game.start()
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Snake Game")
    game = SnakeGame(root)
    game.pack()
    play_again_button = tk.Button(root, text="Play Again", command=play_again)
    play_again_button.pack()
    game.start()
    root.mainloop()