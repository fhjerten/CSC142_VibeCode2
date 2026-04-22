import pygame
from settings import BLACK, PRICES, WIDTH, HEIGHT

class Store:
    def __init__(self):
        # sections: name, rect, stock
        self.sections = [
            ["Fruits", pygame.Rect(100, 100, 120, 120), 20],
            ["Drinks", pygame.Rect(300, 100, 120, 120), 20],
            ["Checkout", pygame.Rect(520, 400, 150, 120), None],
        ]

        self.font = pygame.font.SysFont(None, 26)
        self.big_font = pygame.font.SysFont(None, 60)

        self.profit = 0
        self.line = []

        # images
        self.fruit_img = pygame.transform.scale(pygame.image.load("images/fruit.png"), (40, 40))
        self.drink_img = pygame.transform.scale(pygame.image.load("images/drink.png"), (40, 40))
        self.money_img = pygame.transform.scale(pygame.image.load("images/money.png"), (30, 30))

    def add_to_line(self, customer):
        if customer not in self.line:
            self.line.append(customer)

    def process_checkout(self):
        if not self.line:
            return False

        customer = self.line[0]
        customer.timer -= 1

        if customer.timer <= 0:
            self.profit += customer.money
            self.line.pop(0)
            return True

        return False

    def all_stock_empty(self):
        return all(s[2] == 0 for s in self.sections[:2])

    def draw(self, screen):
        for name, rect, stock in self.sections:
            pygame.draw.rect(screen, (200, 200, 200), rect)

            # name
            screen.blit(self.font.render(name, True, BLACK), (rect.x, rect.y - 25))

            # stock
            if stock is not None:
                screen.blit(self.font.render(f"Stock: {stock}", True, BLACK), (rect.x + 10, rect.y + 80))

            # price
            if name in PRICES:
                screen.blit(self.font.render(f"${PRICES[name]}", True, BLACK), (rect.x + 40, rect.y + 50))

            # icons
            if name == "Fruits":
                screen.blit(self.fruit_img, (rect.x + 40, rect.y - 65))
            elif name == "Drinks":
                screen.blit(self.drink_img, (rect.x + 40, rect.y - 65))

        # profit
        screen.blit(self.money_img, (10, 10))
        screen.blit(self.font.render(f"Total Profit: ${self.profit}", True, BLACK), (50, 12))

        # simulation over
        if self.all_stock_empty():
            screen.blit(self.big_font.render("Simulation Over", True, (200, 0, 0)),
                        (WIDTH//2 - 180, HEIGHT//2 - 30))