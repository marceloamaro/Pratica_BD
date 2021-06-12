import sqlite3

from contextlib import closing

dados = [
    ["São Paulo", 43663672], ["Minas Gerais", 21292666], ["Rio de Janeiro", 17366189],["Bahia", 14930634],
    ["Paraná", 11516840], ["Rio Grande do Sul", 11422973], ["Pernambuco", 9616621], ["Ceará", 9187103],
    ["Pará", 8690745], ["Santa Catarina", 7252502], ["Maranhão", 7114598], ["Goiáis", 7113540],
    ["Amazonas", 4207714], ["Espirito Santo", 4064052], ["Paraíba", 4039277], 
    ["Rio Grande do Norte", 3534165], ["Mato Grosso", 3526220], ["Alagoas", 3351543], 
    ["Piauí", 3281480], ["Distrito Federal", 3055149], ["Mato Grosso do Sul", 2809394],
    ["Sergipe", 2318822], ["Rondônia", 1796460], ["Tocantins", 1590248], ["Acre", 894470],
    ["Amapá", 861773], ["Roraima", 631181]
] 
busca = input("Digite um nome de um Estado para buscar: ")
with sqlite3.connect('Pais.db') as conexao:
    with closing(conexao.cursor()) as cursor:
        cursor.execute("select * from estados where nome = ?", (busca,))
        while True:
            resultado = cursor.fetchone()
            if resultado is None:
                break
            print(f"Nome: {resultado[1]}\nid: {resultado[0]}\npopulação: {resultado[2]}")