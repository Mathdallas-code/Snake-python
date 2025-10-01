import pygame
import random
import math

from snake import Snake
from apple import Apple

pygame.init()
pygame.font.init()
pygame.mixer.init()

rows_of_squares = 20
cols_of_squares = 12

WIDTH, HEIGHT = 30 * rows_of_squares, 30 * cols_of_squares
FPS = 10

window = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Snake 🐍")

white = pygame.Color(255, 255, 255)
green = pygame.Color(0, 255, 0)
red = pygame.Color(255, 0, 0)

snake = Snake(window, 30)
apple = Apple(window, 30, red)

boldpixels = pygame.font.Font("Assets/BoldPixels.otf", 75)

lose_text = boldpixels.render("You lost! :(", True, red)
win_text = boldpixels.render("You won! :D", True, green)

lose_sound = pygame.mixer.Sound("Assets/lose.wav")
powerup_sound = pygame.mixer.Sound("Assets/powerup.wav")
pygame.mixer.music.load("Assets/bg_music.mp3")

pygame.mixer.music.set_volume(0.3)
text_surface_alpha = pygame.Surface((300, 200), pygame.SRCALPHA)
# Blit the rendered text onto the alpha surface

bg_color = (1, 5, 36)


def generate_apple_position():
    return random.randint(1, rows_of_squares - 1), random.randint(
        1, cols_of_squares - 1
    )


def game():
    clock = pygame.time.Clock()
    run = True
    moving_direction = "right"
    should_increase = False

    apple_x = random.randint(1, rows_of_squares - 1)
    apple_y = random.randint(1, cols_of_squares - 1)
    snake.snake_positions = [
        (0, 0),
        (1, 0),
        (2, 0),
    ]
    hover_value = 0.0
    pygame.mixer.music.play(-1)
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        hover_value += 0.1
        window.fill((bg_color))
        score = str(len(snake.snake_positions))
        score_text = boldpixels.render(score, True, (255, 0, 00, 30))
        lose_text_under = boldpixels.render("Your score is " + score, True, white)
        text_surface_alpha.blit(score_text, (0, 0))

        text_surface_alpha.set_alpha(128)

        # Handling apple spawning

        if (apple_x, apple_y) in snake.snake_positions:
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

        if should_increase:
            snake.move(moving_direction, True)
            pygame.mixer.Sound.play(powerup_sound)
        else:
            snake.move(moving_direction)
        snake.draw()
        window.blit(
            text_surface_alpha,
            (
                WIDTH // 2 - score_text.get_width() // 2,
                (HEIGHT // 2 - score_text.get_height() // 2)
                - math.sin(hover_value * 2) * 20,
            ),
        )
        if (
            snake.snake_positions[-1] in snake.snake_positions[:-1]
            or snake.snake_positions[-1][0] < 0
            or snake.snake_positions[-1][0] > rows_of_squares - 1
            or snake.snake_positions[-1][1] < 0
            or snake.snake_positions[-1][1] > cols_of_squares - 1
        ):
            run = False
            pygame.mixer.Sound.play(lose_sound)
            pygame.mixer.music.stop()
            window.fill((bg_color))
            window.blit(
                lose_text,
                (
                    WIDTH // 2 - lose_text.get_width() // 2,
                    50,
                ),
            )
            window.blit(
                lose_text_under,
                (
                    WIDTH // 2 - lose_text_under.get_width() // 2,
                    125,
                ),
            )
        if len(snake.snake_positions) == rows_of_squares * cols_of_squares:
            run = False
            window.fill((bg_color))

            window.blit(
                win_text,
                (
                    WIDTH // 2 - win_text.get_width() // 2,
                    50,
                ),
            )

        pygame.display.flip()
        text_surface_alpha.fill((0, 0, 0, 0))


def main(window=window):
    while True:
        game()
        pygame.time.delay(1500)
        pygame.display.flip()


if __name__ == "__main__":
    main(window)
