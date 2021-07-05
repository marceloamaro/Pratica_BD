from PyQt5 import  uic,QtWidgets
import sqlite3



def funcao_principal():
    codigo = peixaria.lineEdit.text()
    descricao = peixaria.lineEdit_2.text()
    preco = peixaria.lineEdit_3.text()
    categoria = peixaria.lineEdit_4.text()
    

    print("Código:",codigo)
    print("Descricao:",descricao)
    print("Preco",preco)
    print("Categoria selecionada",categoria)
    
    banco = sqlite3.connect('estoque.db') 
    cursor = banco.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS produtos (codigo integer, descricao text, preco text, categoria text)")
    cursor.execute("INSERT INTO produtos VALUES ('"+codigo+"','"+descricao+"','"+preco+"','"+categoria+"')")

    banco.commit() 
    banco.close()

    
app=QtWidgets.QApplication([])
peixaria=uic.loadUi("peixaria.ui")
peixaria.pushButton.clicked.connect(funcao_principal)

peixaria.show()
app.exec()