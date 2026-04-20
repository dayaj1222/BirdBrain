import random

from constants import HEIGHT, WIDTH
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
        self.PIPE_INTERVAL = 90

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

    def get_state(self, bird: Bird) -> list[float]:

        next_pipe = next(
            (
                p
                for p in self.pipes
                if p.dir == Position.DOWN and p.rect.x + p.rect.width > bird.rect.x
            ),
            None,
        )
        if next_pipe is None:
            return [0, 0, 0]

        return [
            bird.rect.y / HEIGHT,
            next_pipe.rect.x / WIDTH,
            (next_pipe.rect.y) / HEIGHT,
        ]

    def reset(self, num_birds: int, sprites):
        self.pipes = []
        self.birds = []
        self.score = 0
        self.frame = 0
        self._spawn_birds(num_birds)
        self._spawn_pipe()
