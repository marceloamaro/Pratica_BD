import sqlite3
dados = [
    ("Marcelo", "Muay-thai", "Azul-escura", "SM"),
    ("Cicero", "Muay-thai", "Azul-escura", "SM"),
    ("Cicero", "Jiu-Jitsu", "Branca-3grau", "SM"),
    ("Robson", "Muay-thai", "Branca", "R$50")
]
conexao = sqlite3.connect("ctmombaça.db")

cursor = conexao.cursor()

# Envia o comando seguinte ao banco de dados(Cria a Tabela)

# Inserindo vários dados através do Executemany
cursor.executemany(
    '''
    insert into ctmombaça (nome, modalidade, graduacao, mensalidade)
    values(?, ?, ?, ?)
''', dados)

conexao.commit()
cursor.close()
conexao.close()  