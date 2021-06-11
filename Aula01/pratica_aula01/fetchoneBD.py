import sqlite3
conexao = sqlite3.connect("ctmombaça.db")

cursor = conexao.cursor()

# comando para fazer a busca na tabela
cursor.execute("select * from ctmombaça")

# fetchone retorna uma tupla com os resultados da consulta
resultado = cursor.fetchone()

# fstring que captura os dados da tupla através da indexação
print(f"Nome: {resultado[0]}\nModalidade: {resultado[1]}")


cursor.close()
conexao.close()