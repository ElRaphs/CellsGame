from matplotlib import pyplot as plt

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

def show_graphs(t, cellsN, y00, y01, y02, y10, y11, y12=None):
    fig, axs = plt.subplots(2, 3)

    axs[0, 0].plot(t, cellsN, color='b')
    ax0 = axs[0, 0].twinx()
    ax0.plot(t, y00, color='r')
    axs[0, 0].set_title('Temperatura')

    axs[0, 1].plot(t, cellsN, color='b')
    ax1 = axs[0, 1].twinx()
    ax1.plot(t, y01, color='g')
    axs[0, 1].set_title('Salinidade')

    axs[0, 2].plot(t, cellsN, color='b')
    ax2 = axs[0, 2].twinx()
    ax2.plot(t, y02, color='yellow')
    axs[0, 2].set_title('Acidez')

    axs[1, 0].plot(t, cellsN, color='b')
    ax3 = axs[1, 0].twinx()
    ax3.plot(t, y10, color='g')
    axs[1, 0].set_title('Radiação')

    axs[1, 1].plot(t, cellsN, color='b')
    ax4 = axs[1, 1].twinx()
    ax4.plot(t, y11, color=(1, 127/255, 39/255))
    axs[1, 1].set_title('Energia')  

    axs[1, 2].plot(t, cellsN, color='b')
    ax5 = axs[1, 2].twinx()
    ax5.plot(t, y12)
    axs[1, 2].set_title('Árvore')

    plt.tight_layout()
    plt.show()  

