import pygame
import math
import random
import numpy as np

# Constants
white = (225,225,225)
black = (0,0,0)
FPS = 60

# Initializing
pygame.init()
width,height = 400,400
screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()

# Variable
angle = 0
transX = int(width/2)
transY = int(height/2)

points = np.array([[-1, -1,  1,  1],
			[1 , -1,  1,  1],
			[1 ,  1,  1,  1],
			[-1,  1,  1,  1],
			[-1, -1, -1,  1],
			[1 , -1, -1,  1],
			[1 ,  1, -1,  1],
			[-1,  1, -1,  1],
			[-1, -1,  1, -1],
			[1 , -1,  1, -1],
			[1 ,  1,  1, -1],
			[-1,  1,  1, -1],
			[-1, -1, -1, -1],
			[1 , -1, -1, -1],
			[1 ,  1, -1, -1],
			[-1,  1, -1, -1]])

# Functions
def draw():
	global angle

	tesseract_rotation = [[1, 0, 0],
            [0, math.cos(-math.pi/2), -math.sin(-math.pi/2)],
            [0, math.sin(-math.pi/2), math.cos(-math.pi/2)]]

	rotationXY = np.array([[math.cos(angle), -math.sin(angle), 0, 0],
			[ math.sin(angle),  math.cos(angle), 0, 0],
			[0, 0, 1, 0],
			[0, 0, 0, 1]])

	rotationXZ = np.array([[math.cos(angle), 0, -math.sin(angle),0],
			[0,1,0,0],
			[math.sin(angle), 0, math.cos(angle),0],
			[0,0, 0,1]])

	rotationXW = np.array([[math.cos(angle), 0, 0, -math.sin(angle)],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [math.sin(angle), 0, 0, math.cos(angle)]])

	rotationYZ = np.array([[1, 0, 0, 0],
            [0, math.cos(angle), -math.sin(angle), 0],
            [0, math.sin(angle), math.cos(angle), 0],
            [0, 0, 0, 1]])

	rotationYW = np.array([[1, 0, 0, 0],
            [0, math.cos(angle), 0, -math.sin(angle)],
            [0, 0, 1, 0],
            [0, math.sin(angle), 0, math.cos(angle)]])

	rotationZW = np.array([[1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, math.cos(angle), -math.sin(angle)],
            [0, 0, math.sin(angle), math.cos(angle)]])

	projected = []
	for point in points:
		rotated3d = rotationXY@point
		rotated3d = rotationZW@rotated3d

		dist = 4
		w = 1/(dist-rotated3d[3])
		projection4d = np.array([[w,0,0,0],
			[0,w,0,0],
			[0,0,w,0]])

		projected3d = projection4d@rotated3d
		rotated2d = tesseract_rotation@projected3d
		z = 1/(dist - (rotated2d[2]+rotated3d[3]))

		projection2d = np.array([[z,0,0],
			[0,z,0]])

		projected2d = projection2d@rotated2d

		projected2d *= 800

		x = int(projected2d[0]+transX)
		y = int(projected2d[1]+transY)

		pygame.draw.circle(screen, (225,225,0), (x,y), 4)
		projected.append([x,y])

	drawEdges(projected)

	angle += 0.03

def drawEdges(projected):
	for i in range(4):
		connect(i, (i+1)%4, 0, projected)
		connect(i+4, ((i+1)%4)+4, 0, projected)
		connect(i, i+4, 0, projected)

	for i in range(0,4):
		connect(i, (i+1)%4, 8, projected)
		connect(i+4, ((i+1)%4)+4, 8, projected)
		connect(i, i+4, 8, projected)

	for i in range(8):
		connect(i, i+8, 0, projected)

def connect(i,j,offset,points):
	x1,y1 = int(points[i+offset][0]), int(points[i+offset][1])
	x2,y2 = int(points[j+offset][0]), int(points[j+offset][1])

	pygame.draw.line(screen, (225,225,225), (x1,y1), (x2,y2), 2)

running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	draw()

	pygame.display.flip()
	screen.fill((0,0,0))
	clock.tick(FPS)

pygame.quit()

