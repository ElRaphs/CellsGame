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
    global test_cell
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
        
        if test_cell.energy >= 1:
            test_cell = Cell(-1, 1, test_cell.rect.x+5, test_cell.rect.y+5)
            cells.add(test_cell)
            test_cell.energy = 0

        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                exit()

        pg.display.flip()

main_menu()