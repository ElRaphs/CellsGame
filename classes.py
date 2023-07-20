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

        draw_text(self.text, self.font, GColor, screen, self.rect.x+5, self.rect.y+5)
       
class Cell(pg.sprite.Sprite):

    highTempDeaths = 0
    lowTempDeaths = 0
   
    radDeaths = 0
   
    lowAcidDeaths = 0
    highAcidDeaths = 0
   
    totalDeaths = 0
   
    def __init__(self, xvel, yvel, x, y, energy, ambient, radRes=10, tempRes=295, color=azul, acidRes=7, saltRes=10):
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
        self.tempRes = tempRes
        self.acidRes = acidRes
        self.radRes = radRes
        self.saltRes = saltRes

        if (self.ambient.rad)*5 <= 399:
             self.MutTemp = randint(1, 400-((self.ambient.rad)*5))
       
             
        self.MutRad = randint(1, 400-(self.ambient.rad*10))

        if self.MutTemp == 1:
            self.tempRes = randint(self.tempRes-50, self.tempRes+50)
            self.color = (randint(0, 255), randint(0, 255), randint(0, 255))
           
        if self.MutRad == 1:
            self.radRes = randint(self.radRes-5, self.radRes+5)
            self.color = (randint(0, 255), randint(0, 255), randint(0, 255))
           


    def update(self, screen):
        self.energy -= 1

        self.rect.x += self.xvel
        self.rect.y += self.yvel    

        if self.rect.right >= largura or self.rect.left <= 0:
            self.xvel *= -1
        if self.rect.bottom >= 600 or self.rect.top <= 40:
            self.yvel *= -1

        pg.draw.circle(screen, self.color, self.rect.center, self.radius)
        pg.draw.circle(screen, preto, self.rect.center, self.radius/2)


        if self.ambient.temp >= self.tempRes+30:
            self.energy -= 2
            if self.energy <= 0:
                 Cell.highTempDeaths += 1
       

        if self.ambient.temp <= self.tempRes-30:
            self.energy -= 2
            if self.energy <= 0:
                 Cell.lowTempDeaths += 1

                 
        if self.ambient.rad >= self.radRes+10:
            self.energy -= 2
            if self.energy <= 0:
                 Cell.radDeaths += 1
                 
        if self.ambient.acid <= 4:
            self.energy -= 2
            if self.energy <=0:
                 Cell.lowAcidDeaths += 1

        if self.ambient.acid >= 10:
            self.energy -= 2
            if self.energy <=0:
                 Cell.highAcidDeaths += 1
                 
        if self.energy <= 0:
            Cell.totalDeaths += 1
            self.kill()
         

class Ambient:
    def __init__(self, temp, rad, acid):
        self.temp = temp
        self.rad = rad
        self.salt = 10
        self.acid = acid

    def draw(self, text, screen, color, xr, xt, yt):
        self.rect = pg.Rect(xr, 0, 250, 40)
        pg.draw.rect(screen, color, self.rect)
        draw_text(text, gameFont, preto, screen, xr+xt, yt)

startamb = Ambient(350, 10, 7)
test_cell = Cell(1, 1, 100, 100, 600, startamb)
       

class Energy(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pg.Surface((5, 5))
        self.image.fill(amarelo)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)


class SlideButton:
    def __init__(self, color, x, y):
        self.color = color
        self.slide = pg.Rect(0, y+10, 200, 5)
        self.rect = pg.Rect(x, y, 30, 30)

    def draw(self, screen):
        pg.draw.rect(screen, preto, self.slide)
        pg.draw.rect(screen, self.color, self.rect)