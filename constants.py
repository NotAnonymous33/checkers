
import pygame
pygame.init()

LCOLOR = (240, 230, 220)
RCOLOR = (199, 117, 61)
SCOLOR = (0, 255, 255)
HCOLOR = (0, 181, 98)  # (127, 255, 0)
TLENGTH = 600
CLENGTH = TLENGTH // 8
FPS = 60
WIN = pygame.display.set_mode((TLENGTH, TLENGTH + 50))

IMAGES = [pygame.transform.scale(pygame.image.load("images/0.png"), (CLENGTH, CLENGTH)),
          pygame.transform.scale(pygame.image.load("images/1.png"), (CLENGTH, CLENGTH))]
