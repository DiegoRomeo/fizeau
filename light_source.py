import pygame
from random import randint

from particle import Particle

class LightSource:

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.image = pygame.transform.scale_by(pygame.image.load("./assets/torch.png"), 2)

    def generate_particle(self):
        return Particle(self.x + self.image.get_width() // 2, self.y, 0, -900, 3)

    def draw(self, screen: pygame.Surface):
        screen.blit(self.image, (self.x, self.y))
