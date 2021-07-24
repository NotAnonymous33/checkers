import pygame
from constants import *
from board import Board

pygame.init()





clock = pygame.time.Clock()
running = True

board = Board()
pygame.display.set_caption("Checkers by Anonymous33")

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    board.draw()
    pygame.display.flip()
    clock.tick(FPS)





