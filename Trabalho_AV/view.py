# Importando SQLite 

import sqlite3 as lite

# Criando conexao com o BD

con=lite.connect('Lojinha_Moonli.db')

# Função Inserir dados 

def inserir_info(i):

    with con:
       cur = con.cursor()
       query = "INSERT INTO Produtos (sku, nome, marca, preco, precodez, quantidade, garantia) VALUES (?, ?, ?, ?, ?, ?, ?)"
       cur.execute(query, i)

# Função Acessar os dados 

def mostrar_dados():
    lista = []
    with con:
       cur = con.cursor()
       query = "SELECT * FROM Produtos"
       cur.execute(query)
       dados = cur.fetchall()

       for i in dados:
           lista.append(i)

    return lista

# Função Atualizar dados 

def atualizar_info(i):

   with con:
       cur = con.cursor()
       query = "UPDATE Produtos SET nome=?, marca=?, preco=?, precodez=?, quantidade=?, garantia=? WHERE sku=?"
       cur.execute(query, i)

# Função Deletar dados

def excluir_info(i):

   with con:
       cur=con.cursor()
       query = "DELETE FROM Produtos WHERE Sku=?"
       cur.execute(query, i)

