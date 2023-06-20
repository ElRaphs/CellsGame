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
    for c in range(500):
        energy = Energy(randint(0, largura), randint(0, altura))
        energies.add(energy)

    while True:
        relogio.tick(fps)
        tela.fill(cinza)

        energies.draw(tela)
        energies.update()
        cells.draw(tela)
        cells.update(tela, azul)

        collisions = pg.sprite.groupcollide(cells, energies, False, True)
        for cell, energy_list in collisions.items():
            for energy in energy_list:
                new_cell1 = Cell(uniform(-2,2), uniform(-2,2), cell.rect.x, cell.rect.y, 300)
                new_cell2 = Cell(uniform(-2,2), uniform(-2,2), cell.rect.x, cell.rect.y, 300)
                cells.add(new_cell1, new_cell2)
                cells.remove(cell)

        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                exit()

        pg.display.flip()

main_menu()