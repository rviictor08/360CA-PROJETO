import psycopg2

<<<<<<< HEAD

=======
>>>>>>> fc82c94f1572f6d508de56458a0fb5ab2166698c
class Database:
    def __init__(self):
        self.conexao = psycopg2.connect(
            dbname="meuprojeto",
            user="postgres",
            password="raul",
            host="localhost",
<<<<<<< HEAD
            port="5432",
=======
            port="5432"
>>>>>>> fc82c94f1572f6d508de56458a0fb5ab2166698c
        )

    def get_conexao(self):
        return self.conexao
<<<<<<< HEAD

    # ///dados do meu banco

    # insert feitos no banco (menos pratico)


#     CREATE TABLE fornecedores (
#     id SERIAL PRIMARY KEY,
#     email VARCHAR(100),
#     senha VARCHAR(100)
# );

# CREATE TABLE produto_clientes (
#     id SERIAL PRIMARY KEY,
#     nome VARCHAR(255), -- Ajuste o tamanho conforme necessário
#     produto VARCHAR(255), -- Ajuste o tamanho conforme necessário
#     quantidade INTEGER,
#     origem VARCHAR(255), -- Ajuste o tamanho conforme necessário
#     destino VARCHAR(255), -- Ajuste o tamanho conforme necessário
#     status VARCHAR(255), -- Ajuste o tamanho conforme necessário
#     data_pedido TIMESTAMP WITHOUT TIME ZONE
# );


# CREATE TABLE produtos_fornecedores (
#     id SERIAL PRIMARY KEY,
#     nome_fornecedor VARCHAR(255), -- Ajuste o tamanho conforme necessário
#     produto_fornecedor VARCHAR(255), -- Ajuste o tamanho conforme necessário
#     quantidade INTEGER,
#     endereco VARCHAR(255), -- Ajuste o tamanho conforme necessário
#     valor_por_item NUMERIC(10, 2),
#     quantidade_por_valor NUMERIC(10, 2)
# );
=======
>>>>>>> fc82c94f1572f6d508de56458a0fb5ab2166698c
