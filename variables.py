import pygame as pg
from pygame import mixer

pg.init()

largura, altura = 1000, 750
relogio = pg.time.Clock()
fps = 60

tela = pg.display.set_mode((largura, altura))
pg.display.set_caption('Simélula')
pg.display.set_icon(pg.image.load('./images/icon.png'))

branco = (255, 255, 255)
verde = (0, 255, 0)
vermelho = (255, 0, 0)
azul = (0, 0, 255)
amarelo = (242, 231, 0)
rosa = (236, 0, 242)
cinza = (150, 150, 150)
preto = (0, 0, 0)
azul_claro = (153, 217, 234)
verde_escuro = (34, 177, 76)
laranja = (249, 118, 0)
roxo = (166, 20, 182)

MMbg = pg.transform.scale(pg.image.load('./images/MMbg.jpg'), (largura, altura))
creditsBG = pg.image.load('./images/creditsBG.jpg')
creditsBG.set_alpha(50)
wikiBG = pg.image.load('./images/TutorialBG.jpg')
temp_wiki_bg = pg.transform.scale(pg.image.load('./images/temp_bg.png'), (largura, altura))
salt_bg = pg.image.load('./images/SaltTutorial.png')
energy_bg = pg.image.load('./images/energyBG.jpg')
acid_bg = pg.image.load('./images/acidTutorial.jpg')
rad_bg = pg.image.load('./images/RadTutorial.png')
f1obj = pg.transform.scale(pg.image.load('./images/f1obj.png'), (largura, altura))
f2obj = pg.transform.scale(pg.image.load('./images/f2obj.png'), (largura, altura))
f3obj = pg.transform.scale(pg.image.load('./images/f3obj.png'), (largura, altura))
MtempAlta = pg.image.load('./images/MtempAlta.png')
MtempBaixa = pg.image.load('./images/MtempBaixa.png')
MphBaixo = pg.image.load('./images/MphBaixo.png')
MphAlto = pg.image.load('./images/MphAlto.png')
Mrad = pg.image.load('./images/Mrad.png')
MsalAlta = pg.image.load('./images/MsalAlta.png')
MsalBaixa = pg.image.load('./images/MsalBaixa.png')

MMfont = pg.font.Font('./fonts/MMfont.ttf', 100)
MMBfont = pg.font.Font('./fonts/MMfont.ttf', 50)
gameFont = pg.font.Font('./fonts/MMfont.ttf', 25)
backFont = pg.font.Font('./fonts/MMfont.ttf', 10)

ambience = mixer.music.load('./sounds/ambience_sound.mp3')
clicked = mixer.Sound('./sounds/click.wav')

painel = pg.Rect(0, 600, 1000, 150)
