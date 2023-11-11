import psycopg2

conn = psycopg2.connect(database="postgres",user="postgres",password="1234",port="5432")
print("Conexão com o banco de Dados aberta com sucesso!")

comando = conn.cursor()
comando.execute(""" INSERT INTO AGENDA (id,Nome, Telefone)
VALUES (2,'Pessoa 2', '900235478')
""")

conn.commit()
print("Inserção realizada com sucesso!!!")
conn.close()
