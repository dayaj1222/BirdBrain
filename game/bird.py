import pygame

from game.config import ANIMATION_SPEED, GRAVITY

import pygame
from game.config import ANIMATION_SPEED, GRAVITY


class Bird:
    def __init__(self, frames) -> None:
        self.vely = 0.1
        self.is_alive = True
        self.frame_alive = 0
        self.score = 0

        self.frames = frames
        self.frame_index = 0
        self.sprite = self.frames[0]

        w, h = frames[0].get_size()
        self.rect = pygame.Rect(100, 300, w - 5, h - 5)

    def update(self, action):
        if not self.is_alive:
            return

        if action:
            self.vely = -10

        self.vely += GRAVITY

        if self.vely > 15:
            self.vely = 15

        self.rect.y += self.vely

        if self.rect.bottom > 600 or self.rect.top < 0:
            self.is_alive = False
            self.rect.y = 600 if self.rect.bottom > 600 else 0

        self.frame_alive += 1
        if self.frame_alive % ANIMATION_SPEED == 0:
            self.frame_index = (self.frame_index + 1) % len(self.frames)

        self.sprite = self.frames[self.frame_index]
