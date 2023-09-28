"""Main code for Speed Racer. Speed Racer is a classic 2d racing game
where you can switch what lane you're in to avoid obstacles."""

import pygame, sys, random 
from pygame.locals import *
from pathlib import Path 

# Set up window constants.
WINDOWWIDTH = 1000
WINDOWHEIGHT = 600
TRACKWIDTH = 900
TRACKHEIGHT = 500
CENTERX = WINDOWWIDTH / 2
CENTERY = WINDOWHEIGHT / 2

# Set arrow constants.
ARROWSPAWNRATE = 60
ARROWSPEED = 10

# Set obstacle constants.
MINSPAWNTIME = 50
MAXSPAWNTIME = 100
OBSTACLESPEED = 10

# Color constants.
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHTGRAY = (200, 200, 200)
LIGHTRED = (255, 0, 0)
RED = (255, 0 , 0)
LIGHTGREEN = (0, 255, 0)
GREEN = (0, 255, 0)
LIGHTBLUE = (0, 0, 255)
BLUE = (0, 0, 255)
LIGHTYELLOW = (255, 255, 0)
YELLOW = (255, 255, 0)
LIGHTORANGE = (255, 165, 0)
ORANGE = (255, 165, 0)
LIGHTPURPLE = (255, 0, 255)
PURPLE = (255, 0, 255)
LIGHTPINK = (255, 192, 203)
PINK = (255, 192, 203)
LIGHTBROWN = (139, 69, 19)
BROWN = (139, 69, 19)
LIGHTCYAN = (0, 255, 255)
CYAN = (0, 255, 255)
BG_COLOR = LIGHTGRAY

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
    global car_lane, score, arrows, arrow_frame, obstacles, obstacle_frame

    # Start the music.
    #pygame.mixer.music.play(-1, 0.0)

    # Reset game variables.
    arrows = []
    score = 0
    car_lane = 2
    arrow_frame = 0
    obstacle_frame = 0
    obstacles = []
    
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

                # Check for arrow keys or WASD, and move the car.
                if event.key in (K_UP, K_w):
                    move_car_up(True)
                
                elif event.key in (K_DOWN, K_s):
                    move_car_up(False)

        # Draw the game. Start with the background.
        DISPLAYSURF.fill(BG_COLOR)
        DISPLAYSURF.blit(bg_img, bg_rect)

        # Update the score.
        score += 1

        # Update the arrows.
        spawn_arrows()
        update_arrows()

        # Update the obstacles.
        spawn_obstacles()
        update_obstacles()

        # Draw the player.
        DISPLAYSURF.blit(car_img, car_rect)

        # Update the game.
        pygame.display.update()
        MAINCLOCK.tick(FPS)



def update_obstacles():
    """Update the currently active obstacles."""
    global obstacles

    for obstacle in obstacles[:]:
        # Move the obstacle.
        obstacle["rect"].x -= OBSTACLESPEED

        # Check if the obstacle has hit the player.
        if obstacle['rect'].colliderect(car_rect):
            terminate()

        # Check if the obstacle is off the screen.
        if obstacle["rect"].x < 75:
            # Remove the obstacle.
            obstacles.remove(obstacle)

        # Draw the obstacle.
        DISPLAYSURF.blit(obstacle["img"], obstacle["rect"])
    

def spawn_obstacles():
    """Spawn obstacles at random intervals."""
    global obstacles, obstacle_frame

    if obstacle_frame >= random.randint(MINSPAWNTIME, MAXSPAWNTIME):
        # Reset the obstacle frame.
        obstacle_frame = 0

        # Choose a random obstacle to spawn.
        obstacle = "rock"

        # Spawn the obstacle.
        if obstacle == "rock":
            obstacle = {}
            obstacle["img"] = rock_img
            obstacle_rect = rock_img.get_rect()

        # Set the obstacle's lane.
        lane = random.randint(1, 3)
        if lane == 1:
            y_pos = CENTERY - 160
        elif lane == 2:
            y_pos = CENTERY
        else:
            y_pos = CENTERY + 160

        # Set the obstacle's position.
        obstacle_rect.center = (TRACKWIDTH, y_pos)
        obstacle["rect"] = obstacle_rect

        # Add the obstacle to the list.
        obstacles.append(obstacle)

    else:
        obstacle_frame += 1


def update_arrows():
    """Update the currently active arrows."""
    global arrows

    for arrow in arrows[:]:
        # Move the arrow.
        arrow.x -= ARROWSPEED

        # Check if the arrow is off the screen.
        if arrow.x < 75:
            # Remove the arrow.
            arrows.remove(arrow)

        # Draw the arrow.
        DISPLAYSURF.blit(arrow_img, (arrow.x, arrow.y))


def spawn_arrows():
    """Spawn arrows if the time is right."""
    global arrows, arrow_frame 

    offset = 160
    y_positions = [CENTERY - offset, CENTERY, CENTERY + offset]

    if arrow_frame >= ARROWSPAWNRATE:
        # Reset the arrow frame.
        arrow_frame = 0

        # It's time to spawn arrows.
        for y_pos in y_positions:
            arrow_rect = arrow_img.get_rect()
            arrow_rect.center = (TRACKWIDTH, y_pos)
            arrows.append(arrow_rect)

    else:
        arrow_frame += 1


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
    terminate()


def load_assets():
    """Load the game's assets."""
    global car_img, car_rect, bg_img, bg_rect, arrow_img, rock_img

    # Load the music.
    pygame.mixer.music.load("sounds/chaoz_impact.mp3")

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
    arrow_img = pygame.image.load("images/arrow.png")
    arrow_img = pygame.transform.scale(arrow_img, (90, 90))

    # Load in the obstacles, starting with the rock.
    rock_img = pygame.image.load("images/rock.png")
    rock_img = pygame.transform.scale(rock_img, (100, 100))

    return


def terminate():
    """Close out of the game."""

    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()