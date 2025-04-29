from flask import Flask, render_template, request, redirect, session, url_for

class App:
    def __init__(self):
        self.app = Flask(__name__)
        self.app.secret_key = 'secreto'  # precisa disso para usar sessões

        # Credenciais corretas
        self.EMAIL_CORRETO = 'fornecedor@gmail.com'
        self.SENHA_CORRETA = '2025'

        # Configurando as rotas
        self.configurar_rotas()

    def configurar_rotas(self):
        # Página inicial com os botões CLIENTE e FORNECEDOR
        @self.app.route('/')
        def index():
            return render_template('inicio.html')

        # Página de login do FORNECEDOR
        @self.app.route('/login', methods=['GET', 'POST'])
        def login():
            if request.method == 'POST':
                email = request.form['email']
                senha = request.form['senha']
                if email == self.EMAIL_CORRETO and senha == self.SENHA_CORRETA:
                    session['logado'] = True
                    return redirect(url_for('cliente'))
                else:
                    return "Você não tem acesso de Fornecedor! Tente novamente."
            return render_template('login.html')

        # Página de cadastro de cliente (acessível após login)
        @self.app.route('/cliente', methods=['GET', 'POST'])
        def cliente():
            if not session.get('logado'):
                return redirect(url_for('login'))

            if request.method == 'POST':
                nome = request.form['cliente-nome']
                endereco = request.form['endereco']
                # aqui você pode salvar os dados, se quiser
                return redirect(url_for('cliente'))
            return render_template('clientes.html')

        # Página de acompanhamento
        @self.app.route('/acompanhamentos')
        def acompanhamentos():
            return render_template('acompanhamento.html')

        # Página aberta para CLIENTE (carrega index.html)
        @self.app.route('/cliente-index')
        def cliente_index():
            return render_template('index.html')

        # Logout do FORNECEDOR
        @self.app.route('/logout')
        def logout():
            session.clear()
            return redirect(url_for('login'))

    def run(self):
        self.app.run(debug=True)

if __name__ == "__main__":
    app = App()
    app.run()
