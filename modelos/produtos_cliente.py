class ProdutoCliente:
    def __init__(self, conexao):
        self.conexao = conexao

    def cadastrar(self, nome, produto, quantidade, origem, destino, status):
        cursor = self.conexao.cursor()
        cursor.execute(
            "INSERT INTO produto_clientes (nome, produto, quantidade, origem, destino, status) VALUES (%s, %s, %s, %s, %s, %s)",
            (nome, produto, quantidade, origem, destino, status)
        )
        self.conexao.commit()
        cursor.close()

    def listar(self):
        cursor = self.conexao.cursor()
        cursor.execute("SELECT produto, origem, destino, nome, status FROM produto_clientes")
        resultados = cursor.fetchall()
        cursor.close()
        return resultados
