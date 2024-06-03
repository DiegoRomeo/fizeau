import pygame
from text import Font


class SwitchButton:

    def __init__(self, x, y, text, pressed=False) -> None:
        self.x = x
        self.y = y
        self.text = text

        self.my_font = Font("./assets/large_font.png")

        self.pressed = pressed
        self.rectangle = pygame.Rect(self.x, self.y, 60, 20)


    def draw(self, screen: pygame.Surface):
        if self.pressed:
            color = "green"
        else:
            color = "red"
        self.my_font.render(screen, self.text, self.x, self.y - 20, (255, 255, 255), 1)
        pygame.draw.rect(screen, "white", self.rectangle)
        pygame.draw.rect(screen, color, pygame.Rect(self.x + 1, self.y + 1, 58, 18))
