import pygame

class LightSensor:

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

        self.image = pygame.transform.scale_by(pygame.image.load("./assets/sensor2.png"), 0.1)
        self.mask = pygame.mask.from_surface(self.image)

    def draw(self, screen: pygame.Surface):
        screen.blit(self.image, (self.x, self.y))
