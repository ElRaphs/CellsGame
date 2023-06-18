import pygame as pg

pg.init()

largura, altura = 1000, 750
relogio = pg.time.Clock()
fps = 60

tela = pg.display.set_mode((largura, altura))
pg.display.set_caption('Inserir Nome')

branco = (255, 255, 255)
verde = (0, 255, 0)
vermelho = (255, 0, 0)
azul = (0, 0, 255)

MMbg = pg.image.load('./images/MMbg.jpg')

MMfont = pg.font.Font('./fonts/MMfont.ttf', 100)
MMBfont = pg.font.Font('./fonts/MMfont.ttf', 50)