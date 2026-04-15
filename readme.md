Grocery Store Simulation

# How to run program
By launching it from the file main.py

# Project Idea
This project is a simple grocery store simulation built using Python and Pygame. The goal is to simulate customers moving around a store, visiting different sections, and behaving like shoppers.

# Features
- Store layout with fruits, drinks, and checkout
- multiple customers moving around the store at the same time
- customers move toward different sections, instead of randomly
- it is a continuous simulation loop.

# Current stage
Right now is it a working prototype of the simulation. All customers do now have basic behaviors, they choose a section, move towards it, stops at it for 1 second, and then continues to go to another section. 

# Structure
main.py → runs the simulation loop
customer.py → handles the customer movement and behavior
store.py → store layout and sections
settings.py → constants 

# Tools used
Python, pygame



# for ui (next move)
import pygame

class UI:
def init(self):
self.font = pygame.font.SysFont(None, 30)

def draw(self, screen, store, customers):
    # show profit
    profit_text = self.font.render("Profit: ?", True, (0,0,0))
    screen.blit(profit_text, (10, 10))

    # show number of customers
    customer_text = self.font.render("Customers: ?", True, (0,0,0))
    screen.blit(customer_text, (10, 40))
