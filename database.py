import psycopg2

class Database:
    def __init__(self):
        self.conexao = psycopg2.connect(
            dbname="meuprojeto",
            user="postgres",
            password="raul",
            host="localhost",
            port="5432"
        )

    def get_conexao(self):
        return self.conexao
