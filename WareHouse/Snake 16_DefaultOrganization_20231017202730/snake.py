import pygame
class Snake:
    def __init__(self, window_width, window_height):
        self.window_width = window_width
        self.window_height = window_height
        self.size = 20
        self.head = pygame.Rect(window_width // 2, window_height // 2, self.size, self.size)
        self.body = [self.head]
        self.direction = pygame.Vector2(1, 0)
        self.speed = 1
    def update(self):
        self.move()
        self.check_boundary()
    def render(self, window):
        for segment in self.body:
            pygame.draw.rect(window, (0, 255, 0), segment)
    def move(self):
        self.body.insert(0, self.body[0].move(self.direction * self.size))
        self.body.pop()
    def check_boundary(self):
        if (
            self.head.left < 0
            or self.head.right > self.window_width
            or self.head.top < 0
            or self.head.bottom > self.window_height
        ):
            self.reset()
    def grow(self):
        tail = self.body[-1]
        self.body.append(pygame.Rect(tail.x, tail.y, self.size, self.size))
    def is_colliding(self):
        for segment in self.body[1:]:
            if self.head.colliderect(segment):
                return True
        return False
    def reset(self):
        self.head = pygame.Rect(self.window_width // 2, self.window_height // 2, self.size, self.size)
        self.body = [self.head]
        self.direction = pygame.Vector2(1, 0)
        self.speed = 1
    def is_lost(self):
        return self.is_colliding() or self.is_out_of_bounds()
    def is_out_of_bounds(self):
        return (
            self.head.left < 0
            or self.head.right > self.window_width
            or self.head.top < 0
            or self.head.bottom > self.window_height
        )