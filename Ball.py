import random
import pygame as pg
from pygame import gfxdraw
from colors import Color

class Ball:
    def __init__(self, pos: tuple):
        self.x = pos[0]
        self.y = pos[1]
        self.size = random.randint(10, 50)
    
    def update(self):
        self.y += self.size * 0.2

    def render(self, screen):
        gfxdraw.aacircle(screen, int(self.x), int(self.y), self.size, Color.WHITE)
        gfxdraw.filled_circle(screen, int(self.x), int(self.y), self.size, Color.WHITE)
