#Redimensionando Frames

import tkinter as tk
janela = tk.Tk()
janela.title("Trabalhando GUI em Python")
botao = tk.Button(janela,text="Botão da tela")
botao.pack()
janela.resizable(True, True)
janela.mainloop()