# Excluindo dados

import psycopg2

conn = psycopg2.connect(database="postgres",user="postgres",password="1234",port="5432")
print("Conexão com o banco de Dados aberta com sucesso!")

comando = conn.cursor()
comando.execute(""" DELETE FROM AGENDA where id = 1 """)
conn.commit()

cont = comando.rowcount
print(cont,
"-> Registro excluído com sucesso!")
print("Exclusão realizada com sucesso!!!")
conn.close()