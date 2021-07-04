import sqlite3


CREATE_TABLE = "create table agenda(id integer primary key, nome text, telefone text)"

INSERT_DADOS = "insert into agenda (nome, telefone) values (?, ?);"

BUSCA_DADOS = "select * from agenda;"

BUSCA_DADOS_POR_NOME = "select * from agenda where nome = ?;"

BUSCA_LINGUAGEM_MAIS_ANTIGA = """
select * from agenda
order by id asc
limit 1;
""" 
BUSCA_LINGUAGEM_MAIS_RECENTE = """
select * from agenda
order by id desc
limit 1;
"""

def connect():
    return sqlite3.connect("agenda.db")

def create(conexao):
    with conexao:
        conexao.execute(CREATE_TABLE)

def insert(conexao, nome, telefone):
    with conexao:
        conexao.execute(INSERT_DADOS,( nome, telefone))
    

def busca(conexao):
    with conexao:
        return conexao.execute(BUSCA_DADOS).fetchall()

def busca_nome(conexao, nome):
    with conexao:
        return conexao.execute(BUSCA_DADOS_POR_NOME, (nome,)).fetchall()

def busca_antiga(conexao):
    with conexao:
        return conexao.execute(BUSCA_LINGUAGEM_MAIS_ANTIGA).fetchone() 

def busca_recente(conexao):
    with conexao:
        return conexao.execute(BUSCA_LINGUAGEM_MAIS_RECENTE).fetchone()