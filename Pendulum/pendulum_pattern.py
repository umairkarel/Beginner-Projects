import pygame
import math

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 400
FPS = 60

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
length = 190
origin = [int(SCREEN_WIDTH/2), 0]
bob = [int(SCREEN_WIDTH/2),length]
gravity = 0.7
damping = 0.999

class Pendulum:
    def __init__(self, origin, bob, length, angle, color):
        self.origin = origin
        self.bob = bob
        self.length = length
        self.radius = 30
        self.angle = angle
        self.aVel = 0
        self.aAcc = 0
        self.color = color
    def display(self):
        pygame.draw.line(screen, (0,0,20), (self.origin), (self.bob))
        self.circle = pygame.draw.circle(screen, self.color, (self.bob), self.radius, 0)

    def go(self):
        self.update()
        self.display()

    def update(self):
        self.aAcc = (-gravity/self.length)*math.sin(self.angle)
        self.aVel += self.aAcc
        self.aVel *= damping
        self.angle += self.aVel
        self.bob[0] = math.floor(self.origin[0] + self.length * math.sin(self.angle))
        self.bob[1] = math.floor(self.origin[1] + self.length * math.cos(self.angle))

p1 = Pendulum(origin, bob, length, math.pi/2, (247,130,19))
p2 = Pendulum(origin, bob, length, (math.pi/2.1), (0,225,0))
p3 = Pendulum(origin, bob, length, (math.pi/2.2), (225,0,0))
p4 = Pendulum(origin, bob, length, (math.pi/2.3), (0,0,225))
p5 = Pendulum(origin, bob, length, (math.pi/2.4), (225,225,20))
p6 = Pendulum(origin, bob, length, (math.pi/2.5), (0,0,0))

def play():
    p1.go()
    p2.go()
    p3.go()
    p4.go()
    p5.go()
    p6.go()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((225,225,225))
    play()
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()