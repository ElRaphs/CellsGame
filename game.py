import pygame as pg
from sys import exit
from pygame.locals import *
from variables import *
from functions import *
from classes import *
from random import *
from pygame import mixer
from fase2 import level2

pg.init()

mixer.music.play(-1)

def main_menu():
    mixer.music.unpause()

    new_game_b = MMButton(400, 350, 212, 'Novo Jogo', MMBfont, verde, azul)
    wiki_b = MMButton(375, 450, 250, 'Enciclopédia', MMBfont, laranja, azul_claro)
    sair_b = MMButton(455, 650, 90, 'Sair', MMBfont, azul, vermelho)
    credits_b = MMButton(415, 550, 170, 'Créditos', MMBfont, amarelo, rosa)

    count = 0

    colors = [verde, vermelho, branco, azul, amarelo, azul_claro, rosa, laranja, verde_escuro, roxo]
    colorInd = 0    

    while True:
        mpos = pg.mouse.get_pos()
        relogio.tick(fps)
        tela.blit(MMbg, (0, 0))
        count += 1
        if count == 60:
            count = 0
            colorInd += 1
        if colorInd == 10:
            colorInd = 0

        draw_text('Simélula', MMfont, colors[colorInd], tela, 330, 20)

        new_game_b.update(tela)
        sair_b.update(tela)
        credits_b.update(tela)
        wiki_b.update(tela)

        click = False
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
                    clicked.play()

        if new_game_b.rect.collidepoint(mpos) and click:
            level1()
        if credits_b.rect.collidepoint(mpos) and click:
            credits()
        if wiki_b.rect.collidepoint(mpos) and click:
            wiki_screen()
        if sair_b.rect.collidepoint(mpos) and click:
            pg.quit()
            exit()

        pg.display.flip()

def select_level():
    phase1b = MMButton(50, 270, 155, '- Fase 1', MMBfont, azul_claro, azul)
    phase2b = MMButton(50, 370, 155, '- Fase 2', MMBfont, amarelo, laranja)
    phase3b = MMButton(50, 470, 155, '- Fase 3', MMBfont, laranja, vermelho)
    obj = MMbg

    while True:
        mpos = pg.mouse.get_pos()
        relogio.tick(fps)

        tela.blit(obj, (0, 0))

        phase1b.update(tela)
        phase2b.update(tela)
        phase3b.update(tela)

        click = False
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    main_menu()

        if phase1b.rect.collidepoint(mpos):
            obj = f1obj
            if click:
                level1()
        elif phase2b.rect.collidepoint(mpos):
            obj = f2obj
            if click:
                level1()
        elif phase3b.rect.collidepoint(mpos):
            obj = f3obj
            if click:
                level1()
        else:
            obj = MMbg

        pg.display.flip()

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
               
                new_cell1 = Cell(1*dx1, 1*dy1, cell.rect.x, cell.rect.y, c_energy, ambient, cellRadRes, celltemp, cellcolor)
                new_cell2 = Cell(1*dx2, 1*dy2, cell.rect.x, cell.rect.y, c_energy, ambient, cellRadRes, celltemp, cellcolor)
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
            start_game = False
            tela.fill(preto)
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

            if totalTempDeaths > totalAcidDeaths and totalTempDeaths > Cell.radDeaths:
                if highTempDeaths > lowTempDeaths:
                    tela.blit(MtempAlta, (0, 0))
                    show_stats(branco, tela, altura, highTempDeathsText, lowTempDeathsText, highAcidDeathsText,
                                lowAcidDeathsText, radDeathsText, energyDeathsText, Cell, gameFont)
                    draw_text('Maior quantidade de mortes foi por alta temperatura!', gameFont, branco,
                               tela, 10, altura-60)
                if lowTempDeaths > highTempDeaths:
                    tela.blit(MtempBaixa, (0, 0))
                    show_stats(branco, tela, altura, highTempDeathsText, lowTempDeathsText, highAcidDeathsText,
                                lowAcidDeathsText, radDeathsText, energyDeathsText, Cell, gameFont)
                    draw_text('Maior quantidade de mortes foi por baixa temperatura!', gameFont, preto, tela, 10, altura-60)
                if lowTempDeaths == highTempDeaths:
                    show_stats(branco, tela, altura, highTempDeathsText, lowTempDeathsText, highAcidDeathsText,
                                lowAcidDeathsText, radDeathsText, energyDeathsText, Cell, gameFont)
                    draw_text('Houve um mesmo número de mortes por alta e baixa temperatura!', gameFont, preto, tela, 10, altura-60)

            if totalAcidDeaths > totalTempDeaths and totalAcidDeaths > Cell.radDeaths:
                if highAcidDeaths > lowAcidDeaths:
                    tela.blit(MphAlto, (0, 0))
                    show_stats(branco, tela, altura, highTempDeathsText, lowTempDeathsText, highAcidDeathsText,
                                lowAcidDeathsText, radDeathsText, energyDeathsText, Cell, gameFont)
                    draw_text('Maior quantidade de mortes foi por alto pH!', gameFont, preto, tela, 10, altura-60)
                if lowAcidDeaths > highAcidDeaths:
                    tela.blit(MphBaixo, (0, 0))
                    show_stats(branco, tela, altura, highTempDeathsText, lowTempDeathsText, highAcidDeathsText,
                                lowAcidDeathsText, radDeathsText, energyDeathsText, Cell, gameFont)
                    draw_text('Maior quantidade de mortes foi por baixo pH!', gameFont, preto, tela, 10, altura-60)
                if highAcidDeaths == lowAcidDeaths:
                    show_stats(branco, tela, altura, highTempDeathsText, lowTempDeathsText, highAcidDeathsText,
                                lowAcidDeathsText, radDeathsText, energyDeathsText, Cell, gameFont)
                    draw_text('Houve um mesmo número de mortes por alto e baixo pH!', gameFont, preto, tela, 10, altura-60)

            #if energyDeaths > totalTempDeaths and energyDeaths > totalAcidDeaths and energyDeaths > Cell.radDeaths:
                #show_stats(branco, tela, altura, highTempDeathsText, lowTempDeathsText, highAcidDeathsText,
                                #lowAcidDeathsText, radDeathsText, energyDeathsText, Cell, gameFont)
                #draw_text('Maior quantidade de mortes foi por falta de energia!', gameFont, preto, tela, 10, altura-60)

            if Cell.radDeaths > totalAcidDeaths and Cell.radDeaths > totalTempDeaths:
                tela.blit(Mrad, (0, 0))
                show_stats(branco, tela, altura, highTempDeathsText, lowTempDeathsText, highAcidDeathsText,
                                lowAcidDeathsText, radDeathsText, energyDeathsText, Cell, gameFont)
                draw_text('Maior quantidade de mortes foi por radiação!', gameFont, preto, tela, 10, altura-60)

        pg.display.flip()

def wiki_screen():
    tempB = MMButton(10, 150, 300, '- Temperatura', MMBfont, azul_claro, vermelho)
    saltB = MMButton(10, 250, 250, '- Salinidade', MMBfont, laranja, rosa)
    acidB = MMButton(10, 350, 200, '- Nível pH', MMBfont, verde, amarelo)
    radB = MMButton(10, 450, 220, '- Radiação', MMBfont, roxo, verde)
    energyB = MMButton(10, 550, 200, '- Energia', MMBfont, amarelo, roxo)

    while True:
        mpos = pg.mouse.get_pos()
        relogio.tick(fps)
        tela.blit(wikiBG, (0, 0))

        draw_text('Esc: voltar', gameFont, branco, tela, 5, 5)
        tempB.update(tela)
        saltB.update(tela)
        acidB.update(tela)
        radB.update(tela)
        energyB.update(tela)

        click = False
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
                    clicked.play()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    clicked.play()
                    main_menu()

        if tempB.rect.collidepoint(mpos) and click:
            temp_wiki()
        if saltB.rect.collidepoint(mpos) and click:
            salt_wiki()
        if radB.rect.collidepoint(mpos) and click:
            rad_wiki()
        if energyB.rect.collidepoint(mpos) and click:
            energy_wiki()
        if acidB.rect.collidepoint(mpos) and click:
            acid_wiki()

        pg.display.flip()

def temp_wiki():
    while True:
        relogio.tick(fps)
        tela.blit(temp_wiki_bg, (0, 0))

        draw_text('Esc: voltar', gameFont, vermelho, tela, 890, 5)
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    clicked.play()
                    wiki_screen()

        pg.display.flip()

def salt_wiki():
    while True:
        relogio.tick(fps)
        tela.blit(salt_bg, (0, 0))

        draw_text('Esc: voltar', gameFont, vermelho, tela, 890, 5)
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    clicked.play()
                    wiki_screen()

        pg.display.flip()

def rad_wiki():
    while True:
        relogio.tick(fps)
        tela.blit(rad_bg, (0, 0))

        draw_text('Esc: voltar', gameFont, vermelho, tela, 890, 5)
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    clicked.play()
                    wiki_screen()

        pg.display.flip()

def acid_wiki():
    while True:
        relogio.tick(fps)
        tela.blit(acid_bg, (0, 0))

        draw_text('Esc: voltar', gameFont, vermelho, tela, 890, 5)
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    clicked.play()
                    wiki_screen()

        pg.display.flip()

def energy_wiki():
    while True:
        relogio.tick(fps)
        tela.blit(energy_bg, (0, 0))

        draw_text('Esc: voltar', gameFont, vermelho, tela, 890, 5)
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    clicked.play()
                    wiki_screen()

        pg.display.flip()

def credits():
    ny = -500
    while True:
        relogio.tick(fps)
        tela.fill(branco)
        tela.blit(creditsBG, (0, 0))

        draw_text('Esc: voltar', gameFont, preto, tela, 5, 5)
        draw_text('Luis Felipe Moreira - Licenciatura em Química', MMBfont, laranja, tela, 50, ny)
        draw_text('Luiz Felipe Crespo - Licenciatura em Física', MMBfont, vermelho, tela, 90, ny+100)
        draw_text('Raphael Groppo - Licenciatura em Física', MMBfont, rosa, tela, 100, ny+200)
        draw_text('Richardson de Miranda - Licenciatura em CMT', MMBfont, azul, tela, 50, ny+300)
        draw_text('Vitor da Silva - Licenciatura em Biologia', MMBfont, verde_escuro, tela, 95, ny+400)
       
        if ny <= 120:
            ny += 2
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    clicked.play()
                    main_menu()

        pg.display.flip()

main_menu()