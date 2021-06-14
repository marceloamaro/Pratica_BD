import sqlite3
from contextlib import closing
busca = input("Digite um nome de um Estado para buscar: ")
with sqlite3.connect("agenda2.db") as conexao:
    with closing(conexao.cursor()) as cursor:
        
        cursor.execute(
             """
                 update agenda2
                 set telefone = '000-000'
                 where nome = 'Jonas'
             """)
        
conexao.commit()