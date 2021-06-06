import sqlite3
conexao = sqlite3.connect("ctmombaça.db")

cursor = conexao.cursor()


cursor.execute("select * from ctmombaça")


resultado = cursor.fetchone()

print(f"Nome: {resultado[0]}\nModalidade: {resultado[1]}")


cursor.close()
conexao.close()