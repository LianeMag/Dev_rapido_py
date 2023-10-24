#

import tkinter 
janela = tkinter.Tk()
janela.title("Trabalhando GUI em Python")
botao = tkinter.Button(janela,text="Botão da tela")
botao.pack()
janela.resizable(True, True)
janela.mainloop()