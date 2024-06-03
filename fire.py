import pygame
from random import randint

class FlameParticle:

    def __init__(self, x, y, r) -> None:
        self.x = x
        self.y = y
        self.r = r
        self.original_r = r

        self.alpha_layers = 2
        self.alpha_glow = 2

        self.burn_rate = 0.1 * randint(1, 4)

    def update(self):
        self.y -= 7- self.r
        self.x += randint(-self.r, self.r)
        self.original_r -= self.burn_rate
        self.r = int(self.original_r)
        
        if self.r <= 0:
            self.r = 1

    def draw(self, screen: pygame.Surface):
        max_surface_size = 2 * self.r * self.alpha_glow * self.alpha_layers ** 2
        self.surface = pygame.Surface((max_surface_size, max_surface_size), pygame.SRCALPHA)

        for i in range(self.alpha_layers, -1, -1):
            alpha = 255 - i * (255 // self.alpha_layers - 5)
            if alpha <= 0:
                alpha = 0

            radius = self.r * self.alpha_glow * i ** 2
            if self.r == 4 or self.r == 3:
                r, g, b = (255, 0, 0)
            elif self.r == 2:
                r, g, b = (255, 150, 0)
            else:
                r, g, b = (50, 50, 50)
            color = (r, g, b, alpha)
            pygame.draw.circle(self.surface, color, (self.surface.get_width() // 2, self.surface.get_height() // 2), radius)

        screen.blit(self.surface, self.surface.get_rect(center=(self.x, self.y)))


class Flame:

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

        self.flame_intensity = 2
        self.flame_particles = []

        for i in range(self.flame_intensity * 25):
            self.flame_particles.append(FlameParticle(self.x + randint(-5, 5), self.y, randint(1, 5)))

    def draw(self, screen: pygame.Surface):
        for particle in self.flame_particles:
            if particle.original_r <= 0:
                self.flame_particles.remove(particle)
                del particle
                self.flame_particles.append(FlameParticle(self.x + randint(-5, 5), self.y, randint(1, 5)))
                continue
            particle.update()
            particle.draw(screen)

