import pygame
from pygame.draw import *
import math

width = 400
height = 400
r = 180
factor = 2
n = 100
i = 0

pygame.init()
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

black = (0, 0, 0)
pink = (255, 0, 208)
white = (255,255,255)
screen.fill(black)
FPS = 15

def draw():
    global i
    prevx, prevy = (width//2 + r,height//2)
    delta = (2*math.pi) / n 

    circle(screen, white, (width//2, height//2), r, 1)

    # for i in range(0, n):
    angle = i*delta
    x = int(r*math.cos(angle)+width//2)
    y = int(r*math.sin(angle)+height//2)
    # circle(screen, white, (x,y), 4)

    # for i in range(0, n):
    a = i*delta 
    b = i*delta*factor
    x1 = int(r*math.cos(a)+width//2)
    y1 = int(r*math.sin(a)+height//2)
    x2 = int(r*math.cos(b)+width//2)
    y2 = int(r*math.sin(b)+height//2)
    line(screen, white, (x1,y1), (x2,y2))

    i += 1


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