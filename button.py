import pygame
from constants import *

pygame.init()

class Button:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = TLENGTH // 2
        self.height = 100
        self.color = BCOLOR

    def draw(self):
        pygame.draw.rect(WIN, self.color, [self.x, self.y, self.width, self.height])

    def check_hover(self, x, y):
        if self.x < x < self.x + self.width and self.y < y < self.y + self.height:
            self.color = BCOLOR2
        else:
            self.color = BCOLOR
