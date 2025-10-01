import pygame


class Snake(pygame.sprite.Sprite):
    def __init__(self, window, size):
        self.snake_positions = [
            (0, 0),
            (1, 0),
            (2, 0),
        ]
        self.size = size
        self.window = window

    def move(self, direction, increase=False):
        if not increase:
            self.snake_positions.pop(0)
        last_position = self.snake_positions[-1]
        if direction == "left":
            self.snake_positions.append((last_position[0] - 1, last_position[1]))
        elif direction == "right":
            self.snake_positions.append((last_position[0] + 1, last_position[1]))
        elif direction == "up":
            self.snake_positions.append((last_position[0], last_position[1] - 1))
        elif direction == "down":
            self.snake_positions.append((last_position[0], last_position[1] + 1))

    def draw(self):
        i = 0
        color = (0, 209, 0)
        for snake_position in self.snake_positions:
            i += 1
            if i % 2 == 0:
                color = (0, 178, 0)
            else:
                color = (0, 209, 0)
            pygame.draw.rect(
                self.window,
                color,
                pygame.Rect(
                    (snake_position[0] * self.size, snake_position[1] * self.size),
                    (self.size, self.size),
                ),
            )
