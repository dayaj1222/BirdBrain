import pygame

from constants import HEIGHT, WIDTH
from game.config import GAP, PIPE_SPEED, Position


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

        self.sprite = pygame.transform.scale(sprite, (w, self.height))
        self.rect = pygame.Rect(WIDTH, y, w, self.height)

    def update(self):
        self.rect.x -= PIPE_SPEED
