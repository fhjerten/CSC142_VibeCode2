import pygame
from settings import WIDTH, HEIGHT, WHITE, NUM_CUSTOMERS
from customer import Customer
from store import Store

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Grocery Store Simulation")

clock = pygame.time.Clock()

# Create the store
store = Store()

# Create multiple customers
customers = [Customer(store) for i in range(NUM_CUSTOMERS)]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # update customers so they randomly move around the store.
    for customer in customers:
        customer.move()

    # draw everything
    screen.fill(WHITE)
    store.draw(screen)

    for customer in customers:
        customer.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()