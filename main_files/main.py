"""Main code for Speed Racer. Speed Racer is a classic 2d racing game
where you can switch what lane you're in to avoid obstacles."""

import pygame, sys, random 
from pygame.locals import *
from pathlib import Path
from webbrowser import open 

# Set up window constants.
WINDOWWIDTH = 1000
WINDOWHEIGHT = 600
TRACKWIDTH = 900
TRACKHEIGHT = 500
CENTERX = WINDOWWIDTH / 2
CENTERY = WINDOWHEIGHT / 2

# Set arrow constants.
ARROWSPAWNRATE = 60

# Set obstacle constants.
ROCK = 'rock'
BARREL = 'barrel'
OIL = 'oil'
OBSTACLES = [ROCK, BARREL, OIL]

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

    # Set up the title screen fonts.
    titlefont = create_font(100)
    smallfont = create_font(40)
    buttonfont = create_font(75)

    # Set up the title screen text.
    titletext = titlefont.render('Speed Racer', False, RED, WHITE)
    titlerect = titletext.get_rect()
    titlerect.center = (CENTERX, CENTERY - 200)

    # Set up the credits text.
    bytext = smallfont.render('By Collin Maryniak', False, BLACK, WHITE)
    byrect = bytext.get_rect()
    byrect.center = (CENTERX, CENTERY - 100)

    # Set up the GitHub text.
    gitsurf = smallfont.render("Visit this game's GitHub page below.", False,
                               BLACK, WHITE)
    gitrect = gitsurf.get_rect()
    gitrect.center = (CENTERX, CENTERY)

    # Set up the buttons.
    gitbutton = pygame.Rect(0, 0, 300, 100)
    gitbutton.center = (CENTERX - 200, CENTERY + 100)

    startbutton = pygame.Rect(0, 0, 300, 100)
    startbutton.center = (CENTERX + 200, CENTERY + 100)

    # Add the text to go on top of the github button.
    gittext = buttonfont.render('GitHub', False, PURPLE)
    gittextrect = gittext.get_rect()
    gittextrect.center = gitbutton.center

    # Add the text to go on top of the start button.
    starttext = buttonfont.render('Start', False, GREEN)
    starttextrect = starttext.get_rect()
    starttextrect.center = startbutton.center

    # Run the title screen loop.
    while True:
        # Check for events.
        for event in pygame.event.get():
            # Check for quit.
            if event.type == QUIT:
                terminate()

            # Check if the player is pressing a key.
            if event.type == KEYDOWN:
                # Check for ESCAPE key.
                if event.key == K_ESCAPE:
                    terminate()

            # Check if the player is clicking.
            if event.type == MOUSEBUTTONDOWN:
                # Check if the player clicked the GitHub button.
                if gitbutton.collidepoint(event.pos):
                    # Open Speed Racer GitHub page.
                    open("https://github.com/OmegaXK/Speed-Racer")

                # Check if the player has clicked the start button.
                if startbutton.collidepoint(event.pos):
                    # Start the game by returning.
                    return

        # Blit the title screen background.
        DISPLAYSURF.blit(title_img, (0, 0))

        # Draw the buttons.
        pygame.draw.rect(DISPLAYSURF, BLACK, gitbutton)
        pygame.draw.rect(DISPLAYSURF, BLACK, startbutton)

        # Draw the text that goes on top of the buttons.
        DISPLAYSURF.blit(gittext, gittextrect)
        DISPLAYSURF.blit(starttext, starttextrect)

        # Draw the other text.
        DISPLAYSURF.blit(titletext, titlerect)
        DISPLAYSURF.blit(bytext, byrect)
        DISPLAYSURF.blit(gitsurf, gitrect)

        # Update.
        pygame.display.update()
        MAINCLOCK.tick(FPS)


def run_game():
    """Run the game, and return when the player hits an obstacle."""
    global car_lane, score, arrows, arrow_frame, obstacles, obstacle_frame
    global game_speed, obstacle_spawn

    # Start the music.
    #pygame.mixer.music.play(-1, 0.0)

    # Reset game variables.
    arrows = []
    score = 0
    car_lane = 2
    arrow_frame = 0
    obstacle_frame = 0
    obstacles = []
    game_speed = 7
    obstacle_spawn = 80
    
    # Start the car on the left side center of the screen.
    car_rect.midleft = (80, CENTERY)

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
        DISPLAYSURF.blit(bg_img, (bg_rect))

        # Update the score.
        score += 1

        # Draw the score.
        draw_score(score)

        # Update the speed.
        update_speed()

        # Update the arrows.
        spawn_arrows()
        update_arrows()

        # Update the obstacles.
        spawn_obstacles()
        quit = update_obstacles()

        # Draw the player.
        DISPLAYSURF.blit(car_img, car_rect)

        # Check if the player has hit an obstacle.
        if quit:
            # Return to the game over screen.
            return

        # Update the game.
        pygame.display.update()
        MAINCLOCK.tick(FPS)


def update_speed():
    """Make the game faster every five seconds."""
    global game_speed, obstacle_spawn

    if score % 500 == 0:
        game_speed += 2


def draw_score(score):
    """Draw the score text on the screen."""

    scorefont = create_font(40)
    scoresurf = scorefont.render(f"Score: {score}", False, BLACK)
    scorerect = scoresurf.get_rect()
    DISPLAYSURF.blit(scoresurf, scorerect)


def update_obstacles():
    """Update the currently active obstacles."""
    global obstacles

    for obstacle in obstacles[:]:
        # Move the obstacle.
        obstacle["rect"].x -= game_speed

        # Check if the obstacle has hit the player.
        if obstacle['rect'].colliderect(car_rect):
            end = True 
            return end

        # Check if the obstacle is off the screen.
        if obstacle["rect"].x < 75:
            # Remove the obstacle.
            obstacles.remove(obstacle)

        # Draw the obstacle.
        DISPLAYSURF.blit(obstacle["img"], obstacle["rect"])
    

def spawn_obstacles():
    """Spawn obstacles at random intervals."""
    global obstacles, obstacle_frame, obstacle_spawn

    if obstacle_frame >= obstacle_spawn:
        # Reset the obstacle frame.
        obstacle_frame = 0
        obstacle_spawn -= 1

        # Choose a random obstacle to spawn.
        obstacle = random.choice(OBSTACLES)

        # Spawn the obstacle.
        if obstacle == ROCK:
            obstacle = {}
            obstacle["img"] = rock_img
            obstacle_rect = rock_img.get_rect()

        elif obstacle == BARREL:
            obstacle = {}
            obstacle["img"] = barrel_img
            obstacle_rect = barrel_img.get_rect()

        elif obstacle == OIL:
            obstacle = {}
            obstacle["img"] = oil_img
            obstacle_rect = oil_img.get_rect()

        # Set the obstacle's lane. 50% Chance it targets the car.
        target = random.randint(1, 2)
        
        # Randomize the lane or set the lane to the car's lane.
        if target == 1:
            lane = random.randint(1, 3)
        else:
            lane = car_lane

        if lane == 3:
            y_pos = CENTERY - 160
        elif lane == 2:
            y_pos = CENTERY
        elif lane == 1:
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
        arrow.x -= game_speed

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
    
    # Set up the game over fonts.
    big_font = create_font(120)
    button_font = create_font(75)

    # Set up the game over text.
    gamesurf = big_font.render('Game Over', False, BLACK, WHITE)
    gamerect = gamesurf.get_rect()
    gamerect.center = (CENTERX, CENTERY - 200)

    # Set up the quit button.
    quit_button = pygame.Rect(0, 0, 300, 100)
    quit_button.center = (CENTERX + 200, CENTERY)

    # Set up the restart button.
    restart_button = pygame.Rect(0, 0, 300, 100)
    restart_button.center = (CENTERX - 200, CENTERY)

    # Set up the quit text.
    quitsurf = button_font.render('Quit', False, RED)
    quitrect = quitsurf.get_rect()
    quitrect.center = quit_button.center

    # Set up the restart text.
    restartsurf = button_font.render('Restart', False, GREEN)
    restartrect = restartsurf.get_rect()
    restartrect.center = restart_button.center

    # Run the game over loop.
    while True:
        # Check for events.
        for event in pygame.event.get():
            # Check for quit.
            if event.type == QUIT:
                terminate()

            # Check if the player is pressing a key.
            if event.type == KEYDOWN:
                # Check for ESCAPE key.
                if event.key == K_ESCAPE:
                    terminate()

            # Check if the player is clicking.
            if event.type == MOUSEBUTTONDOWN:
                # Check if the player clicked the quit button.
                if quit_button.collidepoint(event.pos):
                    # Quit the game.
                    terminate()

                # Check if the player clicked the restart button.
                if restart_button.collidepoint(event.pos):
                    # Restart the game.
                    return
                
        # Blit the game over background.
        DISPLAYSURF.blit(title_img, (0, 0))

        # Draw the buttons.
        pygame.draw.rect(DISPLAYSURF, BLACK, quit_button)
        pygame.draw.rect(DISPLAYSURF, BLACK, restart_button)

        # Draw the text that goes on top of the buttons.
        DISPLAYSURF.blit(quitsurf, quitrect)
        DISPLAYSURF.blit(restartsurf, restartrect)

        # Draw the other text.
        DISPLAYSURF.blit(gamesurf, gamerect)

        # Update.
        pygame.display.update()
        MAINCLOCK.tick(FPS)


def create_font(size):
    """Create a font of the respective size."""
    font = pygame.font.Font('freesansbold.ttf', size)
    return font


def load_assets():
    """Load the game's assets."""
    global car_img, car_rect, bg_img, bg_rect, arrow_img, rock_img
    global barrel_img, oil_img, title_img, title_img_rect

    # Load the music.
    pygame.mixer.music.load("sounds/chaoz_impact.mp3")

    # Load in the background and position it.
    bg_img = pygame.image.load("images/race_track.png")
    bg_img = pygame.transform.scale(bg_img, (900, 500))
    bg_rect = bg_img.get_rect()
    bg_rect.center = (CENTERX, CENTERY)

    # Load in th title image and position it.
    title_img = pygame.image.load("images/title_background.jpeg")
    title_img = pygame.transform.scale(title_img, (WINDOWWIDTH, WINDOWHEIGHT))

    # Load the car sprite.
    car_img = pygame.image.load('images/car.png')
    car_img = pygame.transform.scale(car_img, (300, 100))
    car_rect = car_img.get_rect()

    # Load the arrow image.
    arrow_img = pygame.image.load("images/arrow.png")
    arrow_img = pygame.transform.scale(arrow_img, (90, 90))

    # Load in the obstacles.
    rock_img = pygame.image.load("images/rock.png")
    rock_img = pygame.transform.scale(rock_img, (75, 75))

    barrel_img = pygame.image.load("images/barrel.png")
    barrel_img = pygame.transform.scale(barrel_img, (100, 100))

    oil_img = pygame.image.load("images/oil.png")
    oil_img = pygame.transform.scale(oil_img, (130, 130))

    return


def terminate():
    """Close out of the game."""

    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()