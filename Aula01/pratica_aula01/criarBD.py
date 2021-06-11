# criação do banco de dados
# informa o banco dedados a ser utilizado através do import

import sqlite3 

# Criação do banco de dados
conexao = sqlite3.connect("ctmombaça.db")

# Criação do cursor (Objetos utilizados para enviar comados e receber resultados do banco de dados)
cursor = conexao.cursor()

cursor.close()   # Fechando o cursor
conexao.close()  # Fechando a conexão