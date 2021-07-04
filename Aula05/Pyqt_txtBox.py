import sys
from PyQt5.QtCore import QLine

from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QToolTip, QLineEdit
# ---> foi adicionada classe QlineEdit
from PyQt5 import QtGui
# criação da classe principal

class Janela(QMainWindow):
    def __init__(self):
        super().__init__()

        self.topo = 100
        self.esquerda = 100
        self.largura = 800
        self.altura = 600
        self.titulo = "Primeira Janela"
      
        self.caixa_texto = QLineEdit(self)
        self.caixa_texto.move(350, 160)
        self.caixa_texto.resize(250, 30)
    # Criar primeiro botão

        botao1 = QPushButton('Botão 1', self)
        botao1.move(350, 250) # determina a posição do elemento dentro da janela
        botao1.resize(50,50) # tamanho do botão
        botao1.setStyleSheet('QPushButton {background-color:#0FB329; font-size:10px}') # estilização do elemento
        botao1.clicked.connect(self.bota01_click) # Conectar ao metodo do click

    # Criar segundo botão

        botao2 = QPushButton('Botão 2', self)
        botao2.move(450, 250) # determina a posição do elemento dentro da janela
        botao2.resize(50,50) # tamanho do botão
        botao2.setStyleSheet('QPushButton {background-color:#0FB329; font-size:10px}') # estilização do elemento
        botao2.clicked.connect(self.bota02_click) # Conectar ao metodo do click

    # Criar o botão para a caixa de texto
        botao_caixa = QPushButton('Enviar', self)
        botao_caixa.move(550, 250) # determina a posição do elemento dentro da janela
        botao_caixa.resize(50,50) # tamanho do botão
        botao_caixa.setStyleSheet('QPushButton {background-color:#0FB329; font-size:10px}') # estilização do elemento
        botao_caixa.clicked.connect(self.bota01_click) # Conectar ao metodo do click

    # Criação a Label
        self.label_1 = QLabel(self)
        self.label_1.setText("Olá Mundo")
        self.label_1.move(400, 120)
        self.label_1.setStyleSheet("QLabel {color:red; font-size:25px}")
        self.label_1.resize(200, 25)

    # Criação da label caixa
        self.label_caixa = QLabel(self)
        self.label_caixa.setText("Digitou: ")
        self.label_caixa.move(400, 420)
        self.label_caixa.setStyleSheet("QLabel {color:red; font-size:25px}")
        self.label_1.resize(200, 25)


    #  Criação da label que vai guardar a imagem
        self.logo = QLabel(self)
        self.logo.move(450, 200)
        self.logo.resize(400, 500)
        self.CarregarJanela()

    def  CarregarJanela(self):
        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)
        self.setWindowTitle(self.titulo)
        self.show()

    # Método para responder ao click do botão
    def bota01_click(self):
        self.label_1.setStyleSheet("QLabel {color:blue; font-size:25px}")

        self.label_1.setText("Pyton")
        self.logo.setPixmap(QtGui.QPixmap('python.png')) # importação da imagem

    
    def bota02_click(self):
        self.label_1.setStyleSheet("QLabel {color:pink; font-size:25px}")

        self.label_1.setText("Java")
        self.logo.setPixmap(QtGui.QPixmap('java.png')) # importação da imagem

    # Método para capturar texto digitado
    def mostra_texto(self):
        self.label_1.setStyleSheet("QLabel {color:pink; font-size:25px}")

        self.label_1.setText("Java")
        self.logo.setPixmap(QtGui.QPixmap('java.png')) # importação da imagem

# criação da aplicação
aplicação = QApplication(sys.argv)

j = Janela()
sys.exit(aplicação.exec_())