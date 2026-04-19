import random

import pygame

from constants import HEIGHT
from game.bird import Bird
from game.config import Position
from game.pipe import Pipe


class Game:
    def __init__(self, sprites, num_birds: int = 1) -> None:
        self.pipes: list[Pipe] = []
        self.birds: list[Bird] = []
        self.sprites = sprites
        self.score = 0
        self.frame = 0
        self.PIPE_INTERVAL = 90  # spawn pipe every 90 frames

        self._spawn_birds(num_birds)
        self._spawn_pipe()

    def update(self, actions: list[int]):
        self.frame += 1

        for bird, action in zip(self.birds, actions):
            bird.update(action)

        for pipe in self.pipes:
            pipe.update()

        if self.frame % self.PIPE_INTERVAL == 0:
            self._spawn_pipe()

        self._check_collisions()
        # remove off screen pipes
        self.pipes = [p for p in self.pipes if p.rect.x > -100]

    def _spawn_birds(self, n: int):
        frames = self.sprites["bird"]["red"]
        self.birds = [Bird(frames) for _ in range(n)]

    def _spawn_pipe(self):
        gap_y = random.randint(150, 400)
        sprite = random.choice(self.sprites["pipes"])
        self.pipes.append(Pipe(sprite, Position.DOWN, gap_y))
        self.pipes.append(Pipe(sprite, Position.UP, gap_y))

    def _check_collisions(self):
        for bird in self.birds:
            if not bird.is_alive:
                continue

            # hit ground or ceiling
            if bird.rect.y + bird.rect.height >= HEIGHT or bird.rect.y <= 0:
                bird.is_alive = False
                continue

            for pipe in self.pipes:
                if bird.rect.colliderect(pipe.rect):
                    bird.is_alive = False
                    break

            if (
                pipe.dir == Position.DOWN
                and not pipe.passed
                and pipe.rect.x + pipe.rect.width < bird.rect.x
            ):
                pipe.passed = True
                bird.score += 1
