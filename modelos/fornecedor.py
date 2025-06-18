class Fornecedor:
    def __init__(self, conexao):
        self.conexao = conexao

    def autenticar(self, email, senha):
        cursor = self.conexao.cursor()
        cursor.execute(
            "SELECT * FROM fornecedores WHERE email = %s AND senha = %s",
            (email, senha)
        )
        resultado = cursor.fetchone()
        cursor.close()
        return resultado
