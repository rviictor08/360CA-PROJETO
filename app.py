from flask import Flask, request, jsonify, send_from_directory
import os

app = Flask(__name__)

# Definindo as classes para Fornecedor e Cliente
class Fornecedor:
    def __init__(self, nome, produto, valor, quantidade):
        self.nome = nome
        self.produto = produto
        self.valor = valor
        self.quantidade = quantidade  # Novo atributo: Quantidade

class Cliente:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco

# Armazenando fornecedores e clientes
fornecedores = []
clientes = []

# Rota para servir o index.html
@app.route('/')
def index():
    return send_from_directory(os.getcwd(), 'index.html')

# Rota para cadastrar fornecedor
@app.route('/fornecedor', methods=['POST'])
def cadastrar_fornecedor():
    data = request.get_json()
    fornecedor = Fornecedor(
        data['nome'],
        data['produto'],
        data['valor'],
        data['quantidade']  # Quantidade
    )
    fornecedores.append(fornecedor)
    return jsonify({"message": "Fornecedor cadastrado com sucesso!"}), 201

# Rota para cadastrar cliente
@app.route('/cliente', methods=['POST'])
def cadastrar_cliente():
    data = request.get_json()
    cliente = Cliente(data['nome'], data['endereco'])
    clientes.append(cliente)
    return jsonify({"message": "Cliente cadastrado com sucesso!"}), 201

@app.route('/fornecedores', methods=['GET'])
def listar_fornecores():
    response = []
    for fornecedor in fornecedores:
            response.append({
                "nome": fornecedor.nome
            })
    return jsonify(response)

# Rota para listar produtos com informações adicionais
@app.route('/produtos', methods=['GET'])
def listar_produtos():
    response = []
    for fornecedor in fornecedores:
        for cliente in clientes:
            response.append({
                "produto": fornecedor.produto,
                "quantidade": fornecedor.quantidade,
                "valor": fornecedor.valor
            })
    return jsonify(response)

# Nova rota para listar apenas os clientes
@app.route('/clientes', methods=['GET'])
def listar_clientes():
    response = []
    for cliente in clientes:
        response.append({
            "nome": cliente.nome,
            "endereco": cliente.endereco
        })
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
