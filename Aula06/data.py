import sqlite3

CREATE_TABLE = "create table linguagens(nome text, criador text, ano integer)"

INSERT_LINGUAGENS = "insert into linguagens(nome, criador ,ano) values(?, ? ,?);"

BUSCA_LINGUAGENS = "select * from linguagens;"

BUSCA_LINGUAGENS_POR_NOME = "select * from linguagens where nome = ?;"

BUSCA_LINGUAGENS_ANTIGA = """
select * from linguagens
order by ano asc
limit 1
"""

# função que cria o banco
def conect():
    return sqlite3.connect("linguagens.db")

# função que cria a tabela
def create(conexao):
    with conexao:
        conexao.execute(CREATE_TABLE)

# função para inserir dados
def add_linguagens(conexao, nome, criador, ano):
    with conexao:
        conexao.execute(INSERT_LINGUAGENS, (nome, criador, ano))

# função para busca simples
def busca(conexao):
    with conexao:
        return conexao.execute(BUSCA_LINGUAGENS).fetchall()

# função para busca por nome
def busca_nome(conexao, nome):
    with conexao:
        return conexao.execute(BUSCA_LINGUAGENS_POR_NOME, (nome,)).fetchall()
# função para buscar a linguagem mais antiga
def busca_antiga(conexao):
    with conexao:
        return conexao.execute(BUSCA_LINGUAGENS_ANTIGA).fetchone()
