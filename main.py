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
        if event.type == pygame.QUIT or board.quit():
            running = False

        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            board.click(pos[0], pos[1])

        pos = pygame.mouse.get_pos()
        for button in board.buttons:
            button.check_hover(pos[0], pos[1])

    board.draw()
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()



