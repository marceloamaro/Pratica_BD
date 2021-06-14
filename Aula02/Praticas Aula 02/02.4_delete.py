import sqlite3
from contextlib import closing

with sqlite3.connect('Pais.db') as conexao:
    conexao.row_factory = sqlite3.Row

    print(f"{'id':3s} {'Estado':20s} {'População':12s}")
    print("=" * 37)

    for estado in conexao.execute("select * from  estados order by id"):
        print(f"{estado['id']:3d} {estado['nome']:20s} {estado['populacao']:12d}")

busca = input("Digite um nome de um Estado para buscar: ")
with sqlite3.connect("Pais.db") as conexao:
    with closing(conexao.cursor()) as cursor:
       
        cursor.execute(""" delete from estados
                            where nome = ? """,(busca, ))
        print("Registros Deletados: ", cursor.rowcount)
        if cursor.rowcount == 1:
            conexao.commit()
            print("Alteração realizada")
        else:
            conexao.rollback()
            print("Abortar operação")
with sqlite3.connect('Pais.db') as conexao:
    conexao.row_factory = sqlite3.Row

    print(f"{'id':3s} {'Estado':20s} {'População':12s}")
    print("=" * 37)

    for estado in conexao.execute("select * from  estados order by id"):
        print(f"{estado['id']:3d} {estado['nome']:20s} {estado['populacao']:12d}")