import sqlite3
from contextlib import closing


with sqlite3.connect("agenda2.db") as conexao:
    with closing(conexao.cursor()) as cursor:
       
        cursor.execute(""" delete from agenda2
                            where nome = 'Jonas' """)
        print("Registros Deletados: ", cursor.rowcount)
        if cursor.rowcount == 2:
            conexao.commit()
            print("Alteração realizada")
        else:
            conexao.rollback()
            print("Abortar operação")