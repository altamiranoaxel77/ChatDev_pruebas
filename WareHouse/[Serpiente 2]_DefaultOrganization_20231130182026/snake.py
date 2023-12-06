'''
This file contains the SnakeGame class that represents the snake game.
'''
import tkinter as tk
import random
class SnakeGame(tk.Canvas):
    def __init__(self, master):
        super().__init__(master, width=400, height=400, bg="black")
        self.snake = [(200, 200), (210, 200), (220, 200)]
        self.apple = self.create_apple()
        self.direction = "Right"
        self.bind_all("<Key>", self.on_key_press)
        self.score = 0
        self.delay = 100
        self.game_over = False
        self.score_text = self.create_text(10, 10, anchor="nw", fill="white", text="Score: 0", font=("Arial", 14, "bold"))
        self.snake_body = self.create_snake()
        self.move_snake()
    def create_snake(self):
        snake_body = []
        for x, y in self.snake:
            snake_body.append(self.create_rectangle(x, y, x+10, y+10, fill="green"))
        return snake_body
    def create_apple(self):
        x = random.randint(0, 39) * 10
        y = random.randint(0, 39) * 10
        return self.create_oval(x, y, x+10, y+10, fill="red")
    def move_snake(self):
        if not self.game_over:
            head_x, head_y = self.snake[0]
            if self.direction == "Right":
                head_x += 10
            elif self.direction == "Left":
                head_x -= 10
            elif self.direction == "Up":
                head_y -= 10
            elif self.direction == "Down":
                head_y += 10
            self.snake.insert(0, (head_x, head_y))
            if self.check_collision():
                self.game_over = True
                self.create_text(200, 200, text="Game Over", fill="white", font=("Arial", 24, "bold"))
                self.create_text(200, 230, text="Press 'Play Again' to restart", fill="white", font=("Arial", 16, "bold"))
            else:
                if head_x == self.coords(self.apple)[0] and head_y == self.coords(self.apple)[1]:
                    self.score += 1
                    self.delete(self.apple)
                    self.apple = self.create_apple()
                    tail_x, tail_y = self.snake[-1]  # Get the coordinates of the tail segment
                    self.snake_body.append(self.create_rectangle(tail_x, tail_y, tail_x+10, tail_y+10, fill="green"))  # Add new body segment
                else:
                    self.delete(self.snake.pop())  # Remove the tail segment instead of the last segment
            self.update_score()
            self.after(self.delay, self.move_snake)
    def check_collision(self):
        head_x, head_y = self.snake[0]
        return (
            head_x < 0 or head_x >= 400 or
            head_y < 0 or head_y >= 400 or
            (head_x, head_y) in self.snake[1:]
        )
    def update_score(self):
        self.itemconfig(self.score_text, text="Score: " + str(self.score))
    def on_key_press(self, event):
        if event.keysym == "Right" and self.direction != "Left":
            self.direction = "Right"
        elif event.keysym == "Left" and self.direction != "Right":
            self.direction = "Left"
        elif event.keysym == "Up" and self.direction != "Down":
            self.direction = "Up"
        elif event.keysym == "Down" and self.direction != "Up":
            self.direction = "Down"
    def reset(self):
        self.delete(tk.ALL)
        self.snake = [(200, 200), (210, 200), (220, 200)]
        self.apple = self.create_apple()
        self.direction = "Right"
        self.score = 0
        self.game_over = False
        self.score_text = self.create_text(10, 10, anchor="nw", fill="white", text="Score: 0", font=("Arial", 14, "bold"))
        self.snake_body = self.create_snake()
    def start(self):
        self.move_snake()