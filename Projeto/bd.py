import sqlite3  
conexao = sqlite3.connect("estoque.db")  

cursor = conexao.cursor()


cursor.execute(
    '''
create table produtos
(
    id primary key,
    codigo integer,
    descricao text,
    preco text,
    categoria text
    
)
''')

conexao.commit() 
cursor.close()   
conexao.close()  