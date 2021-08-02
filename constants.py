
import pygame
pygame.init()

LCOLOR = (240, 230, 220)
RCOLOR = (199, 117, 61)
SCOLOR = (0, 255, 255)
HCOLOR = (0, 181, 98)  # (127, 255, 0)
BCOLOR = (224, 45, 87)
BCOLOR2 = (184, 25, 57)
TLENGTH = 800
NUM_ROWS = 8
DEPTH = 5
CLENGTH = TLENGTH // NUM_ROWS
FPS = 60
WIN = pygame.display.set_mode((TLENGTH, TLENGTH + 100))

IMAGES = [pygame.transform.scale(pygame.image.load("images/0.png"), (CLENGTH, CLENGTH)),
          pygame.transform.scale(pygame.image.load("images/1.png"), (CLENGTH, CLENGTH))]
