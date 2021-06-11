
# criação do banco de dados
import sqlite3  # informa o banco dedados a ser utilizado através do import
conexao = sqlite3.connect("agenda.db")  # Criação do banco de dados
# Criação do cursor (Objetos utilizados para enviar comados e receber resultados do banco de dados)
cursor = conexao.cursor()

# Envia o comando seguinte ao banco de dados(Cria a Tabela)
cursor.execute(
    '''
create table agenda
(
    nome text,
    telefone text
)
''')

# Envia o comando que insere dados no banco de dados
cursor.execute(
    '''
insert into agenda(nome, telefone) values(?, ?)
''', ("Evaldo", "123-456")
)

conexao.commit()  # Operação necessaŕia para modificar o Banco de Dados
cursor.close()   # Fechando o cursor
conexao.close()  # Fechando a conexão
