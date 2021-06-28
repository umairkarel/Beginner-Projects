""" 
    Created on Sat May 6 2021

    @author: umairkarel
"""

import pygame
from board import Board
import time

# Color
white = (255,255,255)

# Const
width = 400
height = 400
screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()
FPS = 60

board = Board(width, height, screen)
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                board.reset()

        if event.type == pygame.MOUSEBUTTONDOWN and not(board.win):
            pos = pygame.mouse.get_pos()
            placed = board.place(pos)
            isWin = board.check_win()

            if placed and not isWin :
                board.computer_move()

    board.draw()
    pygame.display.flip()
    screen.fill(white)
    clock.tick(FPS)

pygame.quit()