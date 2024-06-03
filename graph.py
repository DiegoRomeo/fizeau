import pygame

class Graph:

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

        self.width = 400
        self.height = 200

        self.data = [[0,0], [10, 0], [20, 0]]

    def adjusted_points(self):
        adjusted = [[a[0] + self.x, self.y + self.height - a[1] - 15] for a in self.data]
        return adjusted

    def render(self, screen: pygame.Surface, dt):

        for d in self.data:
            if d[0] < 20:
                self.data.remove(d)

        pygame.draw.rect(screen, "white", pygame.Rect(self.x, self.y, self.width, self.height))
        pygame.draw.rect(screen, "black", pygame.Rect(self.x + 1, self.y + 1, self.width - 2, self.height - 2))

        for i in range(len(self.data)):
            self.data[i][0] -= dt/10

        data = self.adjusted_points()
        pygame.draw.lines(screen, "white", False, data)
