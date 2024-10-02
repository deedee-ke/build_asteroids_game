import pygame  # Importing the pygame module for game development
from constants import *  # Importing constants such as SHOT_RADIUS
from circleshape import CircleShape  # Importing the CircleShape base class


class Shot(CircleShape):
    def __init__(self, x, y):
        # Initialize the shot at position (x, y) with a specific radius
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        # Draw the shot as a circle on the given screen
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        # Update the position of the shot based on its velocity and the time delta
        self.position += self.velocity * dt  # Move the shot according to its velocity
