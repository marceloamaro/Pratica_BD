"""
# Inserindo vários dados através do Executemany
import sqlite3

dados = [
    ("João", "111-111"),
    ("André", "222-222"),
    ("Maria", "333-333")
]

conexao = sqlite3.connect("agenda.db")

cursor = conexao.cursor()

cursor.executemany(
    '''
    insert into agenda (nome, telefone)
    values(?, ?)
''', dados)

conexao.commit()
cursor.close()
conexao.close()
"""