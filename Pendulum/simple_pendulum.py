import pygame
import math

SCREEN_WIDTH = 300
SCREEN_HEIGHT = 300
WHITE = (255, 255, 255)
BLACK = (0,0,0)
FPS = 60

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

dragging = False
length = 95
origin = [int(SCREEN_WIDTH/2), 0]
bob = [int(SCREEN_WIDTH/2),length]
angle = math.pi/4
aVel = 0
aAcc = 0
r = 20
gravity = 0.8
damping = 0.995


def update():
    global angle
    global aVel
    global aAcc

    if not dragging:
        aAcc = (-gravity/length)*math.sin(angle)
        aVel += aAcc
        aVel *= damping
        angle += aVel
        bob[0] = math.floor(origin[0] + length * math.sin(angle))
        bob[1] = math.floor(origin[1] + length * math.cos(angle))

def draw():
    global circle

    pygame.draw.line(screen, (0,0,0), (origin), (bob))
    circle = pygame.draw.circle(screen, BLACK, (bob), r, 0)


running = True
while running:
    update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if circle.collidepoint(event.pos):
                    dragging = True
                    mouse_x, mouse_y = event.pos
                    aVel = 0

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:            
                dragging = False

        elif event.type == pygame.MOUSEMOTION:
            if dragging:
                mouse_x, mouse_y = event.pos
                try:
                    angle = (math.atan((mouse_x-origin[0])/mouse_y))
                except:
                    angle = math.pi/2 if mouse_x>200 else -math.pi/2
                bob[0] = math.floor(origin[0] + length * math.sin(angle))
                bob[1] = math.floor(origin[1] + length * math.cos(angle))

    screen.fill(WHITE)
    draw()
    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()