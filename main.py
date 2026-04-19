import pygame

from constants import HEIGHT, WIDTH
from game import assets
from game.game import Game
from game.renderer import Renderer


def main():

    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    sprites = assets.load_sprites()

    clock = pygame.time.Clock()

    game = Game(sprites)
    renderer = Renderer(screen)
    running = True

    while running:
        actions = [0]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                actions = [1]

        if all(not bird.is_alive for bird in game.birds):
            running = False
        game.update(actions)
        renderer.draw(game)
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
