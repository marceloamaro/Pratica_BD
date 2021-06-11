import sqlite3

conexao = sqlite3.connect("ctmombaça.db")

cursor = conexao.cursor()

# Envia o comando seguinte ao banco de dados(Cria a Tabela)

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


conexao.commit()
cursor.close()
conexao.close()  