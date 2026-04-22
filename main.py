import pygame
from settings import WIDTH, HEIGHT, WHITE
from customer import Customer
from store import Store

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Grocery Store Simulation")

clock = pygame.time.Clock()

store = Store()

# always 5 customers
customers = [Customer(store) for _ in range(5)]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # stop when simulation over
    if not store.all_stock_empty():
        for c in customers:
            c.move()

        if store.process_checkout():
            customers.append(Customer(store))

    # draw
    screen.fill(WHITE)
    store.draw(screen)

    for c in customers:
        c.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()