import sqlite3
dados = [
    ("Marcelo", "Muay-thai", "Azul-escura", "SM"),
    ("Cicero", "Muay-thai", "Azul-escura", "SM"),
    ("Cicero", "Jiu-Jitsu", "Branca-3grau", "SM"),
    ("Robson", "Muay-thai", "Branca", "R$50")
]
conexao = sqlite3.connect("ctmombaça.db")

cursor = conexao.cursor()
"""
cursor.execute( 
    '''  
create table ctmombaça
(
    nome text,
    modalidade text,
    graduacao text,
    mensalidade text
)
''')
"""
cursor.executemany(
    '''
    insert into ctmombaça (nome, modalidade, graduacao, mensalidade)
    values(?, ?, ?, ?)
''', dados)

conexao.commit()
cursor.close()
conexao.close()  