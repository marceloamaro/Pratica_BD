from sqlite3.dbapi2 import Cursor
from PyQt5 import  uic,QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt
import sqlite3
from reportlab.pdfgen import canvas
    
def chama_segunda():
    primeira.label_4.setText("")
    nome_usuario = primeira.lineEdit.text()
    senha = primeira.lineEdit_2.text()
    banco = sqlite3.connect('banco_cadastro.db') 
    cursor = banco.cursor()
    
    try:
        cursor.execute("select senha from cadastro where login ='{}'".format(nome_usuario) )
        senha_bd = cursor.fetchall()
        banco.close() 
    except:
        print("ERRO ao validar o login") 
 
    if senha == senha_bd[0][0]:
        primeira.close()
        segunda.show()
    else :
        primeira.label_4.setText("Dados de login incorretos!")
    
def volta_tela():
    segunda.show()
    quarta.close()
    terceira.close()
    primeira.close()
    sete.close()
    sete.close()
    tela_cadastro.close()

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
    cursor.execute("CREATE TABLE IF NOT EXISTS produtos (codigo integer primary key, descricao text, preco text, categoria text)")
    cursor.execute("INSERT INTO produtos VALUES ('"+codigo+"','"+descricao+"','"+preco+"','"+categoria+"')")

    banco.commit() 
    terceira.lineEdit.setText("")
    terceira.lineEdit_2.setText("")
    terceira.lineEdit_3.setText("")
    terceira.lineEdit_4.setText("")
    banco.close()

def apagar():

    banco = sqlite3.connect('estoque.db')  
    linha = sete.tableWidget.currentRow()
    sete.tableWidget.removeRow(linha)

    cursor = banco.cursor()
    cursor.execute("SELECT codigo FROM produtos")
    dados_lidos = cursor.fetchall()
    valor_id = dados_lidos[linha][0]
    cursor.execute("DELETE FROM produtos WHERE codigo="+ str(valor_id))
    banco.commit()
    banco.close()

def busca_completa(): 
    sete.show()
    quarta.close()
    banco = sqlite3.connect('estoque.db') 
    cursor = banco.cursor()
    cursor.execute("select * from produtos")
    resultados = cursor.fetchall()
    sete.tableWidget.setRowCount(len(resultados))
    sete.tableWidget.setColumnCount(4)

    for i in range(0, len(resultados)):
        for j in range(0, 4):
            sete.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(resultados[i][j])))
    banco.close()   
    
def abre_tela_cadastro():
    segunda.close()
    tela_cadastro.show()

def cadastrar():
    nome = tela_cadastro.lineEdit.text()
    login = tela_cadastro.lineEdit_2.text()
    senha = tela_cadastro.lineEdit_3.text()
    c_senha = tela_cadastro.lineEdit_4.text()

    if (senha == c_senha):
        try:
            banco = sqlite3.connect('banco_cadastro.db') 
            cursor = banco.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS cadastro (nome text,login text,senha text)")
            cursor.execute("INSERT INTO cadastro VALUES ('"+nome+"','"+login+"','"+senha+"')")

            banco.commit() 
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

def gerar_pdf():
    banco = sqlite3.connect('estoque.db')
    cursor = banco.cursor()
    cursor.execute("select * from produtos")
    dados_lidos = cursor.fetchall()
    y = 0
    pdf = canvas.Canvas("cadastro_produtos.pdf")
    pdf.setFont("Times-Bold", 25)
    pdf.drawString(250,800, "Produtos cadastrados:")
    pdf.setFont("Times-Bold", 18)

    pdf.drawString(110,750, "CODIGO")
    pdf.drawString(210,750, "DESCRIÇÃO")
    pdf.drawString(350,750, "PREÇO")
    pdf.drawString(450,750, "CATEGORIA")

    for i in range(0, len(dados_lidos)):
        y = y + 50
        
        pdf.drawString(150,750 - y, str(dados_lidos[i][0]))
        pdf.drawString(250,750 - y, str(dados_lidos[i][1]))
        pdf.drawString(350,750 - y, str(dados_lidos[i][2]))
        pdf.drawString(450,750 - y, str(dados_lidos[i][3]))

    pdf.save()
    print("PDF FOI GERADO COM SUCESSO!")


app=QtWidgets.QApplication([])
primeira=uic.loadUi("primeira.ui")
segunda = uic.loadUi("segunda.ui")
terceira = uic.loadUi("terceira.ui")
quarta = uic.loadUi("quarta.ui")
sete = uic.loadUi("sete_quarta.ui")
tela_cadastro = uic.loadUi("tela_cadastro.ui")
primeira.pushButton.clicked.connect(chama_segunda)
primeira.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
segunda.pushButton_3.clicked.connect(abre_tela_terceira)
terceira.pushButton.clicked.connect(chama_terceira)  
segunda.pushButton_5.clicked.connect(abre_tela_cadastro)
tela_cadastro.pushButton.clicked.connect(cadastrar) 
quarta.pushButton_6.clicked.connect(volta_tela)
segunda.pushButton.clicked.connect(abre_tela_quarta)
terceira.pushButton_2.clicked.connect(volta_tela)
quarta.pushButton_7.clicked.connect(busca_completa)
sete.pushButton_6.clicked.connect(volta_tela)
tela_cadastro.pushButton_2.clicked.connect(volta_tela)
sete.pushButton_4.clicked.connect(apagar)
sete.pushButton.clicked.connect(gerar_pdf)




primeira.show()
app.exec()