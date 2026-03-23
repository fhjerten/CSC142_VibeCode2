import pygame
import random

class Customer:
    def __init__(self):
        self.x = random.randint(50,750)  # Random starting x position on screen
        self.y = random.randint(50,550)  # Tandom starting y position on screen
        self.speed = 2

    def move(self):
        # Simple random movement
        self.x += random.choice([-1, 1]) * self.speed  # Move left / right
        self.y += random.choice([-1, 1]) * self.speed  # Move up / down

    def draw(self, screen):
        pygame.draw.circle(screen, (0, 255, 0), (self.x, self.y), 10)