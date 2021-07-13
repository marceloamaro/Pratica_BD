from sqlite3.dbapi2 import Cursor
from PyQt5 import  uic,QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt
import sqlite3
from reportlab.pdfgen import canvas

numero_id = 0


def editar_dados():
    global numero_id
    banco = sqlite3.connect('bdpeixaria.db') 
    linha = sete.tableWidget.currentRow()
    
    cursor = banco.cursor()
    cursor.execute("SELECT codigo FROM produtos")
    dados_lidos = cursor.fetchall()
    valor_id = dados_lidos[linha][0]
    cursor.execute("SELECT * FROM produtos WHERE codigo="+ str(valor_id))
    produto = cursor.fetchall()
    tela_editar.show()

    
    tela_editar.lineEdit_2.setText(str(produto[0][0]))
    tela_editar.lineEdit_3.setText(str(produto[0][1]))
    tela_editar.lineEdit_4.setText(str(produto[0][2]))
    tela_editar.lineEdit_5.setText(str(produto[0][3]))
    tela_editar.lineEdit_6.setText(str(produto[0][4]))
    numero_id = valor_id

    banco.close()
    
def salvar_valor_editado():
    global numero_id
    banco = sqlite3.connect('bdpeixaria.db') 
    # ler dados do lineEdit
    codigo = tela_editar.lineEdit_2.text()
    descricao = tela_editar.lineEdit_3.text()
    preco = tela_editar.lineEdit_4.text()
    categoria = tela_editar.lineEdit_5.text()
    qestoque = tela_editar.lineEdit_6.text()
    # atualizar os dados no banco
    cursor = banco.cursor()
    cursor.execute("UPDATE produtos SET descricao = '{}', preco = '{}', categoria ='{}', qestoque ='{}' WHERE codigo = {}".format(descricao,preco,categoria,qestoque,codigo))
    banco.commit()
    #atualizar as janelas
    tela_editar.close()
    sete.close()
    busca_completa()

def chama_segunda():
    primeira.label_4.setText("")
    nome_usuario = primeira.lineEdit.text()
    senha = primeira.lineEdit_2.text()
    banco = sqlite3.connect('bdpeixaria.db') 
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
    quinta.close()
    sexta.close()
    sete.close()
    tela_cadastro.close()

def abre_tela_terceira():
    segunda.close()
    terceira.show()

def abre_tela_quarta():
    segunda.close()
    quarta.show()    

def abre_tela_sete():
    segunda.close()
    sexta.show()           

def chama_terceira():
    codigo = terceira.lineEdit.text()
    descricao = terceira.lineEdit_2.text()
    preco = terceira.lineEdit_3.text()
    categoria = terceira.lineEdit_4.text()
    qestoque = terceira.lineEdit_5.text()
    

    print("Código:",codigo)
    print("Descricao:",descricao)
    print("Preco",preco)
    print("Categoria selecionada",categoria)
    print("Estoque selecionada",qestoque)
    
    banco = sqlite3.connect('bdpeixaria.db') 
    cursor = banco.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS produtos (codigo integer primary key, descricao text, preco text, categoria text,qestoque text)")
    cursor.execute("INSERT INTO produtos VALUES ('"+codigo+"','"+descricao+"','"+preco+"','"+categoria+"','"+qestoque+"')")

    banco.commit() 
    terceira.lineEdit.setText("")
    terceira.lineEdit_2.setText("")
    terceira.lineEdit_3.setText("")
    terceira.lineEdit_4.setText("")
    terceira.lineEdit_5.setText("")
    banco.close()

def apagar():

    banco = sqlite3.connect('bdpeixaria.db')  
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
    banco = sqlite3.connect('bdpeixaria.db') 
    cursor = banco.cursor()
    cursor.execute("select * from produtos")
    resultados = cursor.fetchall()
    sete.tableWidget.setRowCount(len(resultados))
    sete.tableWidget.setColumnCount(5)

    for i in range(0, len(resultados)):
        for j in range(0, 5):
            sete.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(resultados[i][j])))
    banco.close()   
    
def abre_tela_cadastro():
    segunda.close()
    tela_cadastro.show()

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

def busca_usuario(): 
    quinta.show()
    sexta.close() 
    banco = sqlite3.connect('bdpeixaria.db') 
    cursor = banco.cursor()
    cursor.execute("select * from cadastro")
    dados = cursor.fetchall()
    quinta.tableWidget.setRowCount(len(dados))
    quinta.tableWidget.setColumnCount(3)

    for i in range(0, len(dados)):
        for j in range(0, 3):
            quinta.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados[i][j])))
    banco.close()

def apagar_usuario():

    banco = sqlite3.connect('bdpeixaria.db')  
    linha = sete.tableWidget.currentRow()
    sete.tableWidget.removeRow(linha)

    cursor = banco.cursor()
    cursor.execute("SELECT codigo FROM cadastro")
    dados_lidos = cursor.fetchall()
    valor_id = dados_lidos[linha][0]
    cursor.execute("DELETE FROM cadastro WHERE codigo="+ str(valor_id))
    banco.commit()
    banco.close()

def editar_dados_usuario():
    global numero_id
    banco = sqlite3.connect('bdpeixaria.db') 
    linha = sete.tableWidget.currentRow()
    
    cursor = banco.cursor()
    cursor.execute("SELECT codigo FROM cadastro")
    dados_lidos = cursor.fetchall()
    valor_id = dados_lidos[linha][0]
    cursor.execute("SELECT * FROM cadastro WHERE codigo="+ str(valor_id))
    produto = cursor.fetchall()
    editar_dados_usuario.show()

    
    editar_dados_usuario.lineEdit_5.setText(str(produto[0][0]))
    editar_dados_usuario.lineEdit_2.setText(str(produto[0][1]))
    editar_dados_usuario.lineEdit_3.setText(str(produto[0][2]))
    editar_dados_usuario.lineEdit_4.setText(str(produto[0][3]))
    numero_id = valor_id

    banco.close()
    
def salvar_valor_usuario():
    global numero_id
    banco = sqlite3.connect('bdpeixaria.db') 
    # ler dados do lineEdit
    codigo = editar_dados_usuario.lineEdit_5.text()
    nome = editar_dados_usuario.lineEdit_2.text()
    login = editar_dados_usuario.lineEdit_3.text()
    senha = editar_dados_usuario.lineEdit_4.text()
    # atualizar os dados no banco
    cursor = banco.cursor()
    cursor.execute("UPDATE cadastro SET nome = '{}', login = '{}', senha = '{}' WHERE codigo = {}".format(nome,login,senha,codigo))
    banco.commit()
    #atualizar as janelas
    editar_dados_usuario.close()
    sete.close()
    busca_usuario()    

def gerar_pdf():
    banco = sqlite3.connect('bdpeixaria.db')
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
quinta = uic.loadUi("quinta_seg.ui")
sexta = uic.loadUi("sete.ui")
editar_usuario = uic.loadUi("menu_editar_usuario.ui")
tela_cadastro = uic.loadUi("tela_cadastro.ui")
tela_editar=uic.loadUi("menu_editar.ui")
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
sete.pushButton_3.clicked.connect(editar_dados)
tela_editar.pushButton.clicked.connect(salvar_valor_editado)
segunda.pushButton_2.clicked.connect(abre_tela_sete)
sexta.pushButton_6.clicked.connect(volta_tela)
sexta.pushButton_7.clicked.connect(busca_usuario)
quinta.pushButton_6.clicked.connect(volta_tela)
quinta.pushButton_4.clicked.connect(apagar_usuario)
quinta.pushButton_3.clicked.connect(editar_dados_usuario)


primeira.show()
app.exec()