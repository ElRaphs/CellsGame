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
amarelo = (242, 231, 0)
rosa = (236, 0, 242)
cinza = (150, 150, 150)
preto = (0, 0, 0)
azul_claro = (153, 217, 234)

MMbg = pg.transform.scale(pg.image.load('./images/MMbg.jpg'), (largura, altura))

MMfont = pg.font.Font('./fonts/MMfont.ttf', 100)
MMBfont = pg.font.Font('./fonts/MMfont.ttf', 50)
gameFont = pg.font.Font('./fonts/MMfont.ttf', 25)
backFont = pg.font.Font('./fonts/MMfont.ttf', 10)

painel = pg.Rect(0, 600, 1000, 150)