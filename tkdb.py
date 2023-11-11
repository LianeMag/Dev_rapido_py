# Importando Tkinter

from tkinter import *
from tkinter import font
from cgitb import text 
from tkinter import ttk

# iniciando a janela 

janela=Tk()
janela.title('Cadastro')
janela.geometry("1265x550")
janela.configure(background='#FFE282')
janela.resizable(width= FALSE, height= FALSE)

# Dividindo a Janela 

frame_esquerda=Frame(janela, width=565, height=550, bg='#FFE282')
frame_esquerda.grid(row=0, column=0, padx=0, pady=1, sticky=NSEW)


frame_direita=Frame (janela, width=700, height=550, bg='#F0DDEE')
frame_direita.grid(row=0, column=1, rowspan=2, padx=1, pady=0, sticky=NSEW)


# Criando Label e Entry

lblappnome=Label(frame_esquerda, fg='#FE7698', bg='#FFE282', anchor= NW,
            text='Bem vindo ao cadastro de Produtos da \n LOJINHA MOONLI',font=('futura', 16, 'bold'), padx=10, pady=20)
lblappnome.grid(row=0, column=1, columnspan=4)
        

txtSku=Entry(frame_esquerda, width=20, borderwidth=5, relief=RIDGE, 
            fg='#000000', bg='#FFFFFF', font=('futura', 12, 'bold'))
txtSku.grid(row=1, column=2, columnspan=1, pady=1)                
lbSku=Label(frame_esquerda, fg='#FE7698', bg='#FFE282', 
            text='SKU do Produto:',font=('futura', 12, 'bold'), padx=20, pady=1)
lbSku.grid(row=1, column=1)



txtnome=Entry(frame_esquerda, width=20, borderwidth=5, relief=RIDGE, 
            fg='#000000', bg='#FFFFFF',  font=('futura', 12, 'bold'))
txtnome.grid(row=2, column=2, columnspan=1, pady=1)
lblnome=Label(frame_esquerda, fg='#FE7698', bg='#FFE282', 
            text='Nome do Produto:',font=('futura', 12, 'bold'), padx=20, pady=1)
lblnome.grid(row=2, column=1)



txtmarca=Entry(frame_esquerda, width=20, borderwidth=5, relief=RIDGE, 
            fg='#000000', bg='#FFFFFF',  font=('futura', 12, 'bold'))
txtmarca.grid(row=3, column=2, columnspan=1, pady=1)
lblmarca=Label(frame_esquerda, fg='#FE7698', bg='#FFE282', 
            text='Marca do Produto:',font=('futura', 12, 'bold'), padx=20, pady=1)
lblmarca.grid(row=3, column=1)



txtpreco=Entry(frame_esquerda, width=20, borderwidth=5, relief=RIDGE, 
            fg='#000000', bg='#FFFFFF',  font=('futura', 12, 'bold'))
txtpreco.grid(row=4, column=2, columnspan=1, pady=1)
lblpreco=Label(frame_esquerda, fg='#FE7698', bg='#FFE282', 
            text='Preço:',font=('futura', 12, 'bold'), padx=20, pady=1)
lblpreco.grid(row=4, column=1)



txtprecodez=Entry(frame_esquerda, width=20, borderwidth=5, relief=RIDGE, 
                    fg='#000000', bg='#FFFFFF',  font=('futura', 12, 'bold'))
txtprecodez.grid(row=5, column=2, columnspan=1, pady=2)
lblprecodez=Label(frame_esquerda, fg='#FE7698', bg='#FFE282', 
                    text='Preço com +10%:',font=('futura', 12, 'bold'), padx=20, pady=10)
lblprecodez.grid(row=5, column=1)



txtquantidade=Entry(frame_esquerda, width=20, borderwidth=5, relief=RIDGE, 
                    fg='#000000', bg='#FFFFFF',  font=('futura', 12, 'bold'))
txtquantidade.grid(row=6, column=2, columnspan=1, pady=2)
lblquantidade=Label(frame_esquerda, fg='#FE7698', bg='#FFE282', 
                    text='Quantidade disponível:',font=('futura', 12, 'bold'), padx=20, pady=10)
lblquantidade.grid(row=6, column=1)



txtgarantia=Entry(frame_esquerda, width=20, borderwidth=5, relief=RIDGE, 
                fg='#000000', bg='#FFFFFF',  font=('futura', 12, 'bold'))
txtgarantia.grid(row=7, column=2, columnspan=1, pady=2)
lblgarantia=Label(frame_esquerda, fg='#FE7698', bg='#FFE282', 
                text='Garantia:', font=('futura', 12, 'bold'), padx=20, pady=10)
lblgarantia.grid(row=7, column=1)


#Label criada apenas para dar espaço entre o entry e os buttons

lblfantasma=Label(frame_esquerda, bg='#FFE282', 
                    padx=70, pady=10)
lblfantasma.grid(row=9, column=2)


# Criando os Botões

btncadastrar=Button(frame_esquerda, fg='#FFE282', background='#B32AC4', relief=GROOVE, text='Cadastrar',
                                 font=('futura', 13, 'bold'), padx=70, pady=5)
btncadastrar.grid(row=10, column=1)


btnatualizar=Button(frame_esquerda, fg='#FFE282', background='#B32AC4', relief=GROOVE, text='Atualizar',
                                 font=('futura', 13, 'bold'), padx=70, pady=5)
btnatualizar.grid(row=10, column=2)


btnexcluir=Button(frame_esquerda, fg='#FFE282', background='#B32AC4', relief=GROOVE, text='Excluir',
                               font=('futura', 13, 'bold') , padx=82, pady=5)
btnexcluir.grid(row=11, column=1)


btnlimpar=Button(frame_esquerda, fg='#FFE282', background='#B32AC4', relief=GROOVE, text='Limpar', 
                              font=('futura', 13, 'bold'), padx=77, pady=5)
btnlimpar.grid(row=11, column=2)

# Criando a tabela

tabela_cad= ["Sku", "nome", "marca", "preco", "precodez", "quantidade", "garantia" ]

tree = ttk.Treeview(frame_direita, selectmode="extended", columns= "tabela_cad", show="headings")

# Scroll vertical e horizontal

vsb= ttk.Scrollbar(frame_direita, orient="vertical", command=tree.yview)
hsb= ttk.Scrollbar(frame_direita, orient="horizontal", command=tree.xview)

tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

tree.grid(column=0, row=0, sticky='nsew')
vsb.grid(column=1, row=0, sticky='ns')
hsb.grid(column=0, row=1, sticky='ew')
frame_direita.grid_rowconfigure(0, weight=12)

hd=['nw','nw','nw','nw','nw','center','center']
h=[70, 170, 140, 100, 120, 50, 100]
n=0



janela.mainloop()