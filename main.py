import pygame
from settings import WIDTH, HEIGHT, WHITE
from customer import Customer
from store import Store

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT)) # game window
pygame.display.set_caption("Grocery Store Simulation") 

clock = pygame.time.Clock() # controls game speed in fps


#Creating Objects
customer = Customer()
store = Store()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # update
    customer.move() # moving customer

    #drawing it all
    screen.fill(WHITE)
    store.draw(screen)
    customer.draw(screen)

    pygame.display.flip()
    clock.tick(60) # run the simulation at 60 fps

pygame.quit()