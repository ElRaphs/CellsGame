import pygame as pg
from sys import exit
from pygame.locals import *
from variables import *
from functions import *
from classes import *

pg.init()

def main_menu():
    NewGame = MMButton(500, 400, 212, 'Novo Jogo', MMBfont, verde, azul)

    while True:
        relogio.tick(fps)
        tela.blit(MMbg, (0, 0))

        draw_text('Inserir Título', MMfont, verde, tela, 250, 20)

        NewGame.update(tela)

        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                exit()

        pg.display.flip()

def level1():
    while True:
        relogio.tick(fps)
        tela.fill(branco)

main_menu()