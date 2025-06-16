class Cliente:
    def __init__(self, conexao):
        self.conexao = conexao

    def cadastrar(self, nome, endereco):
        cursor = self.conexao.cursor()
        cursor.execute(
            "INSERT INTO clientes (nome, endereco) VALUES (%s, %s)",
            (nome, endereco)
        )
        self.conexao.commit()
        cursor.close()
