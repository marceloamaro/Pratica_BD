from sqlite3.dbapi2 import Cursor
from PyQt5 import  uic,QtWidgets
import sqlite3


def sair():
    primeira.close()
    segunda.close()
    terceira.close()
    quarta.close()
    

def chama_segunda():
    primeira.label_4.setText("")
    nome_usuario = primeira.lineEdit.text()
    senha = primeira.lineEdit_2.text()
    if nome_usuario == "marcelo123" and senha == "123456" :
        primeira.close()
        segunda.show()
    else :
        primeira.label_4.setText("Dados de login incorretos!")
    

def volta_terceira():
    segunda.show()
    terceira.close()

def volta_quarta():
    segunda.show()
    quarta.close()
    terceira.close()
    primeira.close()
def abre_tela_terceira():
    segunda.close()
    terceira.show()

def abre_tela_quarta():
    segunda.close()
    quarta.show()    
       

def chama_terceira():
    codigo = terceira.lineEdit.text()
    descricao = terceira.lineEdit_2.text()
    preco = terceira.lineEdit_3.text()
    categoria = terceira.lineEdit_4.text()
    

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

def chama_quarta():
    banco = sqlite3.connect('estoque.db') 
    cursor = banco.cursor()
    cursor.execute ("select * from produtos")

    resultado = cursor.fetchone()

    quarta.label_4.setText("codigo: {resultado[0]}\ndescricao: {resultado[1]}")
    
    banco.close()

    

app=QtWidgets.QApplication([])
primeira=uic.loadUi("primeira.ui")
segunda = uic.loadUi("segunda.ui")
terceira = uic.loadUi("terceira.ui")
quarta = uic.loadUi("quarta.ui")
primeira.pushButton.clicked.connect(chama_segunda)
primeira.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
segunda.pushButton_3.clicked.connect(abre_tela_terceira)
terceira.pushButton.clicked.connect(chama_terceira)  
segunda.pushButton_5.clicked.connect(sair)
quarta.pushButton_5.clicked.connect(sair)
quarta.pushButton_6.clicked.connect(volta_quarta)
segunda.pushButton.clicked.connect(abre_tela_quarta)
terceira.pushButton_2.clicked.connect(volta_terceira)



primeira.show()
app.exec()