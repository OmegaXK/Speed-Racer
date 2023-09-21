"""Main code for Speed Racer. Speed Racer is a classic 2d racing game
where you can switch what lane you're in to avoid obstacles."""

import pygame, sys, random 
from pygame.locals import *
from pathlib import Path 

# Set up window constants.
WINDOWWIDTH = 800
WINDOWHEIGHT = 800

# Other constants.
FPS = 60

def main():
    """Run the overall script."""
    global DISPLAYSURF, MAINCLOCK

    # Initialize pygame and set up a clock.
    pygame.init()
    MAINCLOCK = pygame.time.Clock()

    # Set up the window.
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption("Speed Racer")

    # Run the main game loop.
    title_screen()
    while True:
        run_game()
        game_over()


def title_screen():
    """Run the game's title screen."""
    pass 


def run_game():
    """Run the game, and return when the player hits an obstacle."""
    pass 


def game_over():
    """Run the game's game over screen."""


if __name__ == '__main__':
    main()