import circleshape
import pygame
class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        from constants import LINE_WIDTH
        self.x = x
        self.y = y
        super().__init__(x, y, radius)
        self.line_width = LINE_WIDTH

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            "white",
            (int(self.position.x), int(self.position.y)),
            self.radius,
            self.line_width,
        )

    def update(self, dt):
        self.position += self.velocity * dt