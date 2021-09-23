import pygame
from pygame.locals import *
import time
import random

# Initialize
pygame.init()

# Colors scheme
white = (255, 255, 255)
black = (0, 0, 0)
Green = (55, 98, 87)
# Define Default Font to Use
font_style = pygame.font.SysFont(None, size=(50))

clock = pygame.time.Clock()

# Create surface
surface_x= 780
surface_y = 400
game_surface = pygame.display.set_mode((surface_x, surface_y))
game_title = pygame.display.set_caption("Snake-Game")

# Create a function to Create message when Game is over
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    game_surface.blit(mesg, [surface_x/2, surface_y/2])

    # Snake Position on Window Screen
snake_x = surface_x/2
snake_y = surface_y/2

# food Random position on Window Screen
food_x = random.randrange(1, (surface_x // 10)) * 10
food_y = random.randrange(1, (surface_y // 10)) * 10

running = True

x1_change = 0
y1_change = 0
while running:

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == K_LEFT:
                x1_change = -10
                y1_change = 0
            elif event.key == K_RIGHT:
                x1_change = 10
                y1_change = 0
            elif event.key == K_UP:
                y1_change = -10
                x1_change = 0
            elif event.key == K_DOWN:
                y1_change = 10
                x1_change = 0
            elif event.key == K_ESCAPE:
                running = False
    snake_x += x1_change
    snake_y += y1_change
    game_surface.fill(Green)
    # Create Snake
    snake = pygame.draw.rect(game_surface, black, [snake_x, snake_y, 10, 10])

    # Create Food
    food = pygame.draw.rect(game_surface,white, [food_x, food_y, 8, 8])
    # Refresh game screen
    pygame.display.update()

    clock.tick(10)

    if snake_x >= surface_x or snake_x < 0 or snake_y >= surface_y or snake_y < 0:
        message("Game Over", black)
        running = False
        time.sleep(0.1)
        pygame.display.update()
pygame.display.update()
# Keep Window open until desired time
time.sleep(3)