#Testando botões de escolha

import tkinter
from tkinter import *

janela = tkinter.Tk()
janela.title("Botões de Escolha")
checkVar1 = IntVar()
checkVar2 = IntVar()

tkinter.Checkbutton(janela, text =
"Chocolate ao leite",variable = checkVar1,
 onvalue = 1, offvalue=0).grid(row=0,sticky=W)

tkinter.Checkbutton(janela, text =
"Chocolate meio amargo",variable = checkVar2,
 onvalue = 0, offvalue=1).grid(row=1,sticky=W)

janela.mainloop()