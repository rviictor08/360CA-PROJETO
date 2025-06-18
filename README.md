# Trabalho de Programação Orientada a Objetos

CA360

## Descrição

Este trabalho tem como objetivo aplicar os conceitos de Programação Orientada a Objetos (POO) na construção de um sistema. O sistema foi desenvolvido utilizando os princípios de abstração, encapsulamento, herança e polimorfismo, visando proporcionar uma solução eficiente e bem estruturada para o problema proposto.

## Integrantes

- **Otávio**
- **Felipe**
- **Daniel**
- **Raul**

## Tecnologias Utilizadas

- FrontEnd: HTML, CSS.
- BackEnd: Python e MySQL
- IDE: VS Code
- Protótipo: Figma

## Estrutura do Projeto

- **`modelos/`**: Contém as classes Python orientadas a objetos que interagem com o banco de dados (ProdutoCliente, ProdutoFornecedor, Fornecedor).
- **`static/`**: Armazena arquivos estáticos como CSS, JavaScript e imagens.
  - `static/css/`: Folhas de estilo CSS.
  - `static/images/`: Imagens usadas no projeto ou no `README`.
- **`templates/`**: Contém os arquivos HTML das páginas da aplicação.
- **`app.py`**: O arquivo principal da aplicação Flask, onde a aplicação é inicializada.
- **`database.py`**: Lógica para conexão com o banco de dados PostgreSQL.
- **`rotas.py`**: Define as rotas (URLs) e a lógica de negócio para cada página da aplicação.
- **`requirements.txt`**: Lista das dependências Python do projeto.
- **`README.md`**: Este arquivo.

## Layout

Link Layout Figma: [https://www.figma.com/design/MPho6u5aRL9yVwQBoqN5DI/ca_360_01?node-id=1-890&t=7PpQqpTFcA1sOXM8-1](https://www.figma.com/design/MPho6u5aRL9yVwQBoqN5DI/ca_360_01?node-id=1-890&t=7PpQqpTFcA1sOXM8-1)

![Página Inicial](https://raw.githubusercontent.com/rviictor08/360CA-PROJETO/main/Layout/inicio.png)
![Página de Login](https://raw.githubusercontent.com/rviictor08/360CA-PROJETO/main/Layout/login.png)
![Página de Acompanhamento](https://raw.githubusercontent.com/rviictor08/360CA-PROJETO/main/Layout/acompanhamento.png)

## Instalação

Para rodar o projeto em sua máquina local, siga as etapas abaixo:

1.  **Clone este repositório:**
    Abra seu terminal ou prompt de comando e execute:

    ```bash
    git clone [https://github.com/rviictor08/360CA-PROJETO](https://github.com/rviictor08/360CA-PROJETO)
    ```

2.  **Navegue até o diretório do projeto:**

    ```bash
    cd 360CA-PROJETO
    ```

3.  **Crie e ative um ambiente virtual (recomendado):**

    ```bash
    python -m venv venv
    # No Windows:
    .\venv\Scripts\activate
    # No macOS/Linux:
    source venv/bin/activate
    ```

4.  **Instale as dependências:**

    ```bash
    pip install -r requirements.txt
    ```

5.  **Configure o Banco de Dados PostgreSQL:**
    Certifique-se de ter um servidor PostgreSQL rodando. Você precisará criar as tabelas necessárias. Abaixo estão os comandos SQL básicos para as tabelas mencionadas no projeto:

    ```sql
    -- Tabela fornecedores
    CREATE TABLE fornecedores (
        id SERIAL PRIMARY KEY,
        email VARCHAR(100),
        senha VARCHAR(100)
    );

    -- Tabela produto_clientes
    CREATE TABLE produto_clientes (
        id SERIAL PRIMARY KEY,
        nome VARCHAR(255),
        produto VARCHAR(255),
        quantidade INTEGER,
        origem VARCHAR(255),
        destino VARCHAR(255),
        status VARCHAR(255),
        data_pedido TIMESTAMP WITHOUT TIME ZONE
    );

    -- Tabela produtos_fornecedores
    CREATE TABLE produtos_fornecedores (
        id SERIAL PRIMARY KEY,
        nome_fornecedor VARCHAR(255),
        produto_fornecedor VARCHAR(255),
        quantidade INTEGER,
        endereco VARCHAR(255),
        valor_por_item NUMERIC(10, 2),
        quantidade_por_valor NUMERIC(10, 2)
    );
    ```

    **Importante:** Atualize a string de conexão no seu arquivo `database.py` (ou onde quer que a conexão seja configurada) com as credenciais do seu banco de dados PostgreSQL.

6.  **Execute a Aplicação:**
    ```bash
    flask run
    ```
    A aplicação geralmente estará disponível em `http://127.0.0.1:5000/` no seu navegador.
