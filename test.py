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
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

clock = pygame.time.Clock()

# Create surface
surface_x= 780
surface_y = 400
game_surface = pygame.display.set_mode((surface_x, surface_y))
game_title = pygame.display.set_caption("Snake-Game")

# Define a function to create a snake
snake_block = 10
def snake(snake_block, snake_body):
    for x in snake_body:
        pygame.draw.rect(game_surface, black, [x[0], x[1], snake_block, snake_block])

# Create a function to Create message when Game is over
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    game_surface.blit(mesg, [surface_x/2, surface_y/2])
def gameloop():
    # Snake Position on Window Screen
    snake_x = surface_x/2
    snake_y = surface_y/2

    # food Random position on Window Screen
    food_x = random.randrange(1, (surface_x // 10)) * 10
    food_y = random.randrange(1, (surface_y // 10)) * 10

    running = True
    game_close = False

    x1_change = 0
    y1_change = 0
    # Create list to define process when snake eat block and it's length increases
    snake_body = []
    length_of_snake = 1
    while running:
        while game_close == True:
            game_surface.fill(Green)
            message("You Lose! Press C-Play Again or Q-QUit", black)
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_q:
                        running = False
                        game_close = False
                    if event.key == K_c:
                        gameloop()
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
        # Create Food
        pygame.draw.rect(game_surface,white, [food_x, food_y, 8, 8])

        snake_head = []
        snake_head.append(snake_x)
        snake_head.append(snake_y)
        snake_body.append(snake_head)
        if len(snake_head) > length_of_snake:
            del snake_body[0]

        for x in snake_body[:-1]:
            if x == snake_head:
                game_close = True

        snake(snake_block, snake_body)

        # Refresh game screen
        pygame.display.update()

        if snake_y == food_x and snake_y == food_y:
            food_x = random.randrange(1, (surface_x // 10)) * 10
            food_y = random.randrange(1, (surface_y // 10)) * 10
            length_of_snake += 1
        clock.tick(10)

        if snake_x >= surface_x or snake_x < 0 or snake_y >= surface_y or snake_y < 0:
            # message("Game Over", black)
            game_close = True
            # time.sleep(0.1)
            pygame.display.update()


# Keep Window open until desired time
    pygame.quit()
    quit()
gameloop()
