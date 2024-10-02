import pygame  # Importing the pygame module for game development
from constants import *  # Importing constants such as PLAYER_RADIUS and others
from circleshape import CircleShape  # Importing the CircleShape base class
from shot import Shot  # Importing the Shot class for projectiles fired by the player


class Player(CircleShape):
    def __init__(self, x, y):
        # Initialize the player at position (x, y) with a specific radius
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0  # Set the initial rotation angle of the player
        self.shoot_timer = 0  # Initialize the shoot timer for cooldown management

    def draw(self, screen):
        # Draw the player as a triangle on the given screen
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def triangle(self):
        # Calculate the three points of the triangle representing the player
        forward = pygame.Vector2(0, 1).rotate(self.rotation)  # Direction the player is facing
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5  # Right point of the triangle

        # Calculate the three vertices of the triangle
        a = self.position + forward * self.radius  # Tip of the triangle
        b = self.position - forward * self.radius - right  # Bottom left point
        c = self.position - forward * self.radius + right  # Bottom right point

        return [a, b, c]  # Return the list of triangle vertices

    def update(self, dt):
        # Update the player's state based on user input and time delta
        self.shoot_timer -= dt  # Decrease the shoot timer by the time passed
        keys = pygame.key.get_pressed()  # Get the current state of all keyboard keys

        # Move the player forward or backward based on key presses
        if keys[pygame.K_w]:  # Move forward if 'W' is pressed
            self.move(dt)
        if keys[pygame.K_s]:  # Move backward if 'S' is pressed
            self.move(-dt)
        if keys[pygame.K_a]:  # Rotate left if 'A' is pressed
            self.rotate(-dt)
        if keys[pygame.K_d]:  # Rotate right if 'D' is pressed
            self.rotate(dt)
        if keys[pygame.K_SPACE]:  # Shoot if the space bar is pressed
            self.shoot()

    def shoot(self):
        # Handle shooting logic, including cooldown management
        if self.shoot_timer > 0:  # If the shoot timer is still active, do not shoot
            return
        self.shoot_timer = PLAYER_SHOOT_COOLDOWN  # Reset the shoot timer
        shot = Shot(self.position.x, self.position.y)  # Create a new shot at the player's position
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED  # Set shot velocity

    def rotate(self, dt):
        # Rotate the player based on the time delta and turn speed
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        # Move the player forward based on the current rotation
        forward = pygame.Vector2(0, 1).rotate(self.rotation)  # Calculate the forward direction
        self.position += forward * PLAYER_SPEED * dt  # Update the position based on speed and time
