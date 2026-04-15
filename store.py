import pygame
from settings import GRAY, BLACK

class Store:
    def __init__(self):
        # Each section of the store has a name + rectangle
        self.sections = [
            ("Fruits", pygame.Rect(100, 100, 100, 100)),
            ("Drinks", pygame.Rect(300, 100, 100, 100)),
            ("Checkout", pygame.Rect(500, 400, 150, 100)),
        ]

        self.font = pygame.font.SysFont(None, 24)  # for text of the sections.

    def draw(self, screen):
        for name, rect in self.sections:
            pygame.draw.rect(screen, GRAY, rect)

            # draw the section name above the box
            text = self.font.render(name, True, BLACK)
            screen.blit(text, (rect.x, rect.y - 20))