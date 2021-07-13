from sqlite3.dbapi2 import Cursor
from PyQt5 import  uic,QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt
import sqlite3
from reportlab.pdfgen import canvas
conexao = sqlite3.connect("bdpeixaria.db")  

cursor = conexao.cursor()

def cadastrar():
    codigo = tela_cadastro.lineEdit_5.text()
    nome = tela_cadastro.lineEdit.text()
    login = tela_cadastro.lineEdit_2.text()
    senha = tela_cadastro.lineEdit_3.text()
    c_senha = tela_cadastro.lineEdit_4.text()

    if (senha == c_senha):
        try:
            banco = sqlite3.connect('bdpeixaria.db') 
            cursor = banco.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS cadastro (codigo integer primary key,nome text,login text,senha text)")
            cursor.execute("INSERT INTO cadastro VALUES ('"+codigo+"','"+nome+"','"+login+"','"+senha+"')")

            banco.commit() 
            tela_cadastro.lineEdit_5.setText("")
            tela_cadastro.lineEdit.setText("")
            tela_cadastro.lineEdit_2.setText("")
            tela_cadastro.lineEdit_3.setText("")
            tela_cadastro.lineEdit_4.setText("")
            banco.close()
            tela_cadastro.label.setText("Usuario cadastrado com sucesso")

        except sqlite3.Error as erro:
            print("Erro ao inserir os dados: ",erro)
    else:
        tela_cadastro.label.setText("As senhas digitadas estão diferentes")



  

app=QtWidgets.QApplication([])
tela_cadastro = uic.loadUi("tela_cadastro.ui")
tela_cadastro.pushButton.clicked.connect(cadastrar)

tela_cadastro.show()
app.exec()
