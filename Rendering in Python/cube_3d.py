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

points = np.array([[-0.5 , -0.5 , -0.5],
		   [ 0.5 , -0.5 , -0.5],
		   [ 0.5 ,  0.5 , -0.5],
		   [-0.5 ,  0.5 , -0.5],
		   [-0.5 , -0.5 ,  0.5],
		   [ 0.5 , -0.5 ,  0.5],
		   [ 0.5 ,  0.5 ,  0.5],
		   [-0.5 ,  0.5 ,  0.5]])

# Functions
def draw():
	global angle

	# rotation = np.array([[math.cos(angle), -math.sin(angle), 0],
	# 				    [math.sin(angle), math.cos(angle), 0]])

	rotationX = np.array([[1, 0, 0],
			[0, math.cos(angle), -math.sin(angle)],
			[0, math.sin(angle), math.cos(angle)]])

	rotationY = np.array([[math.cos(angle), 0, -math.sin(angle)],
			[0, 1, 0],
			[math.sin(angle), 0, math.cos(angle)]])

	rotationZ = np.array([[math.cos(angle), -math.sin(angle), 0],
			[math.sin(angle), math.cos(angle), 0],
			[0, 0, 1]])

	projected = []
	for point in points:
		rotated = rotationX@point
		rotated = rotationY@rotated
		rotated = rotationZ@rotated

		# Perspective Projection
		dist = 2
		z = 1/(dist-rotated[2])

		# Orthogonal Projection
		z = 1

		projection = np.array([[z,0,0],
			[0,z,0],
			[0,0,0]])

		projected2d = projection@rotated

		projected2d *= 100
		projected.append(projected2d)

	# Points
	# for i in projected:
	# 	x = int(i[0]+transX)
	# 	y = int(i[1]+transY)	
	# 	pygame.draw.circle(screen, white, (x,y), 4)

	# Connecting Edges
	for i in range(4):
		connect(i, (i+1)%4, projected)
		connect(i+4, ((i+1)%4)+4, projected)
		connect(i, i+4, projected)

	angle += 0.02

def connect(i,j,points):
	x1,y1 = int(points[i][0])+transX, int(points[i][1])+transY
	x2,y2 = int(points[j][0])+transX, int(points[j][1])+transY

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