import pygame as pg
from pygame.locals import *
from functions import *
from variables import *
from math import sqrt

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
        
class Cell(pg.sprite.Sprite):
    def __init__(self, xvel, yvel, x, y):
        super().__init__()
        self.image = pg.Surface((int(10*sqrt(2)), int(10*sqrt(2))))
        self.rect = self.image.get_rect()
        self.energy = 0
        self.xvel = xvel
        self.yvel = yvel
        self.rect.x = x
        self.rect.y = y

    def update(self, screen, color):
        pg.draw.circle(screen, color, self.rect.center, 10)
        #pg.draw.rect(screen, vermelho, self.rect)
        
        self.rect.x += self.xvel
        self.rect.y += self.yvel

        if self.rect.right >= largura or self.rect.left <= 0:
            self.xvel *= -1
        if self.rect.bottom >= altura or self.rect.top <= 0:
            self.yvel *= -1

        if self.energy == 1:
            self.energy = 0
        
test_cell = Cell(1, 1, 100, 100)
        
class Energy(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pg.Surface((5, 5))
        self.image.fill(amarelo)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        if pg.sprite.collide_rect(self, test_cell):
            test_cell.energy += 1
            self.kill()

cells = pg.sprite.Group()
cells.add(test_cell)



        
