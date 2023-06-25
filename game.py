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

    cor1 = azul
    cor = cor1
    cor2 = vermelho

    c_energy1 = 300
    c_energy = c_energy1
    c_energy2 = 600

    chance1 = randint(1, 100)
    chance = chance1
    chance2 = 1

    ambient = Ambient(300, 10, 7)

    for c in range(500):
        energy = Energy(randint(0, largura), randint(0, altura))
        energies.add(energy)

    while True:
        relogio.tick(fps)
        tela.fill(cinza)

        energies.draw(tela)
        energies.update()
        cells.draw(tela)
        cells.update(tela)

        ambient.draw(f'temperatura: {ambient.temp} K', tela, vermelho, 0)
        ambient.draw(f'pressão: {ambient.press} Pa', tela, azul, 250)
        ambient.draw(f'pH: {ambient.acid}', tela, amarelo, 2*250)
        ambient.draw(f'Radioatividade: {ambient.rad} Bq', tela, verde, 3*250)

        collisions = pg.sprite.groupcollide(cells, energies, False, True)
        for cell, energy_list in collisions.items():
            for energy in energy_list:
                if chance > 1:
                    cor = cor1
                    c_energy = c_energy1
                    chance = randint(1, 100)
                if chance <= 1:
                    cor = cor2
                    c_energy = c_energy2
                    chance = chance2

                dx1 = randint(-1, 1)
                dx2 = randint(-1, 1)
                dy1 = randint(-1, 1)
                dy2 = randint(-1, 1)
                if (dx1 == 0 and dy1 == 0) or (dx2 == 0 and dy2 == 0) or (dx1 == dx2 and dy1 == dy2):
                    dx1 = -1
                    dx2 = 1
                    dy1 = -1
                    dy2 = 1
                new_cell1 = Cell(1 * dx1, 1 * dy1, cell.rect.x, cell.rect.y, c_energy, cor, chance)
                new_cell2 = Cell(1 * dx2, 1 * dy2, cell.rect.x, cell.rect.y, c_energy, cor, chance)
                cells.add(new_cell1, new_cell2)
                cells.remove(cell)

        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                exit()

        pg.display.flip()

main_menu()