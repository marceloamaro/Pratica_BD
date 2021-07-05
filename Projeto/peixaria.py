from PyQt5 import  uic,QtWidgets
import sqlite3

def chama_segunda():
    primeira.label_4.setText("")
    nome_usuario = primeira.lineEdit.text()
    senha = primeira.lineEdit_2.text()
    if nome_usuario == "marcelo123" and senha == "123456" :
        primeira.close()
        segunda.show()
    else :
        primeira.label_4.setText("Dados de login incorretos!")
    

def logout():
    segunda.close()
    primeira.show()

def funcao_principal():
    codigo = segunda.lineEdit.text()
    descricao = segunda.lineEdit_2.text()
    preco = segunda.lineEdit_3.text()
    categoria = segunda.lineEdit_4.text()
    

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
primeira=uic.loadUi("primeira.ui")
segunda = uic.loadUi("segunda.ui")
primeira.pushButton.clicked.connect(chama_segunda)
segunda.pushButton.clicked.connect(logout)
primeira.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password) 


primeira.show()
app.exec()