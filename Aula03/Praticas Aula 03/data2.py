import sqlite3


CREATE_TABLE = "create table linguagens(id integer primary key, nome text, criador text, ano integer)"

INSERT_LINGUAGENS = "insert into linguagens (nome, criador, ano) values (?, ?, ?);"

BUSCA_LINGUAGENS = "select * from linguagens;"

BUSCA_LINGUAGENS_POR_NOME = "select * from linguagens where nome = ?;"

BUSCA_LINGUAGEM_MAIS_ANTIGA = """
select * from linguagens
order by ano asc
limit 1;
""" 
BUSCA_LINGUAGEM_MAIS_RECENTE = """
select * from linguagens
order by ano desc
limit 1;
"""

def connect():
    return sqlite3.connect("linguagens.db")

def create(conexao):
    with conexao:
        conexao.execute(CREATE_TABLE)

def insert(conexao, nome, criador, ano):
    with conexao:
        conexao.execute(INSERT_LINGUAGENS,( nome, criador, ano))
    

def busca(conexao):
    with conexao:
        return conexao.execute(BUSCA_LINGUAGENS).fetchall()

def busca_nome(conexao, nome):
    with conexao:
        return conexao.execute(BUSCA_LINGUAGENS_POR_NOME, (nome,)).fetchall()

def busca_antiga(conexao):
    with conexao:
        return conexao.execute(BUSCA_LINGUAGEM_MAIS_ANTIGA).fetchone() 

def busca_recente(conexao):
    with conexao:
        return conexao.execute(BUSCA_LINGUAGEM_MAIS_RECENTE).fetchone()