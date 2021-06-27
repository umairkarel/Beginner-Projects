import pygame
import math

width = 400
height = 400
FPS = 60
i = 0
k = 0
speed = 20
pink = (255, 0, 208)
white = (255,255,255)

pygame.init()
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
screen.fill(white)

def draw():
	global i
	global k

	k = 0.8
	zoom = 150
	# iters = 50
    
    # Using Polar System
	# Use while loop for to get complete pattern at once
	# while i < 2*math.pi*iters:
	r = math.cos(k*i)*zoom
	x = int(r*math.cos(i)+width//2)
	y = int(r*math.sin(i)+height//2)
	screen.set_at((x,y), pink)
	i += 0.07


    # Using Cartesian System
    # i = 0    
    # while i < 360:
    #     r = math.cos(k*i)*zoom
    #     x = int(r*math.cos(i)+width//2)
    #     y = int(r*math.sin(i)+height//2)
    #     screen.set_at((x,y), pink)
    #     i += 0.01


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for _ in range(speed):
        draw()

    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()