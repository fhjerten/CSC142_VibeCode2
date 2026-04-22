import pygame
import random
from settings import CUSTOMER_SPEED, PRICES

class Customer:
    def __init__(self, store):
        self.store = store

        # image
        self.image = pygame.transform.scale(
            pygame.image.load("images/customer.png"), (20, 20))

        self.reset()

    def reset(self):
        # start position
        self.x = random.randint(0, 800)
        self.y = random.randint(0, 600)

        self.money = 0
        self.items = 0

        self.target_name, self.target, self.section = self.pick_target()

        self.state = "moving"
        self.timer = 0

    def pick_target(self):
        section = random.choice(self.store.sections[:2])
        return section[0], section[1], section

    def move(self):
        if self.state == "moving":
            tx, ty = self.target.centerx, self.target.centery

            # smooth move
            self.x += (tx - self.x) * 0.015
            self.y += (ty - self.y) * 0.015

            if abs(self.x - tx) < 5 and abs(self.y - ty) < 5:
                self.state = "shopping"
                self.timer = 60

        elif self.state == "shopping":
            self.timer -= 1

            if self.timer <= 0:
                # take item
                if self.section[2] > 0:
                    self.money += PRICES[self.target_name]
                    self.section[2] -= 1
                    self.items += 1

                # go checkout after 2 items
                if self.items >= 2:
                    self.state = "going_to_line"
                else:
                    self.target_name, self.target, self.section = self.pick_target()
                    self.state = "moving"

        elif self.state == "going_to_line":
            checkout = self.store.sections[2][1]

            tx = checkout.x - 30
            ty = checkout.y

            self.x += (tx - self.x) * 0.03
            self.y += (ty - self.y) * 0.03

            # join line once
            if abs(self.x - tx) < 5 and self not in self.store.line:
                self.store.add_to_line(self)
                self.state = "in_line"
                self.timer = 120

        elif self.state == "in_line":
            if self not in self.store.line:
                return

            index = self.store.line.index(self)
            checkout = self.store.sections[2][1]

            # first goes inside checkout
            if index == 0:
                tx = checkout.centerx
                ty = checkout.centery
            else:
                tx = checkout.x - 30
                ty = checkout.y + index * 25

            # move into position
            self.x += (tx - self.x) * 0.1
            self.y += (ty - self.y) * 0.1

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

        # money above
        font = pygame.font.SysFont(None, 20)
        screen.blit(font.render(f"${self.money}", True, (0, 0, 0)),
                    (self.x - 5, self.y - 15))