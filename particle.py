import pygame
from pygame.locals import BLEND_RGB_ADD

def circle_surface(radius, color):
    surface = pygame.Surface((radius * 2, radius * 2))
    pygame.draw.circle(surface, color, (radius, radius), radius)
    surface.set_colorkey((0, 0, 0))
    
    return surface

class Particle:

    def __init__(self, x, y, vx, vy, radius) -> None:
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

        self.radius = radius
        self.surface_radius = 2 * self.radius

        self.image = circle_surface(self.surface_radius, (20, 20, 40))
        self.mask = pygame.mask.from_surface(self.image)

        self.reflected = False


    def update(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt

    def draw(self, screen: pygame.Surface):
        pygame.draw.circle(screen, (255, 255, 255), [self.x, self.y], self.radius)


        screen.blit(self.image, (self.x - self.surface_radius, self.y - self.surface_radius), special_flags=BLEND_RGB_ADD)
