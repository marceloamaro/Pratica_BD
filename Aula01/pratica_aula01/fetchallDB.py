import sqlite3
conexao = sqlite3.connect("ctmombaça.db")

cursor = conexao.cursor()


cursor.execute("select * from ctmombaça")


resultado = cursor.fetchall()


for registro in resultado:
    print(f"Nome: {registro[0]}\nModalidade: {registro[1]}")


cursor.close()
conexao.close()