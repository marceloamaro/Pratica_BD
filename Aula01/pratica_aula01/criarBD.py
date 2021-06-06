import sqlite3
conexao = sqlite3.connect("ctmombaça.db")

cursor = conexao.cursor()

conexao.close()