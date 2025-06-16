class ProdutoFornecedor:
    def __init__(self, conexao):
        self.conexao = conexao

    def cadastrar(self, nome_fornecedor, produto_fornecedor, quantidade, endereco, valor_por_item, quantidade_por_valor):
        cursor = self.conexao.cursor()
        cursor.execute("""
            INSERT INTO produtos_fornecedores (
                nome_fornecedor,
                produto_fornecedor,
                quantidade,
                endereco,
                valor_por_item,
                quantidade_por_valor
            ) VALUES (%s, %s, %s, %s, %s, %s)
        """, (
            nome_fornecedor,
            produto_fornecedor,
            quantidade,
            endereco,
            valor_por_item,
            quantidade_por_valor
        ))
        self.conexao.commit()
        cursor.close()
