import pygame
from text import Font

class MessageBox:

    def __init__(self, x, y, text) -> None:
        self.x = x
        self.y = y
        self.text = text

        self.my_font = Font("./assets/large_font.png")
        self.padding_x = 10
        self.padding_y = 10


        self.text_width, self.text_height = self.my_font.get_size(self.text, 1)

    def render(self, screen: pygame.Surface):
        pygame.draw.rect(screen, "white", pygame.Rect(self.x, self.y, self.text_width + 2*self.padding_x, self.text_height + 2*self.padding_y))
        pygame.draw.rect(screen, "black", pygame.Rect(self.x + 1, self.y + 1, self.text_width + 2*self.padding_x - 2, self.text_height + 2*self.padding_y - 2))
 
        self.my_font.render(screen, self.text, self.x + self.padding_x, self.y + self.text_height // 2 + self.padding_y // 2, "white", 1)

