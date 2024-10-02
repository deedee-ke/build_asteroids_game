import sys  # Importing the sys module for system-specific parameters and functions
import pygame  # Importing the pygame module for game development
from constants import *  # Importing constants such as screen dimensions
from player import Player  # Importing the Player class from player.py
from asteroid import Asteroid  # Importing the Asteroid class from asteroid.py
from asteroidfield import AsteroidField  # Importing the AsteroidField class from asteroidfield.py
from shot import Shot  # Importing the Shot class from shot.py


def main():
    # Initialize all imported pygame modules
    pygame.init()
    
    # Set up the game screen with specified width and height
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # Create a clock to manage the game's frame rate
    clock = pygame.time.Clock()

    # Create sprite groups for managing game objects
    updatable = pygame.sprite.Group()  # Group for objects that need updating
    drawable = pygame.sprite.Group()    # Group for objects that need drawing
    asteroids = pygame.sprite.Group()   # Group for asteroids
    shots = pygame.sprite.Group()        # Group for shots fired by the player

    # Set up containers for Asteroid and Shot classes
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable  # AsteroidField updates with updatable objects

    # Create an instance of AsteroidField
    asteroid_field = AsteroidField()

    # Set up container for the Player class
    Player.containers = (updatable, drawable)

    # Create the player character positioned at the center of the screen
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0  # Variable to store delta time for frame updates

    # Main game loop
    while True:
        # Event handling loop to check for events like quitting the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # If the quit event is triggered
                return  # Exit the main loop and end the game

        # Update all objects in the updatable group
        for obj in updatable:
            obj.update(dt)  # Call the update method on each object

        # Check for collisions between asteroids and the player
        for asteroid in asteroids:
            if asteroid.collides_with(player):  # If the player collides with an asteroid
                print("Game over!")  # Print game over message
                sys.exit()  # Exit the game

            # Check for collisions between asteroids and shots
            for shot in shots:
                if asteroid.collides_with(shot):  # If an asteroid collides with a shot
                    shot.kill()  # Remove the shot from the game
                    asteroid.split()  # Split the asteroid into smaller ones

        # Clear the screen by filling it with black color
        screen.fill("black")

        # Draw all objects in the drawable group onto the screen
        for obj in drawable:
            obj.draw(screen)  # Call the draw method on each object

        # Update the display with the newly drawn frame
        pygame.display.flip()

        # Limit the frame rate to 60 frames per second
        dt = clock.tick(60) / 1000  # Calculate delta time for frame updates


# Start the game if this script is executed directly
if __name__ == "__main__":
    main()  # Call the main function to run the game
