from random import randrange
import pygame


def get_food_postion(frame_size_x: int, frame_size_y: int, square_size: int) -> list:
    return [
        randrange(1, (frame_size_x // square_size)) * square_size,
        randrange(1, (frame_size_y // square_size)) * square_size,
    ]


def display_score(choice, color, font, size, score, frame_size_x, frame_size_y) -> list:
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render(f"Score: {score}", True, color)
    score_rect = score_surface.get_rect()
    if choice == 1:
        score_rect.midtop = (frame_size_x / 10, 15)
    else:
        score_rect.midtop = (frame_size_x / 2, frame_size_y / 1.25)
    return score_surface, score_rect
