# Steps that involve in it are:
# 1. Installing Pygame
# 2. Create the Screen
# 3. Create the Snake
# 4. Displaying the Score
# 5. Moving the Snake
# 6. Adding the Food
# 7. Increasing the Length of the Snake
# 8. Game Over when Snake hits the boundaries

import pygame
from pygame.locals import *
import random

# Initialize pygame
pygame.init()

# Window axis
window_x = 800
window_y = 560

# Set size of block (default size of food and snake rectangle) and snake speed
block = 10
snake_speed = 15

# Colors Scheme
white = (255, 255, 255)
black = (0, 0, 0)
orange = (245, 146, 66)
yellow = (255, 255, 102)
red = (245, 66, 66)
blue = (66, 90, 245)

# Initialize Window display mode and title
game_window = pygame.display.set_mode(size=(window_x, window_y))
game_window.fill(orange)
game_title = pygame.display.set_caption("Snake Game")

# Fps Controller
fps = pygame.time.Clock()


# Create a function to print message .
def message(msg, color, window_pos=[window_x / 4, window_y / 2]):
    my_font = pygame.font.SysFont("high tower", 30)
    mesg = my_font.render(msg, True, color)
    game_window.blit(mesg, window_pos)


# Function to display score
def Score(score, position=(0, 0)):
    score_font = pygame.font.SysFont("times new roman", 20)
    value = score_font.render("Score: " + str(score), True, blue)
    game_window.blit(value, position)  # Draw score surface on Window Surface


# Define a function to create a snake
def snake(block, snake_body):
    for x in snake_body:
        pygame.draw.rect(game_window, black, [x[0], x[1], block, block])

# Define a loop (Running of game till end of it, with controllers to move snake and boundary conditions)
def gameloop():
    # Snake Position on Window Screen
    snake_pos = [window_x / 2, window_y / 2]

    # food position on Window Screen
    food = [random.randrange(0, (window_x // 10)) * 10,
            random.randrange(0, (window_y // 10)) * 10]
    # Set initial direction (when game start snake move towards Left) and conditions
    direction = 'LEFT'
    change_to = direction
    # Create list to define process when snake eat food and it's length increases
    snake_body = []
    # Initial length of snake
    length_of_snake = 1
    # Main Logic
    game_close = False
    game_over = False
    # Set controllers to move snake
    while not game_close:
        for event in pygame.event.get():
            # Whenever a key is pressed down
            if event.type == pygame.KEYDOWN:
                if event.key == K_UP:
                    change_to = 'UP'
                if event.key == K_DOWN:
                    change_to = 'DOWN'
                if event.key == K_LEFT:
                    change_to = 'LEFT'
                if event.key == K_RIGHT:
                    change_to = 'RIGHT'
                # Esc -> Create event to quit the game
                if event.key == K_ESCAPE:
                    game_close = True
            # Can close game whenever we want using Quit (X)
            if event.type == QUIT:
                game_close = True
        # Making sure the snake cannot move in the opposite direction instantaneously
        if change_to == 'UP' and direction != 'DOWN':
            direction = 'UP'
        if change_to == 'DOWN' and direction != 'UP':
            direction = 'DOWN'
        if change_to == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        if change_to == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'

        # Moving the snake
        if direction == 'UP':
            snake_pos[1] -= 10
        if direction == 'DOWN':
            snake_pos[1] += 10
        if direction == 'LEFT':
            snake_pos[0] -= 10
        if direction == 'RIGHT':
            snake_pos[0] += 10
        # Whenever snake moves the most recent position of it on window will filled
        game_window.fill(orange)
        # Create Food
        pygame.draw.rect(game_window, white, [food[0], food[1], block, block])

        snake_head = []
        snake_head.append(snake_pos[0])
        snake_head.append(snake_pos[1])
        snake_body.append(snake_head)
        if len(snake_body) > length_of_snake:
            del snake_body[0]

        for x in snake_body[:-1]:
            if x == snake_head:
                game_close = True

        # Create Snake
        snake(block, snake_body)
        Score(length_of_snake - 1)  # Count Scores

        if snake_pos[0] == food[0] and snake_pos[1] == food[1]:
            food = [random.randrange(0, (window_x // 10)) * 10, random.randrange(0, (window_y // 10)) * 10]
            length_of_snake += 1

        # Boundary Condition (if snake touch any of boundary, game over)
        if snake_pos[0] >= window_x or snake_pos[0] < 0 or snake_pos[1] >= window_y or snake_pos[1] < 0:
            game_over = True
        # Define message (when game will over and set condition to either play again or Quit)
        while game_over == True:
            game_window.fill(orange)
            message("Game Over Press P-Play Again or Q-Quit", black)
            message(f"Total Score: {length_of_snake-1}", red, window_pos=[window_x/2.5, window_y-50])
            Score(length_of_snake - 1)
            pygame.display.update()

            # Set keys to Play Again or QUit when game over
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_q:
                        game_close = True
                        game_over = False
                    if event.key == K_p:
                        gameloop()
        # Refresh game screen
        pygame.display.update()
        # Cam use to define fps as or can say speed of snake
        fps.tick(snake_speed)
    # Keep Window open until desired time
    pygame.quit()
    quit()


Game = gameloop()