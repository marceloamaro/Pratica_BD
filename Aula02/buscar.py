import sqlite3
from contextlib import closing

dados = [
    ("João","111-111"),
    ("Edinara","222-222"),
    ("Jonas","333-333"),
    ("Raquel","444-444")
]

with sqlite3.connect("agenda2.db") as conexao:
    with closing(conexao.cursor()) as cursor:
cursor.execute("select * from agenda2 where nome = 'Abacate' ")
        while True:
            resultado = cursor.fetchone()
            if resultado is None:
                break
            print(f"Nome: {resultado[0]}\nTelefone: {resultado[1]}")