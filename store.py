import pygame

class Store: 
    def __init__(self):

        # Example for the sections
        self.sections = [ 
            pygame.Rect(100, 100, 100, 100), # the fruits
            pygame.Rect(300, 100, 100, 100), # the drinks
            pygame.Rect(500, 400, 150, 100), # checkout register
        ]

    def draw(self, screen):
        for section in self.sections:
            pygame.draw.rect(screen, (200, 200, 200), section)