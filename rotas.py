from flask import render_template, request, redirect, session, url_for, jsonify

# Importação dos modelos (entidades) que encapsulam a lógica de banco
from modelos.cliente import Cliente
from modelos.fornecedor import Fornecedor
from modelos.produtos_cliente import ProdutoCliente
from modelos.produtos_fornecedor import ProdutoFornecedor


class Rotas:
    """Classe responsável por registrar todas as rotas da aplicação.

    A classe recebe a instância do Flask (app) e a conexão com o banco de dados
    (obtida a partir da classe Database). Ela cria instâncias dos modelos,
    delegando a eles a responsabilidade de manipular dados no banco.
    """

    def __init__(self, app, db):
        self.app = app
        self.conexao = db.get_conexao()

        # Instanciando os modelos, passando a conexão para cada um
        self.cliente_model = Cliente(self.conexao)
        self.fornecedor_model = Fornecedor(self.conexao)
        self.produto_cliente_model = ProdutoCliente(self.conexao)
        self.produto_fornecedor_model = ProdutoFornecedor(self.conexao)

        # Registra todas as rotas na aplicação
        self.registrar_rotas()

    # ---------------------------------------------------------------------
    # Definição das rotas
    # ---------------------------------------------------------------------
    def registrar_rotas(self):

        # ----------------------- Rota inicial ----------------------------
        @self.app.route('/')
        def index():
            return render_template('inicio.html')

        # --------------------- Rota de login -----------------------------
        @self.app.route('/login', methods=['GET', 'POST'])
        def login():
            if request.method == 'POST':
                email = request.form['email']
                senha = request.form['senha']

                # Autentica fornecedor usando o modelo
                fornecedor = self.fornecedor_model.autenticar(email, senha)

                if fornecedor:
                    session['logado'] = True
                    return redirect(url_for('cliente'))
                else:
                    return "Email ou senha incorretos!"
            return render_template('login.html')

        # -------------------- Rota de cliente/fornecedor ----------------
        @self.app.route('/fornecedor', methods=['GET', 'POST'])
        def cliente():
            # Garante que o usuário esteja logado
            if not session.get('logado'):
                return redirect(url_for('login'))

            if request.method == 'POST':
                nome = request.form['cliente-nome']
                endereco = request.form['endereco']

                # Cadastra cliente usando o modelo
                self.cliente_model.cadastrar(nome, endereco)
                return redirect(url_for('cliente'))

            return render_template('fornecedor.html')

        # --------------- Rota de cadastro de fornecedor -----------------
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
                self.produto_fornecedor_model.cadastrar(
                    nome_fornecedor,
                    produto_fornecedor,
                    quantidade,
                    endereco,
                    valor_por_item,
                    quantidade_por_valor
                )
                mensagem = "Fornecedor cadastrado com sucesso!"
            except Exception as e:
                mensagem = f"Erro ao cadastrar fornecedor: {e}"

            return render_template('fornecedor.html', mensagem=mensagem)

        # --------------- Rota de cadastro de cliente --------------------
        @self.app.route('/cadastrar_cliente', methods=['POST'])
        def adicionar_cliente():
            nome_cliente = request.form['fornecedor-nome']
            produto = request.form['produto']
            quantidade = request.form['quantidade']
            destino = request.form['destino']

            try:
                self.produto_cliente_model.cadastrar(
                    nome_cliente,
                    produto,
                    int(quantidade),
                    'Armazém Central',
                    destino,
                    'Em transporte'
                )
                mensagem = "Cliente cadastrado com sucesso!"
            except Exception as e:
                mensagem = f"Erro ao cadastrar o cliente: {e}"

            return render_template('index.html', mensagem=mensagem)

        # ------------------ Rota de acompanhamento ----------------------
        @self.app.route('/acompanhamentos')
        def acompanhamentos():
            pedidos = self.produto_cliente_model.listar()
            return render_template('acompanhamento.html', pedidos=pedidos)

        # ---------------- Rota index do cliente ------------------------
        @self.app.route('/cliente-index')
        def cliente_index():
            return render_template('index.html')

        # ---------------------- Rota de logout --------------------------
        @self.app.route('/logout')
        def logout():
            session.clear()
            return redirect(url_for('login'))
