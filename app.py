from flask import Flask, render_template, request, redirect, session, url_for
import psycopg2

class App:
    def __init__(self):
        self.app = Flask(__name__)
        self.app.secret_key = 'secreto'

        # Conexão com o PostgreSQL
        self.conexao = psycopg2.connect(
            dbname="meuprojeto",
            user="postgres",
            password="raul",  # substitua com sua senha
            host="localhost",
            port="5432"
        )

        self.configurar_rotas()

    def configurar_rotas(self):
        @self.app.route('/')
        def index():
            return render_template('inicio.html')

        @self.app.route('/login', methods=['GET', 'POST'])
        def login():
            if request.method == 'POST':
                email = request.form['email']
                senha = request.form['senha']

                cursor = self.conexao.cursor()
                cursor.execute("SELECT * FROM fornecedores WHERE email = %s AND senha = %s", (email, senha))
                fornecedor = cursor.fetchone()
                cursor.close()

                if fornecedor:
                    session['logado'] = True
                    return redirect(url_for('cliente'))
                else:
                    return "Email ou senha incorretos!"
            return render_template('login.html')

        @self.app.route('/fornecedor', methods=['GET', 'POST'])
        def cliente():
            if not session.get('logado'):
                return redirect(url_for('login'))

            if request.method == 'POST':
                nome = request.form['cliente-nome']
                endereco = request.form['endereco']

                cursor = self.conexao.cursor()
                cursor.execute("INSERT INTO clientes (nome, endereco) VALUES (%s, %s)", (nome, endereco))
                self.conexao.commit()
                cursor.close()

                return redirect(url_for('cliente'))
            return render_template('fornecedor.html')

        @self.app.route('/cadastrar_fornecedor', methods=['POST'])
        def cadastrar_fornecedor():
            if not session.get('logado'):
                return redirect(url_for('login'))

            nome_fornecedor = request.form['nome_fornecedor']
            produto_fornecedor = request.form['produto_fornecedor']
            quantidade = request.form['quantidade']
            endereco = request.form['endereco']
            valor_por_item = request.form['valor_por_item']
            quantidade_por_valor = request.form['quantidade_por_valor']

            try:
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
                mensagem = "Fornecedor cadastrado com sucesso!"
            except Exception as e:
                mensagem = f"Erro ao cadastrar fornecedor: {e}"

            return render_template('fornecedor.html', mensagem=mensagem)

        @self.app.route('/cadastrar_cliente', methods=['POST'])
        def adicionar_cliente():
            nome_cliente = request.form['fornecedor-nome']
            produto = request.form['produto']
            quantidade = request.form['quantidade']
            destino = request.form['destino']

            try:
                cursor = self.conexao.cursor()
                cursor.execute(
                    "INSERT INTO produto_clientes (nome, produto, quantidade, origem, destino, status) VALUES (%s, %s, %s, %s, %s, %s)",
                    (nome_cliente, produto, int(quantidade), 'Armazém Central', destino, 'Em transporte')
                )
                self.conexao.commit()
                cursor.close()
                mensagem = "Cliente cadastrado com sucesso!"
            except Exception as e:
                mensagem = f"Erro ao cadastrar o cliente: {e}"

            return render_template('index.html', mensagem=mensagem)

        @self.app.route('/acompanhamentos')
        def acompanhamentos():
            cursor = self.conexao.cursor()
            cursor.execute("SELECT produto, origem, destino, nome, status FROM produto_clientes")
            pedidos = cursor.fetchall()
            cursor.close()
            return render_template('acompanhamento.html', pedidos=pedidos)

        @self.app.route('/cliente-index')
        def cliente_index():
            return render_template('index.html')

        @self.app.route('/logout')
        def logout():
            session.clear()
            return redirect(url_for('login'))

    def run(self):
        self.app.run(debug=True)

if __name__ == "__main__":
    app = App()
    app.run()
