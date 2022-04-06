import pygame
import time
import random

# initialize all of the pygame variables and objects
pygame.init()

# colors I want to use as tuples
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
custom = (1, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# the width and height of the display
dis_width = 600
dis_height = 400

# set the pygame display's width and height and title
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption("Mazin's First Python Game")

clock = pygame.time.Clock()

# the size of the n by n snake block, and the framerate
snake_size = 20
snake_speed = 15


# some fonts for the window
font_style = pygame.font.SysFont("Impact", 25)
score_font = pygame.font.SysFont("Comic Sans", 35)

# displays the score
def display_score(score):
    mesg = score_font.render("Score: " + str(score), True, custom)
    dis.blit(mesg, [0, 0])

# function to draw every snake block that is a part of the snake
def draw_snake(snake_list):
    for x in snake_list: 
        pygame.draw.rect(dis, black, [x[0], x[1], snake_size, snake_size])

# creating a method for blit-ing a message on the screen, less duplicative code
def message(msg, color): 
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

#defining the game, which is a loop until you completely quit the game
def gameLoop(): 
    game_over = False
    game_close = False
    ate_food = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    # initialized the snake list with the first position
    snake_list = [[x1, y1]]
    length_of_snake = 1

    # remembers the last key pressed so that you can't go in the direct opposite direction
    last_key = None

    #random position of the food that will always be in the grid of the game
    foodx = random.randint(0, (dis_width - snake_size) / snake_size) * snake_size
    foody = random.randint(0, (dis_height - snake_size) / snake_size) * snake_size

    # making pressing Q or C do their repective things - quit or reloop the game
    while not game_over:
        while game_close == True:
            dis.fill(white)
            message("You Lost! Press C - Play Again or Q - Quit!", red)
            display_score(length_of_snake - 1)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        # defining how to move the snake in 4 directions
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and last_key != pygame.K_RIGHT:
                    x1_change = -snake_size
                    y1_change = 0
                    last_key = event.key
                elif event.key == pygame.K_UP and last_key != pygame.K_DOWN:
                    x1_change = 0
                    y1_change = -snake_size
                    last_key = event.key
                elif event.key == pygame.K_RIGHT and last_key != pygame.K_LEFT:
                    x1_change = snake_size
                    y1_change = 0
                    last_key = event.key
                elif event.key == pygame.K_DOWN and last_key != pygame.K_UP:
                    x1_change = 0
                    y1_change = snake_size
                    last_key = event.key
                

        # if the snake hits the boundaries, you lose
        if x1 < 0 or x1 >= dis_width or y1 < 0 or y1 >= dis_height:
            game_close = True

        # changing the snakes position
        x1 += x1_change
        y1 += y1_change
        dis.fill(white)

        # if the snake hits itself, you lose
        if last_key != None:
            for x in snake_list:
                if x1 == x[0] and y1 == x[1]:
                    game_close = True

        # food block
        pygame.draw.rect(dis, blue, [foodx, foody, snake_size, snake_size])
        
        # delete the last block of the snake simulating it moving away, unless it ate food
        snake_list.insert(0, [x1, y1])
        if not ate_food:
            del snake_list[length_of_snake]

        # draws the snake using the list of snake blocks
        draw_snake(snake_list)
        display_score(length_of_snake - 1)
        
        pygame.display.update()

        # if the snake eats the food, then increment the snake length, and record ate_food as true
        if x1 == foodx and y1 == foody:
            print("Yummy!!")
            foodx = random.randint(0, (dis_width - snake_size) / snake_size) * snake_size
            foody = random.randint(0, (dis_height - snake_size) / snake_size) * snake_size
            ate_food = True
            length_of_snake += 1
        # if it didn't eat the food, change ate_food back to False
        else:
            ate_food = False

        # update the snake snake_speed times per second
        clock.tick(snake_speed)

    pygame.quit()
    quit()


gameLoop()