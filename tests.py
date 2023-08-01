import pygame as pg
from pygame.locals import *
from math import sqrt
from random import *
from variables import *
from classes import *

class Cell(pg.sprite.Sprite):
    highTempDeaths = 0
    lowTempDeaths = 0
   
    radDeaths = 0
   
    lowAcidDeaths = 0
    highAcidDeaths = 0
   
    totalDeaths = 0
   
    def __init__(self, xvel, yvel, x, y, energy, ambient, radRes=10, tempRes=295, color=azul, acidRes=7, saltRes=10, list=[]):
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
             self.Mutacid = randint(1,  400-((self.ambient.rad)*5))
         
        self.MutRad = randint(1, 400-(self.ambient.rad*10))

        if self.MutTemp == 1:
            self.tempRes = randint(self.tempRes-50, self.tempRes+50)
            self.color = (randint(0, 255), randint(0, 255), randint(0, 255))
            list.append(self.color)

        if self.Mutacid == 1:
            self.acidRes = randint(self.acidRes-3, self.acidRes+3)
            self.color = (randint(0, 255), randint(0, 255), randint(0, 255))
            list.append(self.color)
           
        if self.MutRad == 1:
            self.radRes = randint(self.radRes-5, self.radRes+5)
            self.color = (randint(0, 255), randint(0, 255), randint(0, 255))
            list.append(self.color)
           
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
                 
        if self.ambient.acid <= self.acidRes-3:
            self.energy -= 2
            if self.energy <=0:
                 Cell.lowAcidDeaths += 1

        if self.ambient.acid >= self.acidRes+3:
            self.energy -= 2
            if self.energy <=0:
                 Cell.highAcidDeaths += 1
 
        if self.energy <= 0:
            Cell.totalDeaths += 1
            self.kill()

def level1():
    pg.mixer.music.pause()
    energies = pg.sprite.Group()
    cells = pg.sprite.Group()
    cells.add(test_cell)
   
    c_energy = 150

    stop = False

    ambient = Ambient(100, 10, 7)

    tempoFPS = 0
    tempo = 0

    tempBtn = SlideButton(vermelho, 80, 610)
    acidBtn = SlideButton(amarelo, 7, 660)
    radBtn = SlideButton(verde, 0, 710)

    start_game = False

    timelist = []
    cellslist = []
    templist = []
    radlist = []
    saltlist = []
    energlist = []
    acidlist = []

    for c in range(400):
        energy = Energy(randint(0, largura), randint(40, 600))
        energies.add(energy)

    while True:
       
        if len(energies) <= 300 and start_game:
            energy = Energy(randint(40, largura), randint(40, 600))
            energies.add(energy)
        if start_game:
            tempoFPS += 1
            if tempoFPS == 60:
                tempoFPS = 0
                tempo += 1
                timelist.append(tempo)
                templist.append(ambient.temp)
                cellslist.append(len(cells))
                radlist.append(ambient.rad)
                acidlist.append(ambient.acid)
                energlist.append(len(energies))
                saltlist.append(ambient.salt)

        relogio.tick(fps)
        tela.fill(cinza)

        mx, my = pg.mouse.get_pos()

        energies.draw(tela)
        if start_game:
            cells.draw(tela)
            cells.update(tela)

        ambient.draw(f'temperatura: {ambient.temp} K', tela, vermelho, 0, 5, 10)
        ambient.draw(f'Salinidade {ambient.salt} mg/ml', tela, azul, 250, 5, 10)
        ambient.draw(f'pH: {ambient.acid}', tela, amarelo, 2*250, 5, 10)
        ambient.draw(f'Radioatividade: {ambient.rad}.10¹²Bq', tela, verde, 3*250, 5, 10)

        pg.draw.rect(tela, branco, (0, 40, 130, 50))
        draw_text(f'tempo: {tempo} s', gameFont, preto, tela, 5, 40)
        draw_text(f'Células: {len(cells)}', gameFont, preto, tela, 5, 60)
        if start_game == False:
            draw_text('Pressione barra de espaço para começar', gameFont, vermelho, tela, 290, altura/3)

        pg.draw.rect(tela, azul_claro, painel)

        ambient.rad = radBtn.rect.centerx - 5
        ambient.acid = acidBtn.rect.centerx - 15
        ambient.temp = tempBtn.rect.centerx + 200
        ambient.salt = ambient.acid+23.2

        if tempBtn.rect.collidepoint(mx, my):
            if pg.mouse.get_pressed()[0] and mx <= 185 and mx >= 15:
                tempBtn.rect.centerx = mx

        if acidBtn.rect.collidepoint(mx, my):
            if pg.mouse.get_pressed()[0] and mx <= 29 and mx >=15:
                acidBtn.rect.centerx = mx
       
        if radBtn.rect.collidepoint(mx, my):
            if pg.mouse.get_pressed()[0] and mx <= 185 and mx >=15:
                radBtn.rect.centerx = mx

        tempBtn.draw(tela)
        acidBtn.draw(tela)
        radBtn.draw(tela)

        collisions = pg.sprite.groupcollide(cells, energies, False, True)
        for cell, energy_list in collisions.items():
            for energy in energy_list:
                dx1 = randint(-1, 1)
                dx2 = randint(-1, 1)
                dy1 = randint(-1, 1)
                dy2 = randint(-1, 1)
                if (dx1 == 0 and dy1 == 0) or (dx2 == 0 and dy2 == 0) or (dx1 == dx2 and dy1 == dy2):
                    dx1 = -1
                    dx2 = 1
                    dy1 = -1
                    dy2 = 1

                celltemp = cell.tempRes
                cellRadRes = cell.radRes
                cellcolor = cell.color
               
                new_cell1 = Cell(1*dx1, 1*dy1, cell.rect.x, cell.rect.y, c_energy, ambient, cellRadRes, celltemp, cellcolor, list=colorlist)
                new_cell2 = Cell(1*dx2, 1*dy2, cell.rect.x, cell.rect.y, c_energy, ambient, cellRadRes, celltemp, cellcolor, list=colorlist)
                cells.add(new_cell1, new_cell2)
                cells.remove(cell)

        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    main_menu()
                if event.key == K_SPACE:
                    start_game = True
                if event.key == K_RIGHT:
                    radBtn.rect.centerx += 1
                if event.key == K_LEFT:
                    radBtn.rect.centerx -= 1
                if event.key == K_e:
                    stop = True
        
        if len(cells) == 0 or stop:
            tela.fill(branco)
            dx = 500
            dy = 750/2
            for d in range(0, len(colorlist)):
                pg.draw.circle(tela, colorlist[d], (dx, dy), 10)
                pg.draw.circle(tela, preto, (dx, dy), 5)
                
            #pg.quit()
            #how_graphs(timelist, cellslist, templist, saltlist, acidlist, radlist, energlist, radlist)

        pg.display.flip()

