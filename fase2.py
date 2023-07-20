import pygame as pg
from sys import exit
from pygame.locals import *
from variables import *
from functions import *
from classes import *
from random import *

pg.init()

def level2(warning=None):
    pg.mixer.music.pause()
    energies = pg.sprite.Group()
    cells = pg.sprite.Group()
    cells.add(test_cell)
   
    c_energy = 150

    ambient = Ambient(100, 10, 7)

    tempoFPS = 0
    tempo = 0

    tempBtn = SlideButton(vermelho, 80, 610)
    acidBtn = SlideButton(amarelo, 7, 660)
    radBtn = SlideButton(verde, 0, 710)

    start_game = False

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
        relogio.tick(fps)
        tela.fill(cinza)

        mx, my = pg.mouse.get_pos()

        energies.draw(tela)
        if start_game:
            cells.draw(tela)
            cells.update(tela)

        ambient.draw(f'temperatura: {ambient.temp} K', tela, vermelho, 0, 5, 10)
        ambient.draw(f'Salinidade {ambient.salt} mg/g', tela, azul, 250, 5, 10)
        ambient.draw(f'pH: {ambient.acid}', tela, amarelo, 2*250, 5, 10)
        ambient.draw(f'Radioatividade: {ambient.rad} Bq', tela, verde, 3*250, 5, 10)

        pg.draw.rect(tela, branco, (0, 40, 130, 50))
        draw_text(f'tempo: {tempo} s', gameFont, preto, tela, 5, 40)
        draw_text(f'Células: {len(cells)}', gameFont, preto, tela, 5, 60)
        if start_game == False:
            draw_text('Pressione barra de espaço para começar', gameFont, vermelho, tela, 290, altura/3)

        pg.draw.rect(tela, azul_claro, painel)

        ambient.rad = radBtn.rect.centerx - 5
        ambient.acid = acidBtn.rect.centerx - 15
        ambient.acid = 7
        ambient.temp = tempBtn.rect.centerx + 200

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
        #acidBtn.draw(tela)
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
               
                new_cell1 = Cell(1*dx1, 1*dy1, cell.rect.x, cell.rect.y, c_energy, ambient, cellRadRes, celltemp, cellcolor)
                new_cell2 = Cell(1*dx2, 1*dy2, cell.rect.x, cell.rect.y, c_energy, ambient, cellRadRes, celltemp, cellcolor)
                cells.add(new_cell1, new_cell2)
                cells.remove(cell)

        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    start_game = True
                if event.key == K_RIGHT:
                    radBtn.rect.centerx += 1

        if len(cells) == 0:
            highTempDeaths = (Cell.highTempDeaths / Cell.totalDeaths) * 100
            highTempDeathsText = f'Mortes por Alta Temperatura: {highTempDeaths:.2f}%'
            lowTempDeaths = (Cell.lowTempDeaths / Cell.totalDeaths) * 100
            lowTempDeathsText = f'Mortes por Baixa Temperatura: {lowTempDeaths:.2f}%'
            totalTempDeaths = Cell.highTempDeaths + Cell.lowTempDeaths

            radDeaths = (Cell.radDeaths / Cell.totalDeaths) * 100
            radDeathsText = f'Mortes por Radiação: {radDeaths:.2f}%'

            highAcidDeaths = (Cell.highAcidDeaths / Cell.totalDeaths) * 100
            highAcidDeathsText = f'Mortes por Alto pH: {highAcidDeaths:.2f}%'
            lowAcidDeaths = (Cell.lowAcidDeaths / Cell.totalDeaths) * 100
            lowAcidDeathsText = f'Mortes por Baixo pH: {lowAcidDeaths:.2f}%'
            totalAcidDeaths = Cell.highAcidDeaths + Cell.lowAcidDeaths

            variableDeaths = totalTempDeaths + Cell.radDeaths + totalAcidDeaths

            energyDeaths = Cell.totalDeaths - variableDeaths
            energyDeathsPercent = (energyDeaths / Cell.totalDeaths) * 100

            energyDeathsText = f'Mortes por fome: {energyDeathsPercent:.2f}%'

            draw_text('Todas as células estão mortas', gameFont, vermelho, tela, 350, altura/6)
           
            draw_text(highTempDeathsText, gameFont, preto, tela, 355, altura/6 + 30)
            draw_text(lowTempDeathsText, gameFont, preto, tela, 355, altura/6 + 60)

            draw_text(highAcidDeathsText, gameFont, preto, tela, 355, altura/6 + 90)
            draw_text(lowAcidDeathsText, gameFont, preto, tela, 355, altura/6 + 120)

           
            draw_text(radDeathsText, gameFont, preto, tela, 355, altura/6 + 150)
            draw_text(energyDeathsText, gameFont, preto, tela, 355, altura/6 + 180)
            draw_text(f'Total de células na fase: {Cell.totalDeaths}', gameFont, preto, tela, 350, altura/6 + 210)


            if totalTempDeaths > energyDeaths and totalTempDeaths > totalAcidDeaths and totalTempDeaths > Cell.radDeaths:
                if highTempDeaths > lowTempDeaths:
                    draw_text('Maior quantidade de mortes foi por alta temperatura!', gameFont, preto, tela, 350, altura/6 + 240)
                if lowTempDeaths > highTempDeaths:
                    draw_text('Maior quantidade de mortes foi por baixa temperatura!', gameFont, preto, tela, 350, altura/6 + 240)
                if lowTempDeaths == highTempDeaths:
                    draw_text('Houve um mesmo número de mortes por alta e baixa temperatura!', gameFont, preto, tela, 350, altura/6 + 240)

            if totalAcidDeaths > energyDeaths and totalAcidDeaths > totalTempDeaths and totalAcidDeaths > Cell.radDeaths:
                if highAcidDeaths > lowAcidDeaths:
                    draw_text('Maior quantidade de mortes foi por alto pH!', gameFont, preto, tela, 350, altura/6 + 240)
                if lowAcidDeaths > highAcidDeaths:
                    draw_text('Maior quantidade de mortes foi por baixo pH!', gameFont, preto, tela, 350, altura/6 + 240)
                if highAcidDeaths == lowAcidDeaths:
                    draw_text('Houve um mesmo número de mortes por alto e baixo pH!', gameFont, preto, tela, 350, altura/6 + 240)

            if energyDeaths > totalTempDeaths and energyDeaths > totalAcidDeaths and energyDeaths > Cell.radDeaths:
                draw_text('Maior quantidade de mortes foi por falta de energia!', gameFont, preto, tela, 350, altura/6 + 240)

            if Cell.radDeaths > energyDeaths and Cell.radDeaths > totalAcidDeaths and Cell.radDeaths > totalTempDeaths:
                draw_text('Maior quantidade de mortes foi por radiação!', gameFont, preto, tela, 350, altura/6 + 240)

        pg.display.flip()