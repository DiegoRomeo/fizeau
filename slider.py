import pygame
from text import Font

class Slider:

    def __init__(self, x, y, width, height, min, max, initial_value, text) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.text = text
        self.my_font = Font("./assets/large_font.png")

        self.slider_left_pos = self.x - self.width // 2
        self.slider_right_pos = self.x + self.width // 2
        self.slider_top_pos = self.y - self.height // 2

        self.min = min
        self.max = max
        self.initial_value = (self.slider_right_pos - self.slider_left_pos) * initial_value
        
        self.container_rect = pygame.Rect(self.slider_left_pos, self.slider_top_pos, self.width, self.height)
        self.button_rect = pygame.Rect(self.slider_left_pos + self.initial_value - 5, self.slider_top_pos, 10, self.height)

    def move_slider(self, mouse_position):
        self.button_rect.centerx = mouse_position[0]

    def get_value(self):
        value_range = self.slider_right_pos - self.slider_left_pos
        button_value = self.button_rect.centerx - self.slider_left_pos

        return (button_value / value_range) * (self.max - self.min) + self.min

    def render(self, screen: pygame.Surface):
        pygame.draw.rect(screen, "white", self.container_rect)
        pygame.draw.rect(screen, "black", pygame.Rect(self.slider_left_pos + 1, self.slider_top_pos + 1, self.width - 2, self.height - 2))
        pygame.draw.rect(screen, "white", self.button_rect)

        self.my_font.render(screen, self.text, self.x - self.width // 2, self.y - 30, (255, 255, 255), 1)

