import sqlite3
conexao = sqlite3.connect("ctmombaça.db")

cursor = conexao.cursor()

# comando para fazer a busca na tabela
cursor.execute("select * from ctmombaça")

# fetchone retorna uma tupla com os resultados da consulta
resultado = cursor.fetchall()

# Loop que captura os dados da tupla através da indexação
for registro in resultado:
    print(f"Nome: {registro[0]}\nModalidade: {registro[1]}")


cursor.close()
conexao.close()