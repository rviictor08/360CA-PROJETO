<<<<<<< HEAD
from datetime import datetime


=======
>>>>>>> fc82c94f1572f6d508de56458a0fb5ab2166698c
class ProdutoCliente:
    def __init__(self, conexao):
        self.conexao = conexao

    def cadastrar(self, nome, produto, quantidade, origem, destino, status):
        cursor = self.conexao.cursor()
        cursor.execute(
<<<<<<< HEAD
            """
            INSERT INTO produto_clientes
            (nome, produto, quantidade, origem, destino, status, data_pedido)
            VALUES (%s, %s, %s, %s, %s, %s, NOW())
            """,
            (nome, produto, quantidade, origem, destino, status),
=======
            "INSERT INTO produto_clientes (nome, produto, quantidade, origem, destino, status) VALUES (%s, %s, %s, %s, %s, %s)",
            (nome, produto, quantidade, origem, destino, status)
>>>>>>> fc82c94f1572f6d508de56458a0fb5ab2166698c
        )
        self.conexao.commit()
        cursor.close()

    def listar(self):
        cursor = self.conexao.cursor()
<<<<<<< HEAD
        cursor.execute(
            """
            SELECT produto, origem, destino, nome, data_pedido
            FROM produto_clientes
            """
        )
        resultados_brutos = cursor.fetchall()
        cursor.close()

        resultado_final = []
        agora = datetime.now()

        for produto, origem, destino, nome, data_pedido in resultados_brutos:
            # Calcula o número de dias passados desde o pedido
            tempo_passado = agora - data_pedido
            dias = tempo_passado.total_seconds() / (60 * 60 * 24)

            # Define o status com base nos dias
            if dias < 1:
                status = "Em transporte"
            elif dias < 2:
                status = "Chegando"
            else:
                status = "Entregue"

            resultado_final.append((produto, origem, destino, nome, status))

        return resultado_final


# esse codigo seria do projeto oficial porem a siimulacaço seria o java da propria tela acompanhaento com as alteracoes
=======
        cursor.execute("SELECT produto, origem, destino, nome, status FROM produto_clientes")
        resultados = cursor.fetchall()
        cursor.close()
        return resultados
>>>>>>> fc82c94f1572f6d508de56458a0fb5ab2166698c
