from sqlite3.dbapi2 import Cursor
from PyQt5 import  uic,QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt
import sqlite3


def sair():
    primeira.close()
    segunda.close()
    terceira.close()
    quarta.close()
    quinta.close()
    sexta.close()
    
def chama_segunda():
    primeira.label_4.setText("")
    nome_usuario = primeira.lineEdit.text()
    senha = primeira.lineEdit_2.text()
    if nome_usuario == "marcelo123" and senha == "123456" :
        primeira.close()
        segunda.show()
    else :
        primeira.label_4.setText("Dados de login incorretos!")
    
def volta_tela():
    segunda.show()
    quarta.close()
    terceira.close()
    primeira.close()
    quinta.close()
    sexta.close()

def abre_tela_terceira():
    segunda.close()
    terceira.show()

def abre_tela_quarta():
    segunda.close()
    quarta.show()    
       
def abre_tela_quinta():
    segunda.close()
    quinta.show()

def abre_tela_sexta():
    segunda.close()
    sexta.show()    

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
    cursor.execute("CREATE TABLE IF NOT EXISTS produtos (codigo integer primary key, descricao text, preco text, categoria text)")
    cursor.execute("INSERT INTO produtos VALUES ('"+codigo+"','"+descricao+"','"+preco+"','"+categoria+"')")

    banco.commit() 
    terceira.lineEdit.setText("")
    terceira.lineEdit_2.setText("")
    terceira.lineEdit_3.setText("")
    terceira.lineEdit_4.setText("")
    banco.close()

def apagar():
    busca2 = quinta.lineEdit_2.text()
    banco = sqlite3.connect('estoque.db') 
    cursor = banco.cursor()
    
    resultado = cursor.fetchone()
    cursor.execute("delete from produtos where descricao = ?", (busca2,))
    print("Registros Deletados: ")
    
    banco.commit()
    quinta.lineEdit_2.setText("")
    banco.close()


def busca_simples():
    busca1 = quinta.lineEdit_2.text()
    banco = sqlite3.connect('estoque.db') 
    cursor = banco.cursor()
    cursor.execute("select * from produtos where descricao = ?", (busca1,))
    while True:
        resultado = cursor.fetchone()
        if resultado is None:
            break
        print(f"Codigo: {resultado[0]}\ndescriçao: {resultado[1],}\npreço: {resultado[2]}\ncategoria: {resultado[3]}")
    
    quinta.lineEdit_2.setText("")
    banco.close()

def busca_completa():
    banco = sqlite3.connect('estoque.db') 
    cursor = banco.cursor()
    cursor.execute("select *from produtos")
    
    resultados = cursor.fetchall()
    print("Total de arquivos:  ", len(resultados))
    for row in resultados:
            print("Codigo: ", row[0])
            print("Descrição: ", row[1])
            print("Preço: ", row[2])
            print("Catergoria: ", row[3])
            print("\n")

    banco.close()    



app=QtWidgets.QApplication([])
primeira=uic.loadUi("primeira.ui")
segunda = uic.loadUi("segunda.ui")
terceira = uic.loadUi("terceira.ui")
quarta = uic.loadUi("quarta.ui")
quinta = uic.loadUi("quinta.ui")
sexta = uic.loadUi("sexta.ui")
sete = uic.loadUi("sete_quarta.ui")
oito = uic.loadUi("oito_quinta.ui")
primeira.pushButton.clicked.connect(chama_segunda)
primeira.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
segunda.pushButton_3.clicked.connect(abre_tela_terceira)
terceira.pushButton.clicked.connect(chama_terceira)  
segunda.pushButton_5.clicked.connect(sair)
quarta.pushButton_5.clicked.connect(sair)
quarta.pushButton_6.clicked.connect(volta_tela)
segunda.pushButton.clicked.connect(abre_tela_quarta)
terceira.pushButton_2.clicked.connect(volta_tela)
quinta.pushButton_5.clicked.connect(sair)
quinta.pushButton_6.clicked.connect(volta_tela)
segunda.pushButton_2.clicked.connect(abre_tela_quinta)
sexta.pushButton_5.clicked.connect(sair)
sexta.pushButton_6.clicked.connect(volta_tela)
segunda.pushButton_4.clicked.connect(abre_tela_sexta)
quinta.pushButton_7.clicked.connect(busca_simples)
sexta.pushButton_8.clicked.connect(apagar)
quarta.pushButton_7.clicked.connect(busca_completa)



primeira.show()
app.exec()
