import pygame
import random

from snake import Snake
from apple import Apple

pygame.init()

WIDTH, HEIGHT = 20 * 16, 20 * 16
FPS = 10

window = pygame.display.set_mode((WIDTH, HEIGHT))

black = pygame.Color(0, 0, 0)
green = pygame.Color(0, 255, 0)
red = pygame.Color(255, 0, 0)

snake = Snake(window, green, 20)
apple = Apple(window, 20, red)

lose_text = pygame.font.SysFont("Arial Rounded", 50).render("You lost!", True, red)


def generate_apple_position():
    return random.randint(0, 16), random.randint(0, 16)


def main(window=window):
    clock = pygame.time.Clock()
    run = True
    moving_direction = "right"
    should_increase = False

    apple_x = random.randint(1, 15)
    apple_y = random.randint(1, 15)
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        window.fill(black)

        # Handling apple spawning

        if (
            apple_x == snake.snake_positions[-1][0]
            and apple_y == snake.snake_positions[-1][1]
        ):
            should_increase = True
            apple_x, apple_y = generate_apple_position()
        else:
            should_increase = False

        apple.spawn((apple_x, apple_y))

        # Handling movement

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            if moving_direction != "right":
                moving_direction = "left"
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            if moving_direction != "left":
                moving_direction = "right"
        elif keys[pygame.K_UP] or keys[pygame.K_w]:
            if moving_direction != "down":
                moving_direction = "up"
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            if moving_direction != "up":
                moving_direction = "down"

        if (
            snake.snake_positions[-1] in snake.snake_positions[:-1]
            or snake.snake_positions[-1][0] < 0
            or snake.snake_positions[-1][0] > 15
            or snake.snake_positions[-1][1] < 0
            or snake.snake_positions[-1][1] > 15
        ):
            window.blit(
                lose_text, (WIDTH // 2 - lose_text.get_width() // 2, HEIGHT // 2)
            )
            run = False

        if should_increase:
            snake.move(moving_direction, True)
        else:
            snake.move(moving_direction)

        snake.draw()
        pygame.display.flip()

    pygame.quit()
    quit()


if __name__ == "__main__":
    main(window)
