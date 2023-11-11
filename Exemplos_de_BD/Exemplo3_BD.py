# Lendo os dados inseridos

import psycopg2

conn = psycopg2.connect(database="postgres",user="postgres",password="1234",port="5432")
print("Conexão com o banco de Dados aberta com sucesso!")

comando = conn.cursor()
comando.execute(""" SELECT * FROM AGENDA where id = 2 """)
registro = comando.fetchone()
print("Dados encontrados ->", registro)

conn.commit()
print("Seleção realizada com sucesso!!!")
conn.close()