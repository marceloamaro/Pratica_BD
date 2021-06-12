import sqlite3
from contextlib import closing

busca = input("Digite um nome para buscar: ")
with sqlite3.connect("agenda2.db") as conexao:
    with closing(conexao.cursor()) as cursor:
        cursor.execute("select * from agenda2 where nome = ?", (busca,))
        while True:
            resultado = cursor.fetchone()
            if resultado is None:
                break
            print(f"Nome: {resultado[0]}\nTelefone: {resultado[1]}")