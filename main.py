import pygame
import neat
import pickle
import sys
import argparse

from constants import WIDTH, HEIGHT, FPS
from game import assets
from game.game import Game
from game.renderer import Renderer
from ai.trainer import get_config, get_population, eval_genomes


def main():
    parser = argparse.ArgumentParser(description="BirdBrain AI Controls")
    parser.add_argument(
        "mode",
        choices=["train", "train-silent", "show", "co-op"],
        help="train: see learning | train-silent: fast learning | show: watch AI | co-op: play vs AI",
    )
    args = parser.parse_args()

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    sprites = assets.load_sprites()
    clock = pygame.time.Clock()
    game = Game(sprites)
    renderer = Renderer(screen)

    config = get_config()

    if args.mode in ["train", "train-silent"]:
        population = get_population(config)

        visualize = True if args.mode == "train" else False

        winner = population.run(
            lambda genomes, config: eval_genomes(
                genomes,
                config,
                game,
                sprites,
                renderer if visualize else None,
                clock if visualize else None,
            ),
            n=50,
        )

        with open("best_bird.pkl", "wb") as f:
            pickle.dump(winner, f)
        print("\nBest bird saved to best_bird.pkl!")

    elif args.mode == "show":
        net = load_trained_bird(config)
        run_game_loop(game, sprites, renderer, clock, ai_net=net)

    elif args.mode == "co-op":
        net = load_trained_bird(config)
        run_game_loop(game, sprites, renderer, clock, ai_net=net, human_mode=True)

    pygame.quit()


def load_trained_bird(config):
    try:
        with open("best_bird.pkl", "rb") as f:
            genome = pickle.load(f)
        return neat.nn.FeedForwardNetwork.create(genome, config)
    except FileNotFoundError:
        print("Error: best_bird.pkl not found. Train first!")
        sys.exit()


def run_game_loop(game, sprites, renderer, clock, ai_net, human_mode=False):
    num_birds = 2 if human_mode else 1

    while True:
        game.reset(num_birds, sprites)
        running = True
        while running:
            human_action = 0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if (
                    human_mode
                    and event.type == pygame.KEYDOWN
                    and event.key == pygame.K_SPACE
                ):
                    human_action = 1

            actions = []
            for i, bird in enumerate(game.birds):
                if i == 0 and human_mode:
                    actions.append(human_action)
                elif bird.is_alive:
                    output = ai_net.activate(game.get_state(bird))
                    actions.append(1 if output[0] > 0.5 else 0)
                else:
                    actions.append(0)

            game.update(actions)
            renderer.draw(game)
            pygame.display.flip()
            clock.tick(FPS)

            if all(not b.is_alive for b in game.birds):
                running = False


if __name__ == "__main__":
    main()
