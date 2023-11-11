# Update de dados 

import psycopg2

conn = psycopg2.connect(database="postgres",user="postgres",password="1234",port="5432")
print("Conexão com o banco de Dados aberta com sucesso!")

comando = conn.cursor()
comando.execute(""" SELECT * FROM AGENDA where id = 2 """)
registro = comando.fetchone()
print("Dados encontrados ->", registro)

comando.execute(""" UPDATE AGENDA set telefone = 96385471 where id = 2""")
conn.commit()
print("Registro Atualizado com sucesso!!!")

comando = conn.cursor()
print("--- Consulta após a atualização ---")

comando.execute(""" SELECT * FROM AGENDA where id = 2 """)
registro = comando.fetchone()
print("Dados atualizados ->", registro)

conn.commit()
conn.close()