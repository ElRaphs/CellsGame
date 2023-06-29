import pygame as pg
from sys import exit
from pygame.locals import *
from variables import *
from functions import *
from classes import *
from random import *

pg.init()

def main_menu():
    new_game_b = MMButton(400, 400, 212, 'Novo Jogo', MMBfont, verde, azul)
    sair_b = MMButton(455, 650, 90, 'Sair', MMBfont, azul, verde)
    credits_b = MMButton(415, 520, 170, 'Créditos', MMBfont, amarelo, rosa)    

    while True:
        mpos = pg.mouse.get_pos()
        relogio.tick(fps)
        tela.blit(MMbg, (0, 0))

        draw_text('Inserir Título', MMfont, verde, tela, 250, 20)

        new_game_b.update(tela)
        sair_b.update(tela)
        credits_b.update(tela)
        click = False
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if new_game_b.rect.collidepoint(mpos) and click:
            level1()
        if sair_b.rect.collidepoint(mpos) and click:
            pg.quit()
            exit()

        pg.display.flip()

def level1():
    energies = pg.sprite.Group()
    cells = pg.sprite.Group()
    cells.add(test_cell)
    
    c_energy = 150

    ambient = Ambient(300, 10, 7)

    tempoFPS = 0
    tempo = 0

    tempBtn = SlideButton(vermelho, 0, 610)
    acidBtn = SlideButton(amarelo, 7, 660)
    radBtn = SlideButton(verde, 0, 710)

    for c in range(400):
        energy = Energy(randint(0, largura), randint(40, 600))
        energies.add(energy)

    while True:
        tempoFPS += 1
        if len(energies) <= 150:
            energy = Energy(randint(40, largura), randint(40, 600))
            energies.add(energy)
        if tempoFPS == 60:
            tempoFPS = 0
            tempo += 1
        relogio.tick(fps)
        tela.fill(cinza)

        mx, my = pg.mouse.get_pos()

        energies.draw(tela)
        energies.update()
        cells.draw(tela)
        cells.update(tela)

        ambient.draw(f'temperatura: {ambient.temp} K', tela, vermelho, 0, 5, 10)
        ambient.draw(f'pressão: {ambient.press} Pa', tela, azul, 250, 5, 5)
        ambient.draw(f'pH: {ambient.acid}', tela, amarelo, 2*250, 5, 10)
        ambient.draw(f'Radioatividade: {ambient.rad} Bq', tela, verde, 3*250, 5, 10)

        pg.draw.rect(tela, branco, (0, 40, 130, 50))
        draw_text(f'tempo: {tempo} s', gameFont, preto, tela, 5, 40)
        draw_text(f'Células: {len(cells)}', gameFont, preto, tela, 5, 60)

        pg.draw.rect(tela, azul_claro, painel)

        ambient.rad = radBtn.rect.centerx - 5
        ambient.acid = acidBtn.rect.centerx-15
        ambient.temp = tempBtn.rect.centerx + 285
        ambient.press = int(ambient.temp*8.31)

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

                new_cell1 = Cell(1*dx1, 1*dy1, cell.rect.x, cell.rect.y, c_energy, ambient, 150, 150, 150)
                new_cell2 = Cell(1*dx2, 1*dy2, cell.rect.x, cell.rect.y, c_energy, ambient, 150, 150, 150)
                cells.add(new_cell1, new_cell2)
                cells.remove(cell)

        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                exit()

        pg.display.flip()

main_menu()