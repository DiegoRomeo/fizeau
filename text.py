import pygame

def change_color(surface: pygame.Surface, old_color, new_color):
    image_copy = pygame.Surface(surface.get_size())
    image_copy.fill(new_color)
    surface.set_colorkey(old_color)
    image_copy.blit(surface, (0, 0))
    return image_copy

def clip(surface: pygame.Surface, x, y, width, height):
    handle_surface = surface.copy()
    clip_rectangle = pygame.Rect(x, y, width, height)
    handle_surface.set_clip(clip_rectangle)
    image = surface.subsurface(handle_surface.get_clip())
    return image.copy()

class Font:

    def __init__(self, path) -> None:
        self.spacing = 1
        font_image = pygame.image.load(path).convert()
        current_char_width = 0
        character_count = 0
        self.characters = {}
        self.character_order = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','.','-',',',':','+','\'','!','?','0','1','2','3','4','5','6','7','8','9','(',')','/','_','=','\\','[',']','*','"','<','>',';']

        for x in range(font_image.get_width()):
            c = font_image.get_at((x, 0))
            if c[0] == 127:
                char_image = clip(font_image, x - current_char_width, 0, current_char_width, font_image.get_height())
                char_image.set_colorkey((0, 0, 0))
                self.characters[self.character_order[character_count]] = char_image.copy()
                character_count += 1
                current_char_width = 0
            else:
                current_char_width += 1

        self.space_width = self.characters["A"].get_width()

    def render(self, screen: pygame.Surface, text, x, y, color, size):
        x_offset = 0
        for char in text:
            if char != " ":
                screen.blit(pygame.transform.scale_by(change_color(self.characters[char], (255, 0, 0), color), size), (x + x_offset*size, y))
                x_offset += self.characters[char].get_width() + self.spacing
            else:
                x_offset += self.space_width + self.spacing * size

    def get_size(self, text, size):
        x_offset = 0
        for char in text:
            if char != " ":
                x_offset += self.characters[char].get_width() + self.spacing
            else:
                x_offset += self.space_width + self.spacing * size

        return x_offset, self.characters["A"].get_height()
