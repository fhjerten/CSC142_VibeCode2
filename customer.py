import pygame
import random
from settings import CUSTOMER_SPEED, GREEN

class Customer:
    def __init__(self, store):
        # each customer starts at a random position
        self.x = random.randint(0, 800)
        self.y = random.randint(0, 600)

        self.radius = 8

        self.store = store
        self.target = self.pick_target()  # where customer wants to go 

        self.state = "moving"  # "moving" or "shopping"
        self.timer = 0  # used when shopping

    def pick_target(self):
        # choose a random section rectangle to go to.
        return random.choice(self.store.sections)[1]

    def move(self):
        if self.state == "moving":
            # move toward center of intended rectangle
            target_x = self.target.centerx
            target_y = self.target.centery

            # move left/right
            if self.x < target_x:
                self.x += CUSTOMER_SPEED
            elif self.x > target_x:
                self.x -= CUSTOMER_SPEED

            # move up/down
            if self.y < target_y:
                self.y += CUSTOMER_SPEED
            elif self.y > target_y:
                self.y -= CUSTOMER_SPEED

            # check if close enough to "arrived"
            if abs(self.x - target_x) < 5 and abs(self.y - target_y) < 5:
                self.state = "shopping"
                self.timer = 60  # customer stays at a section for 1 second = 60 frames (60 fps)

        elif self.state == "shopping":
            self.timer -= 1

            # when customer is done at a section, go to new target
            if self.timer <= 0:
                self.target = self.pick_target()
                self.state = "moving"

    def draw(self, screen):
        pygame.draw.circle(screen, GREEN, (self.x, self.y), self.radius)