import pygame  # Importing the pygame module for game development

# Base class for game objects that are circular in shape
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # Initialize the parent Sprite class, adding this object to its containers if specified
        if hasattr(self, "containers"):
            super().__init__(self.containers)  # Add to specified sprite groups
        else:
            super().__init__()  # Initialize without adding to any groups

        # Set the position of the object using a Vector2 for easy 2D math
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)  # Initialize velocity as zero
        self.radius = radius  # Set the radius of the circular object

    def draw(self, screen):
        # This method must be overridden in subclasses to define how to draw the object
        pass

    def update(self, dt):
        # This method must be overridden in subclasses to define how to update the object
        pass

    def collides_with(self, other):
        # Check for collision with another circular object
        return self.position.distance_to(other.position) <= self.radius + other.radius
