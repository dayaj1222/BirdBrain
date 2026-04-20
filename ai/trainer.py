import neat
import os
import pygame
import sys


def get_config():
    config_path = os.path.join(os.path.dirname(__file__), "config.txt")
    return neat.Config(
        neat.DefaultGenome,
        neat.DefaultReproduction,
        neat.DefaultSpeciesSet,
        neat.DefaultStagnation,
        config_path,
    )


def get_population(config):
    population = neat.Population(config)
    population.add_reporter(neat.StdOutReporter(True))
    population.add_reporter(neat.StatisticsReporter())
    return population


def eval_genomes(genomes, config, game, sprites, renderer=None, clock=None):
    nets = []
    birds_genomes = []

    # FIX: Unpack the tuple here using _, genome
    for _, genome in genomes:
        genome.fitness = 0
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        nets.append(net)
        birds_genomes.append(genome)

    game.reset(len(genomes), sprites)

    while any(bird.is_alive for bird in game.birds):
        if renderer:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

        actions = []
        for i, bird in enumerate(game.birds):
            if not bird.is_alive:
                actions.append(0)
                continue

            # Access the pre-built network and genome by index
            output = nets[i].activate(game.get_state(bird))
            action = 1 if output[0] > 0.5 else 0
            actions.append(action)

            # Update fitness on the actual genome object
            birds_genomes[i].fitness = bird.score + (bird.frame_alive * 0.1)

        game.update(actions)

        if renderer:
            renderer.draw(game)
            pygame.display.flip()
            if clock:
                clock.tick(60)
