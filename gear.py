import pygame
from math import e

class Gear:

    def __init__(self, x, y, n, angular_velocity) -> None:
        self.x = x
        self.y = y
        self.n = n

        self.metal_image = pygame.transform.scale_by(pygame.image.load("./assets/metal.png"), 2)
        self.width = self.metal_image.get_width()
        self.height = self.metal_image.get_height()


        self.angular_velocity = angular_velocity
        self.tiles = self.height // (self.n) 

        self.scroll = 0
        self.outline = 2


    def check_collision(self, particle):
        tooth = []
        for i in range(0, 2*self.tiles, 2):
            h = self.y + i * self.tiles - self.scroll
            if h >= self.y and h <= self.y + self.height:
                tooth.append([self.x, h, self.width, self.tiles])

        for teeth in tooth:
            if particle.x <= teeth[0] + teeth[2] + particle.radius and particle.x + 3*particle.radius >= teeth[0]:
                if particle.y <= teeth[1] + teeth[3] and particle.y >= teeth[1]:
                    return True
        return False

    def draw(self, screen: pygame.Surface):
        if self.scroll >= self.height:
            self.scroll = 0


        for i in range(0, 2*self.tiles, 2):
            pygame.draw.rect(screen, "#7d6e6e", pygame.Rect(self.x, self.y + i * self.tiles - self.scroll, self.width, self.tiles))
            # BORDER
            pygame.draw.rect(screen, "#c2b5a9", pygame.Rect(self.x + self.outline, self.y + i * self.tiles - self.scroll + self.outline, self.width - 2 * self.outline, self.tiles - 2 * self.outline))

        screen.blit(self.metal_image, (self.x, self.y - self.height))
        screen.blit(self.metal_image, (self.x, self.y + self.height))

        # TODO: Change accordingly to theory
        self.scroll += self.angular_velocity / 150
