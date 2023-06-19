import pygame as pg
from pygame.locals import *
from functions import *
from variables import *

pg.init()

class MMButton:
    def __init__(self, xpos, ypos, w, text, font, Color1, Color2):
        self.text = text
        self.font = font
        self.rect = pg.Rect(xpos, ypos, w, 45)
        self.color1 = Color1
        self.color2 = Color2
    
    def update(self, screen):
        mpos = pg.mouse.get_pos()
        GColor = self.color1
        #pg.draw.rect(screen, (255, 0, 0), self.rect)

        if self.rect.collidepoint(mpos):
            GColor = self.color2
        else:
            GColor = self.color1

        draw_text(self.text, self.font, GColor, screen,
                   self.rect.x+5, self.rect.y+5)
        
class Energy(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pg.Surface((5, 5))
        self.image.fill(amarelo)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    #def update(self, cell_group):
        #if pg.sprite.collide_rect(self, cell_group):
            #self.kill()
        