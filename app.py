from flask import Flask
from database import Database
from rotas import Rotas

app = Flask(__name__)
app.secret_key = 'secreto'

# Cria o banco e as rotas
db = Database()
Rotas(app, db)

if __name__ == '__main__':
    app.run(debug=True)

    






