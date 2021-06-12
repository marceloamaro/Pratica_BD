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
      
         cursor.executemany(
             """
             insert into agenda2(nome, telefone) values(?,?)
             """,(dados)
         )
conexao.commit()