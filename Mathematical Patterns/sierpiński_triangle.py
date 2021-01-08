import pygame
import random

FPS = 60

width = 400
height = 400

pygame.init()
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
screen.fill((255,255,255))

x = random.randint(0, width)
y = random.randint(0, height)
ax = int(width/2)
ay = 0
bx = 0
by = height
cx = width
cy = height

def lerp(x1,x2,d):
	return d*(x2-x1) + x1

def draw():
	global x
	global y

	r = random.randint(0, 2)

	if r==0:
		x = lerp(x, ax, 0.5)
		y = lerp(y, ay, 0.5)
		screen.set_at((int(x),int(y)), (225,0,225))
	elif r==1:
		x = lerp(x, bx, 0.5)
		y = lerp(y, by, 0.5)
		screen.set_at((int(x),int(y)), (225,225,0))
	elif r==2:
		x = lerp(x, cx, 0.5)
		y = lerp(y, cy, 0.5)
		screen.set_at((int(x),int(y)), (0,225,225))

running = True

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	screen.set_at((ax,ay), (225,225,225))
	screen.set_at((bx,by), (225,225,225))
	screen.set_at((cx,cy), (225,225,225))

	for i in range(40):
		draw()
		
	pygame.display.flip()
	clock.tick(FPS)

pygame.quit()