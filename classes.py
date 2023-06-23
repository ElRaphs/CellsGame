import pygame as pg
from pygame.locals import *
from functions import *
from variables import *
from math import sqrt
from random import *

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
    def __init__(self, xvel, yvel, x, y, energy):
        super().__init__()
        self.radius = 10
        self.image = pg.Surface((int(self.radius*sqrt(2)), int(self.radius*sqrt(2))))
        self.rect = self.image.get_rect()
        self.xvel = xvel
        self.yvel = yvel
        self.rect.x = x
        self.rect.y = y
        self.energy = energy
        self.color = azul
        self.chance = 2

    def update(self, screen):
        
        if self.chance > 1:
            self.color = azul
            self.chance = randint(1, 100)
            self.energy -= 5
        else:
            self.chance = 0
            self.color = vermelho
            self.energy -= 1
        pg.draw.circle(screen, self.color, self.rect.center, self.radius)
        #pg.draw.rect(screen, vermelho, self.rect)
        pg.draw.circle(screen, preto, self.rect.center, self.radius/2)
        
        self.rect.x += self.xvel
        self.rect.y += self.yvel

        if self.rect.right >= largura or self.rect.left <= 0:
            self.xvel *= -1
        if self.rect.bottom >= altura or self.rect.top <= 0:
            self.yvel *= -1

        if self.energy <= 0:
            self.kill()
        
test_cell = Cell(1, 1, 100, 100, 600)
        
class Energy(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pg.Surface((5, 5))
        self.image.fill(amarelo)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        if pg.sprite.collide_rect(self, test_cell):
            self.kill()





        
