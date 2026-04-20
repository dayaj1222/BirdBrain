import pygame

from constants import HEIGHT, WIDTH
from game.config import GAP, PIPE_SPEED, TIP_HEIGHT, Position


class Pipe:
    def __init__(self, sprite, direction: Position, gap_y: int):
        self.dir = direction
        w = sprite.get_width()
        self.passed = False

        if direction == Position.DOWN:
            y = gap_y + GAP // 2
            self.height = HEIGHT - y
        else:
            sprite = pygame.transform.flip(sprite, False, True)
            y = 0
            self.height = gap_y - GAP // 2

        sprite_h = sprite.get_height()

        tip = sprite.subsurface((0, sprite_h - TIP_HEIGHT, w, TIP_HEIGHT))
        body = sprite.subsurface((0, 0, w, sprite_h - TIP_HEIGHT))

        body_height = self.height - TIP_HEIGHT
        scaled_body = pygame.transform.scale(body, (w, body_height))

        final = pygame.Surface((w, self.height), pygame.SRCALPHA)
        final.blit(scaled_body, (0, 0))
        final.blit(tip, (0, body_height))

        self.sprite = final
        self.rect = pygame.Rect(WIDTH, y, w, self.height)

    def update(self):
        self.rect.x -= PIPE_SPEED
