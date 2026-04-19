import pygame


def load_sprites():
    return {
        "bird": {
            "red": [
                pygame.image.load("sprites/redbird-upflap.bmp").convert_alpha(),
                pygame.image.load("sprites/redbird-midflap.bmp").convert_alpha(),
                pygame.image.load("sprites/redbird-downflap.bmp").convert_alpha(),
            ]
        },
        "pipes": [
            pygame.image.load("sprites/pipe-green.bmp").convert_alpha(),
            pygame.image.load("sprites/pipe-red.bmp").convert_alpha(),
        ],
        "background": {
            "day": pygame.image.load("sprites/background-day.bmp").convert_alpha(),
            "night": pygame.image.load("sprites/background-night.bmp").convert_alpha(),
        },
        "base": pygame.image.load("sprites/base.bmp").convert_alpha(),
        "numbers": [
            pygame.image.load(f"sprites/{i}.bmp").convert_alpha() for i in range(10)
        ],
    }
