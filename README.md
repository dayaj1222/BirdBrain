# 🐦 BirdBrain

> [PROJECT_DESCRIPTION_PLACEHOLDER]

## Overview

BirdBrain is an AI-powered Flappy Bird game where neural networks learn to play autonomously using NEAT (NeuroEvolution of Augmenting Topologies). Train intelligent agents, watch them evolve, or challenge the AI in co-op mode.

## Features

-  **AI Training** - Train neural networks using NEAT algorithm
-  **Visual Learning** - Watch the AI learn in real-time
-  **Co-op Mode** - Play alongside the trained AI
-  **Silent Training** - Fast training without visualization

## Tech Stack

- **Python** 3.14+
- **NEAT-Python** - Neuroevolution framework
- **Pygame** - Game engine

## Installation

```bash
# Clone the repository
git clone [REPO_URL_PLACEHOLDER]
cd BirdBrain

# Install dependencies
pip install neat-python, pygame

# or with uv
uv sync
```

## Usage

### Train an AI Agent

```bash
# Train with visualization (see learning in real-time)
python main.py train

# Fast training without visualization
python main.py train-silent
```

### Play with Trained AI

```bash
# Watch the trained AI play
python main.py show

# Play cooperatively against the AI
python main.py co-op
```

## Controls

- **Co-op Mode:** Press `SPACE` to make your bird jump
- **Exit:** Close the window or press the close button

## Project Structure

```
BirdBrain/
├── main.py              # Entry point & game loop
├── constants.py         # Game configuration
├── assets.py            # Asset loading
├── game/                # Game logic
│   ├── game.py          # Core game mechanics
│   └── renderer.py      # Graphics rendering
├── ai/                  # AI & training logic
│   └── trainer.py       # NEAT training & evolution
├── sprites/             # Game sprites
└── best_bird.pkl        # Trained model (auto-generated)
```

## Training Details

- **Algorithm:** NEAT (NeuroEvolution of Augmenting Topologies)
- **Population Size:** 50
- **Fitness Function:** Uses Score and Frame alive 
_PLACEHOLDER]

## Screenshots

