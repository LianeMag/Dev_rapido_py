import psycopg2

conn = psycopg2.connect(database="postgres",user="postgres",password="1234",port="5432")
print("Conexão com o Banco de Dados aberta com sucesso!")

comando = conn.cursor()
comando.execute(""" CREATE TABLE Agenda
                 (id INT PRIMARY KEY NOT NULL,
                 Nome TEXT NOT NULL,
                Telefone CHAR(12));
            """)
conn.commit()
print("Tabela criada com sucesso no BD!!!")
conn.close()
