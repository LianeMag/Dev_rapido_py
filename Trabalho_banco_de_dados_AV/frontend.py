# Importando bibliotecas necessárias

from tkinter import *
from tkinter import ttk
from view import *
from tkinter import messagebox

# iniciando a janela.

janela=Tk()
janela.title('Cadastro')
janela.geometry("1295x520")
janela.configure(background='#FFE282')
janela.resizable(width= FALSE, height= FALSE)

# Dividindo a Janela em partes.

frame_esquerda=Frame(janela, width=565, height=550, bg='#FFE282')
frame_esquerda.grid(row=0, column=0, padx=0, pady=1, sticky=NSEW)


frame_direita=Frame (janela, width=800, height=550)
frame_direita.grid(row=0, column=1, rowspan=2, padx=1, pady=0, sticky=NSEW)

# Frase com nome do Banco de dados.

lblappnome=Label(frame_esquerda, fg='#FE7698', bg='#FFE282', anchor= NW,
            text='Bem vindo ao cadastro de Produtos da \n LOJINHA MOONLI',font=('futura', 16, 'bold'), padx=10, pady=20)
lblappnome.grid(row=0, column=1, columnspan=4)
        
# Função do botão cadastrar

def cadastrar():
   
   sku = txtSku.get()
   nome = txtnome.get()
   marca = txtmarca.get()
   preco = txtpreco.get()
   precodez = txtprecodez.get()
   quantidade = txtquantidade.get()
   garantia = txtgarantia.get()

   lista = [sku, nome, marca, preco, precodez, quantidade, garantia]

   if sku == '':
      messagebox.showerror('Erro', 'Parece que você está tentando inserir um produto sem seu SKU. \n Por favor insira-o.')
   else:
      inserir_info(lista)
      messagebox.showinfo('Oba!','Dados inseridos com Sucesso!')

      txtSku.delete(0,'end')
      txtnome.delete(0,'end')
      txtmarca.delete(0,'end')
      txtpreco.delete(0,'end')
      txtprecodez.delete(0,'end')
      txtquantidade.delete(0,'end')
      txtgarantia.delete(0,'end')

   for widget in frame_direita.winfo_children():
      widget.destroy()

   mostrar()

# Função do botão atualizar.

global tree

def atualizar():

   try: 

      treev_dados=tree.focus()
      treev_dicionario=tree.item(treev_dados)
      tree_lista=treev_dicionario['values']

      valor = tree_lista[0]

      txtSku.delete(0,'end')
      txtnome.delete(0,'end')
      txtmarca.delete(0,'end')
      txtpreco.delete(0,'end')
      txtprecodez.delete(0,'end')
      txtquantidade.delete(0,'end')
      txtgarantia.delete(0,'end')

      txtSku.insert(0,tree_lista[0])
      txtnome.insert(0,tree_lista[1])
      txtmarca.insert(0,tree_lista[2])
      txtpreco.insert(0,tree_lista[3])
      txtprecodez.insert(0,tree_lista[4])
      txtquantidade.insert(0,tree_lista[5])
      txtgarantia.insert(0,tree_lista[6])
      
      def update():
   
        sku = txtSku.get()
        nome = txtnome.get()
        marca = txtmarca.get()
        preco = txtpreco.get()
        precodez = txtprecodez.get()
        quantidade = txtquantidade.get()
        garantia = txtgarantia.get()

        lista = [nome, marca, preco, precodez, quantidade, garantia, valor]

        if sku == '':
             messagebox.showerror('Erro', 'Parece que você está tentando inserir um produto sem seu SKU. \n Por favor insira-o.')
        else:
             atualizar_info(lista)
             messagebox.showinfo('Oba!','Dados inseridos com Sucesso!')

             txtSku.delete(0,'end')
             txtnome.delete(0,'end')
             txtmarca.delete(0,'end')
             txtpreco.delete(0,'end')
             txtprecodez.delete(0,'end')
             txtquantidade.delete(0,'end')
             txtgarantia.delete(0,'end')

             mostrar()

      for widget in frame_direita.winfo_children():
            widget.destroy()

      mostrar()

      btnconfirmar=Button(frame_esquerda, command=update, fg='#FFE282', background='#B32AC4', relief=GROOVE, text='Comfirmar',
                                 font=('futura', 10, 'bold'), padx=60, pady=1)
      btnconfirmar.grid(row=12, column=1, columnspan=2)

   except IndexError():
      messagebox.showerror('ERRO', 'Por favor, selecione um dado na tabela.')
    
# Função do botão excluir.

def excluir():

   try:

      treev_dados=tree.focus()
      treev_dicionario=tree.item(treev_dados)
      tree_lista=treev_dicionario['values']
 
      valor = [tree_lista[0]]

      excluir_info(valor)
      messagebox.showinfo('Sucesso', 'dados excluidos com sucesso!')

      
      for widget in frame_direita.winfo_children():
            widget.destroy()

      mostrar()

   except TypeError():

      messagebox.showerror('ERRO', 'Por favor, selecione um dado na tabela.')

# Função do botão limpar.

def limpar():
   
   txtSku.delete(0,'end')
   txtnome.delete(0,'end')
   txtmarca.delete(0,'end')
   txtpreco.delete(0,'end')
   txtprecodez.delete(0,'end')
   txtquantidade.delete(0,'end')
   txtgarantia.delete(0,'end')
 
   mostrar()

# Criando as entradas de texto/dados e seus nomes.

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


#Label criada apenas para dar espaço entre a entrada de dados e os botões

lblfantasma=Label(frame_esquerda, bg='#FFE282', 
                    padx=70, pady=10)
lblfantasma.grid(row=9, column=2)

# Criando os Botões.

btncadastrar=Button(frame_esquerda, command=cadastrar, fg='#FFE282', background='#B32AC4', relief=GROOVE, text='Cadastrar',
                                 font=('futura', 13, 'bold'), padx=70, pady=5)
btncadastrar.grid(row=10, column=1)


btnatualizar=Button(frame_esquerda, command=atualizar, fg='#FFE282', background='#B32AC4', relief=GROOVE, text='Atualizar',
                                 font=('futura', 13, 'bold'), padx=70, pady=5)
btnatualizar.grid(row=10, column=2)


btnexcluir=Button(frame_esquerda, command=excluir, fg='#FFE282', background='#B32AC4', relief=GROOVE, text='Excluir',
                               font=('futura', 13, 'bold') , padx=82, pady=5)
btnexcluir.grid(row=11, column=1)


btnlimpar=Button(frame_esquerda, command=limpar, fg='#FFE282', background='#B32AC4', relief=GROOVE, text='Limpar', 
                              font=('futura', 13, 'bold'), padx=77, pady=5)
btnlimpar.grid(row=11, column=2)

# Criando a tabela com o método tree.

def mostrar():
    
    global tree

    lista = mostrar_dados()

    tree = ttk.Treeview(frame_direita, selectmode="browse", columns=('c1','c2','c3','c4','c5','c6','c7'), show="headings")

    tree.column('c1', width=45, minwidth=50, stretch=NO)
    tree.heading('#1', text='Sku')

    tree.column('c2', width=355, minwidth=50, stretch=NO)
    tree.heading('#2', text='Nome')

    tree.column('c3', width=60, minwidth=50, stretch=NO)
    tree.heading('#3', text='Marca')

    tree.column('c4', width=50, minwidth=50, stretch=NO)
    tree.heading('#4', text='Preço')

    tree.column('c5', width=100, minwidth=50, stretch=NO)
    tree.heading('#5', text='Preço c/+ 10%')

    tree.column('c6', width=150, minwidth=50, stretch=NO)
    tree.heading('#6', text='Quantidade Disponível')

    tree.column('c7', width=60, minwidth=50, stretch=NO)
    tree.heading('#7', text='Garantia')

    tree.grid(column=0, row=0, sticky='nsew')

    for item in lista:
       tree.insert('', 'end', values=item) 

# Scroll vertical e horizontal da tabela.

    vsb= ttk.Scrollbar(frame_direita, orient="vertical", command=tree.yview)
    hsb= ttk.Scrollbar(frame_direita, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')
    frame_direita.grid_rowconfigure(0, weight=12)   

# finalização para que apareça tudo que colocamos e a janela não se feche

mostrar()
janela.mainloop()