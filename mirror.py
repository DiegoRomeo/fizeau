import pygame

class Mirror:

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

        self.image = pygame.transform.scale_by(pygame.image.load("./assets/glass.png").convert_alpha(), 2)
        self.mask = pygame.mask.from_surface(self.image)


    def reflect(self, particle):
        particle.vx, particle.vy = -particle.vy, particle.vx

    def draw(self, screen: pygame.Surface):
        screen.blit(self.image, (self.x, self.y))


class RotatedMirror:

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

        self.image = pygame.transform.scale_by(pygame.image.load("./assets/glass_corner.png").convert_alpha(), 2)
        self.mask = pygame.mask.from_surface(self.image)


    def reflect(self, particle):
        particle.vx, particle.vy = -particle.vy, particle.vx

    def draw(self, screen: pygame.Surface):
        screen.blit(self.image, (self.x, self.y))

