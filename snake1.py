import pygame
import time
import random

pygame.init()


sage = (134, 167, 136)
white = (255, 255, 255)
pink = (255, 207, 207)
pink2 =(232, 37, 97)
peach = (255, 218, 185)


windoWidth = 600
windowHeight = 400


dis = pygame.display.set_mode((windoWidth, windowHeight))
pygame.display.set_caption("Snake game")

clock = pygame.time.Clock()

snakeSize = 10
snakeSpeed = 15


fontStyle = pygame.font.SysFont("calibri", 25)
scoreFont = pygame.font.SysFont("comicsans", 34)

def score(score):
    value = scoreFont.render("Score: " + str(score), True, peach)
    dis.blit(value, [0, 0])

def message(msg, color):
    mssg = fontStyle.render(msg, True, color)
    dis.blit(mssg, [windoWidth / 6, windowHeight / 3])

def my_snake(snakeSize, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, pink, [x[0], x[1], snakeSize, snakeSize])

def reset_game():
    return windoWidth / 2, windowHeight / 2, 0, 0, [], 1, round(random.randrange(0, windoWidth - snakeSize) / 10.0) * 10.0, round(random.randrange(0, windowHeight - snakeSize) / 10.0) * 10.0


def game_loop():
    game_over = False
    game_close = False


    x1, y1, x1_change, y1_change, snake_list, length_snake, foodx, foody = reset_game()

    while not game_over:

        while game_close:
            dis.fill(white)
            message("You lost! Press P to Play Again or Q to Quit", pink2)
            score(length_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_p:
    
                        x1, y1, x1_change, y1_change, snake_list, length_snake, foodx, foody = reset_game()
                        game_close = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snakeSize
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snakeSize
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -snakeSize
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = snakeSize


        if x1 >= windoWidth or x1 < 0 or y1 >= windowHeight or y1 < 0:
            game_close = True


        x1 += x1_change
        y1 += y1_change
        dis.fill(sage)


        pygame.draw.rect(dis, pink2, [foodx, foody, snakeSize, snakeSize])

        snake_head = [x1, y1]
        snake_list.append(snake_head)
        if len(snake_list) > length_snake:
            del snake_list[0]

        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        my_snake(snakeSize, snake_list)
        score(length_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, windoWidth - snakeSize) / 10.0) * 10.0
            foody = round(random.randrange(0, windowHeight - snakeSize) / 10.0) * 10.0
            length_snake += 1

        clock.tick(snakeSpeed)

    pygame.quit()
    quit()

game_loop()
