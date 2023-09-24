"""Main code for Speed Racer. Speed Racer is a classic 2d racing game
where you can switch what lane you're in to avoid obstacles."""

import pygame, sys, random 
from pygame.locals import *
from pathlib import Path 

# Set up window constants.
WINDOWWIDTH = 1000
WINDOWHEIGHT = 600
CENTERX = WINDOWWIDTH / 2
CENTERY = WINDOWHEIGHT / 2

# Color constants.
WHITE = (255, 255, 255)

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

    # Load in the assets.
    load_assets()

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
    global car_lane

    # Start the music.
    pygame.mixer.music.load("sounds/music.wav")
    pygame.mixer.music.play(-1, 0.0)

    # Define game variables.
    score = 0
    car_lane = 2
    
    # Start the car on the left side center of the screen.
    car_rect.midleft = (10, CENTERY)

    # Run the game running loop.
    while True:
        
        # Handle events.
        for event in pygame.event.get():

            # Check for quit.
            if event.type == QUIT:
                terminate()

            # Check if the player is pressing a key.
            if event.type == KEYDOWN:

                # Check if player is pressing escape.
                if event.key == K_ESCAPE:
                    terminate()

            # Check if the player has released a key.
            if event.type == KEYUP:

                # Check for arrow keys or WASD.
                if event.key in (K_UP, K_w):
                    move_car_up(True)
                
                elif event.key in (K_DOWN, K_s):
                    move_car_up(False)

        # Draw the game.
        DISPLAYSURF.blit(bg_img, bg_rect)

        # Draw the player.
        DISPLAYSURF.blit(car_img, car_rect)

        # Update the game.
        pygame.display.update()
        MAINCLOCK.tick(FPS)


def move_car_up(up):
    """Move the car up a lane."""
    global car_lane

    # Check what direction the car should move.
    if up:
        # Check if the car can go up a lane.
        if car_lane != 3:
            # Move the car up.
            for i in range(0, 80):
                car_rect.y -= 2

            # Update the car's lane.
            car_lane += 1

    else:
        # Check if the car can go down a lane.
        if car_lane != 1:
            # Move the car down.
            for i in range(0, 80):
                car_rect.y += 2

            # Update the car's lane.
            car_lane -= 1


def game_over():
    """Run the game's game over screen."""
    pass


def load_assets():
    """Load the game's assets."""
    global car_img, car_rect, arrow, bg_img, bg_rect

    # Load in the background and position it.
    bg_image = pygame.image.load("images/race_track.png")
    bg_img = pygame.transform.scale(bg_image, (900, 500))
    bg_rect = bg_img.get_rect()
    bg_rect.center = (CENTERX, CENTERY)

    # Load the car sprite.
    car_img = pygame.image.load('images/car.png')
    car_img = pygame.transform.scale(car_img, (300, 100))
    car_rect = car_img.get_rect()

    # Load the arrow image.
    arrow = pygame.image.load("images/arrow.png")

    return


def terminate():
    """Close out of the game."""

    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()