import pygame
from board import Board

# Color
white = (255,255,255)

# Const
width = 450
height = 450
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
            
            if board.place(pos):
                board.computer_move()

    board.draw()
    pygame.display.flip()
    screen.fill(white)
    clock.tick(FPS)

pygame.quit()