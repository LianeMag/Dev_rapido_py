# Importando SQLite

import sqlite3 as lite 

# Criando conexão do Banco de Dados 

con = lite.connect('Lojinha_Moonli.db')

# Tabela criada e desativada pois ja foi criada no meu sistema

with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE Produtos(sku INTEGER PRIMARY KEY, nome TEXT, marca TEXT, preco TEXT, precodez TEXT, quantidade TEXT, garantia TEXT)")
















