import pygame

from game.game import Game


class Renderer:
    def __init__(self, screen: pygame.Surface) -> None:
        self.screen = screen

    def draw(self, game: Game):
        bg = game.sprites["background"]["day"]

        # scale to fit height, maintain aspect ratio
        bg_h = self.screen.get_height()
        bg_w = int(bg.get_width() * (bg_h / bg.get_height()))
        bg = pygame.transform.scale(bg, (bg_w, bg_h))

        # tile horizontally until screen is covered
        x = 0
        while x < self.screen.get_width():
            self.screen.blit(bg, (x, 0))
            x += bg_w

        for pipe in game.pipes:
            self.screen.blit(pipe.sprite, pipe.rect)
        for bird in game.birds:
            if bird.is_alive:
                self.screen.blit(bird.sprite, bird.rect)

        pygame.display.flip()
