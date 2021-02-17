import pygame
from consts import *
from snake import Snake, Food

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

snake = Snake()
food = Food()
myfont = pygame.font.SysFont("monospace",16)

def drawGrid():
    for y in range(0, int(grid_height)):
        for x in range(0, int(grid_width)):
            if (x+y)%2 == 0:
                box = pygame.Rect(x*gridsize, y*gridsize, gridsize, gridsize)
                pygame.draw.rect(screen, blue, box)

def drawSnake():
    for pos in snake.positions:
        box = pygame.Rect((pos[0], pos[1]), (gridsize,gridsize))
        pygame.draw.rect(screen, snake.color, box)
        pygame.draw.rect(screen, (93,216, 228), box, 1)

def drawFood():
    box = pygame.Rect((food.position[0], food.position[1]), (gridsize, gridsize))
    pygame.draw.rect(screen, food.color, box)
    pygame.draw.rect(screen, (93, 216, 228), box, 1)

def draw():
    drawSnake()
    drawFood()
    text = myfont.render("Score {0}".format(snake.score), 1, (0,0,0))
    screen.blit(text, (5,10))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.turn(up)
            elif event.key == pygame.K_DOWN:
                snake.turn(down)
            elif event.key == pygame.K_LEFT:
                snake.turn(left)
            elif event.key == pygame.K_RIGHT:
                snake.turn(right)

    screen.fill(white)
    drawGrid()
    snake.move()

    if snake.get_head_position() == food.position:
        snake.length += 1
        snake.score += 1
        food.randomize_position()
        while food.position in snake.positions:
            food.randomize_position()

    draw()

    pygame.display.update()
    clock.tick(FPS)