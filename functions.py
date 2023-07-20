def draw_text(texto, fonte, cor, tela, posx, posy):
    TextObj = fonte.render(texto, True, cor)
    TextRect = TextObj.get_rect()
    TextRect.topleft = (posx, posy)
    tela.blit(TextObj, TextRect)

def show_stats(cor, tela, high, HTD, LTD, HAD, LAD, RD, ED, CC, font):
    draw_text('Todas as células estão mortas', font, cor, tela, 10, high-300)
           
    draw_text(HTD, font, cor, tela, 10, high-270)
    draw_text(LTD, font, cor, tela, 10, high-240)

    draw_text(HAD, font, cor, tela, 10, high-210)
    draw_text(LAD, font, cor, tela, 10, high-180)
    
    draw_text(RD, font, cor, tela, 10, high-150)
    draw_text(ED, font, cor, tela, 10, high-120)
    draw_text(f'Total de células na fase: {CC.totalDeaths}', font, cor, tela, 10, high-90)
