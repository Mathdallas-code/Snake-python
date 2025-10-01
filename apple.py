import pygame


class Apple(pygame.sprite.Sprite):
    def __init__(self, window, size, color):
        super().__init__()
        self.window = window
        self.size = size
        self.color = color

    def spawn(self, position):
        pygame.draw.rect(
            self.window,
            self.color,
            pygame.Rect((position[0] * 20, position[1] * 20), (self.size, self.size)),
        )
