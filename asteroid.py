import pygame  # Importing the pygame module for game development
import random  # Importing the random module for generating random values
from constants import *  # Importing constants such as asteroid minimum radius
from circleshape import CircleShape  # Importing CircleShape class for circular objects


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        # Initialize the parent CircleShape class with the asteroid's position and radius
        super().__init__(x, y, radius)

    def draw(self, screen):
        # Draw the asteroid as a circle on the given screen
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        # Update the position of the asteroid based on its velocity and the time delta
        self.position += self.velocity * dt

    def split(self):
        # Remove the current asteroid from the game
        self.kill()

        # If the asteroid's radius is less than or equal to the minimum radius, do not split
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        # Randomize the angle for the asteroid to split
        random_angle = random.uniform(20, 50)

        # Calculate new velocities for the two new asteroids created from the split
        a = self.velocity.rotate(random_angle)  # Rotate velocity by a positive angle
        b = self.velocity.rotate(-random_angle)  # Rotate velocity by a negative angle

        # Calculate the radius for the new smaller asteroids
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        
        # Create the first new asteroid
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = a * 1.2  # Set the velocity for the first new asteroid

        # Create the second new asteroid
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = b * 1.2  # Set the velocity for the second new asteroid
