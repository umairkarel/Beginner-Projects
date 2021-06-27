import pygame
import math
from random import randint

width = 500
height = 400
FPS = 30

black = (0, 0, 0)
white = (255,255,255)

pygame.init()
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
screen.fill(white)

zoom = 100
n = 7
d = 9
l = 5
theta = 1

def draw():
    global theta
    prevx, prevy = (width//2,height//2)

    if theta == 360:
        theta = 1
    k = theta * d
    r = math.sin(n*k)*zoom
    x = int(r*math.cos(k)+width//2)
    y = int(r*math.sin(k)+height//2)
    # screen.set_at((x,y), black)
    pygame.draw.line(screen, black, (x, y), (prevx, prevy), 1)
    prevx, prevy = (x,y)
    theta += 1



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    draw()
    pygame.display.flip()
    # screen.fill(white)
    clock.tick(FPS)

pygame.quit()

# import math, turtle

# screen = turtle.Screen()
# screen.setup(width=800, height=800, startx=0, starty=0)
# screen.bgcolor('black')
# pen = turtle.Turtle()
# pen.speed(20)
# n = 3
# d = 97

# pen.color('blue')
# pen.pensize(0.5)
# for theta in range(361):
#     k = theta * d * math.pi / 180
#     r = 300 * math.sin(n * k)
#     x = r * math.cos(k)
#     y = r * math.sin(k)
#     pen.goto(x, y)