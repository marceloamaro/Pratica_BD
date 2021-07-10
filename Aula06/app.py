import sqlite3
import data
from PyQt5 import uic, QtWidgets



# Adiciona
def adicionar():
    conexao = data.conect()
    #data.create(conexao)

    nome = tela.lineEdit_linguagem.text()
    criador = tela.lineEdit_Criador.text()
    ano = tela.lineEdit_ano.text()

    data.add_linguagens(conexao, nome, criador, ano)

    # limpando o lineEdit
    tela.lineEdit_linguagem.setText("")
    tela.lineEdit_Criador.setText("")
    tela.lineEdit_ano.setText("")

# Mostrar itens
def mostrar():
    tela_dados.show()
    banco = sqlite3.connect("linguagens.db")
    cursor = banco.cursor()
    cursor.execute("select * from linguagens")
    lidos = cursor.fetchall()

    # Jogando os itens na tabela
    tela_dados.tableWidget.setRowCount(len(lidos))
    tela_dados.tableWidget.setColumnCount(3)

    for i in range(0, len(lidos)):
        for j in range(0, 3):
            tela_dados.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(lidos[i][j])))
    banco.close()

#Deleta itens
def deletar():
    banco = sqlite3.connect("linguagens.db")
    cursor = banco.cursor()
    cursor.execute("delete from linguagens where id % 2 != 0")
    banco.commit()
    banco.close()


app = QtWidgets.QApplication([])
tela = uic.loadUi("linguagens.ui")
tela_dados = uic.loadUi("dados.ui")

# eventos dos botões
tela.pushButton.clicked.connect(adicionar)
tela.pushButton_busca.clicked.connect(mostrar)
tela.pushButton_del.clicked.connect(deletar)


tela.show()
app.exec()