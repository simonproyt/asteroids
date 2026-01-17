import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS, SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_SHOT_SPEED
class Shot(CircleShape):
    """A shot fired by the player."""

    def __init__(self, x, y, direction):
        super().__init__(x, y, radius=SHOT_RADIUS)
        self.velocity = pygame.Vector2(0, 1).rotate(direction) * PLAYER_SHOT_SPEED

    def update(self, dt):
        self.position += self.velocity * dt
        # Remove the shot if it goes off-screen
        if (self.position.x < 0 or self.position.x > SCREEN_WIDTH or
                self.position.y < 0 or self.position.y > SCREEN_HEIGHT):
            self.kill()
    def draw(self, screen):
        pygame.draw.circle(
            screen,
            "yellow",
            (int(self.position.x), int(self.position.y)),
            self.radius,
        )