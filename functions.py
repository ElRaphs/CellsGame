def draw_text(texto, fonte, cor, tela, posx, posy):
    TextObj = fonte.render(texto, True, cor)
    TextRect = TextObj.get_rect()
    TextRect.topleft = (posx, posy)
    tela.blit(TextObj, TextRect)