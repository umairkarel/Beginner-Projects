import pygame
import math

width = 400
height = 400
FPS = 60
i = 0
k = 0

pygame.init()
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
screen.fill((255,255,255))

def draw():
	global i
	global k

	k = 0.4
	zoom = 150
	iters = 50

	# Use while loop for to get complete pattern at once
	# while i < 2*math.pi*iters:
	r = math.cos(k*i)*zoom
	x = int(r*math.cos(i)+width//2)
	y = int(r*math.sin(i)+height//2)
	screen.set_at((x,y),(3, 252, 252))
	i += 0.01

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for _ in range(30):
	    draw()
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()