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
    def __init__(self, xvel, yvel, x, y, energy, color, ambient):
        super().__init__()
        self.radius = 10
        self.image = pg.Surface((int(self.radius * sqrt(2)), int(self.radius * sqrt(2))))
        self.rect = self.image.get_rect()
        self.xvel = xvel
        self.yvel = yvel
        self.rect.x = x
        self.rect.y = y
        self.energy = energy
        self.color = color
        self.ambient = ambient

    def update(self, screen):
        self.energy -= 1
        pg.draw.circle(screen, self.color, self.rect.center, self.radius)
        pg.draw.circle(screen, preto, self.rect.center, self.radius/2)

        self.rect.x += self.xvel
        self.rect.y += self.yvel

        if self.rect.right >= largura or self.rect.left <= 0:
            self.xvel *= -1
        if self.rect.bottom >= 600 or self.rect.top <= 40:
            self.yvel *= -1

        if self.energy <= 0 or self.ambient.temp >= 400 or self.ambient.acid < 4:
            self.kill()
        if self.ambient.press > 3500 or self.ambient.rad > 40:
            self.kill()

class Ambient:
    def __init__(self, temp, rad, acid):
        self.temp = temp
        self.rad = rad
        self.press = int(self.temp*8.31)
        self.acid = acid

    def draw(self, text, screen, color, xr, xt, yt):
        self.rect = pg.Rect(xr, 0, 250, 40)
        pg.draw.rect(screen, color, self.rect)
        draw_text(text, gameFont, preto, screen, xr+xt, yt)

startamb = Ambient(300, 10, 7)
test_cell = Cell(1, 1, 100, 100, 600, azul, startamb)
        
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

class SlideButton:
    def __init__(self, color, x, y):
        self.color = color
        self.slide = pg.Rect(0, y+10, 200, 5)
        self.rect = pg.Rect(x, y, 30, 30)

    def draw(self, screen):
        pg.draw.rect(screen, preto, self.slide)
        pg.draw.rect(screen, self.color, self.rect)
        


        

        

        






        
