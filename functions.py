import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

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

def show_graphs_in_tabs(t, cellsN, y00, y01, y02, y10, y11):
    root = tk.Tk()
    root.title("Gráficos")
    root.iconbitmap('./images/icon.ico')

    tab_control = ttk.Notebook(root)

    tabs = ['Temperatura (K)', 'Salinidade (mg/L)', 'Acidez (pH)', 'Radiação (10¹² Bq)', 'Energia', 'Árvore']
    graph_data = [y00, y01, y02, y10, y11, None]

    for tab_title, data in zip(tabs, graph_data):
        tab = ttk.Frame(tab_control)
        tab_control.add(tab, text=tab_title)
        
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(t, cellsN, color='b')
        ax.set_xlabel('Tempo')
        ax.set_ylabel('Células')
        ax.set_title(tab_title)

        if data is not None:
            ax_twin = ax.twinx()
            ax_twin.plot(t, data, color='r' if tab_title == 'Temperatura (K)' else
                                      'g' if tab_title in ['Salinidade (mg/L)', 'Radiação (10¹² Bq)'] else
                                      'yellow' if tab_title == 'Acidez (pH)' else
                                      (1, 127/255, 39/255) if tab_title == 'Energia' else 'b')
            ax_twin.set_ylabel(tab_title)
        
        canvas = FigureCanvasTkAgg(fig, master=tab)
        canvas.draw()
        canvas.get_tk_widget().pack()

    tab_control.pack(expand=1, fill="both")
    root.mainloop()  

