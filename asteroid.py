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
    def split(self):
        from constants import ASTEROID_MIN_RADIUS
        from logger import log_event
        import random
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        for _ in range(2):
            new_radius = self.radius / 2
            new_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            speed = random.randint(40, 100)
            angle = random.uniform(0, 360)
            new_asteroid.velocity = pygame.Vector2(0, 1).rotate(angle) * speed

    def update(self, dt):
        self.position += self.velocity * dt