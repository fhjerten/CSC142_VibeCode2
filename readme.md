# Grocery Store Simulation

## How to Run
Run the program by running:
main.py


## Project Idea
This project simulates a simple grocery store using Python and Pygame.

Customers move around the store, collect items from different sections, and then go to checkout. Each item has a price, and the store earns profit when customers pay.


## What the Program Does
- Customers move randomly between sections (Fruits and Drinks)
- Each section has:
  - A price per item
  - A limited stock
- Customers collect items and build up money
- After collecting enough items, they go to checkout
- Customers form a line on the left side of the checkout
- Only one customer at a time moves into the checkout to pay
- The store tracks total profit at the top of the screen
- When all items are sold out, the simulation ends.


## Features
- Real-time movement using Pygame
- Queue system (customers wait in line properly)
- Resource system (limited stock in sections)
- Profit system for store
- Display with images (customers and products)


## Structure
- main.py: runs the simulation loop
- customer.py: handles customer behavior and movement
- store.py: handles store logic, sections, and profit
- settings.py: stores constants (screen size, prices)
- images: contains all images used in the simulation