import sqlite3
conexao = sqlite3.connect("garagem.db")

cursor = conexao.cursor()


cursor.execute("DELETE FROM carros WHERE placa = 'ABC-1234'")
"""
cursor.execute( 
    '''  
create table carros
(
    placa VARCHAR(10) NOT NULL,
    nome_dono VARCHAR(20) NOT NULL
)
''')
"""
"""
cursor.execute("UPDATE carros SET nome_dono = 'Joaquim' WHERE placa = 'ABC-1234'")
"""
"""
cursor.execute(
    "INSERT INTO carros (placa, nome_dono) VALUES ('ABC-1234', 'Joao')")
"""
conexao.commit()
cursor.close()
conexao.close()  