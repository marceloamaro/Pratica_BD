import sys

from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QToolTip

from PyQt5 import QtGui


class Janela(QMainWindow):
    def __init__(self):
        super().__init__()

        self.topo = 100
        self.esquerda = 100
        self.largura = 900
        self.altura = 800
        self.titulo = "Primeira Janela"
      
    

        botao1 = QPushButton('Botão 1', self)
        botao1.move(250, 250) 
        botao1.resize(50,50) 
        botao1.setStyleSheet('QPushButton {background-color:#0FB329; font-size:10px}') 
        botao1.clicked.connect(self.bota01_click) 

   

        botao2 = QPushButton('Botão 2', self)
        botao2.move(350, 250) 
        botao2.resize(50,50) 
        botao2.setStyleSheet('QPushButton {background-color:#0FB329; font-size:10px}') 
        botao2.clicked.connect(self.bota02_click) 



        botao3 = QPushButton('Botão 3', self)
        botao3.move(450, 250) 
        botao3.resize(50,50) 
        botao3.setStyleSheet('QPushButton {background-color:#0FB329; font-size:10px}') 
        botao3.clicked.connect(self.bota03_click) 
    
    
        self.label_1 = QLabel(self)
        self.label_1.setText("LINGUAGEM DE PROGRAMAÇÃO")
        self.label_1.move(220, 220)
        self.label_1.setStyleSheet("QLabel {color:red; font-size:25px}")
        self.label_1.resize(400, 25)

    
        self.logo = QLabel(self)
        self.logo.move(500, 200)
        self.logo.resize(500, 600)
        self.CarregarJanela()

    def  CarregarJanela(self):
        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)
        self.setWindowTitle(self.titulo)
        self.show()

    
    def bota01_click(self):
        self.label_1.setStyleSheet("QLabel {color:blue; font-size:25px}")

        self.label_1.setText("Pyton")
        self.logo.setPixmap(QtGui.QPixmap('python.png')) 

    
    def bota02_click(self):
        self.label_1.setStyleSheet("QLabel {color:blue; font-size:25px}")

        self.label_1.setText("Java")
        self.logo.setPixmap(QtGui.QPixmap('java.png')) 

    def bota03_click(self):
        self.label_1.setStyleSheet("QLabel {color:blue; font-size:25px}")

        self.label_1.setText("C")
        self.logo.setPixmap(QtGui.QPixmap('cc.png')) 



aplicação = QApplication(sys.argv)

j = Janela()
sys.exit(aplicação.exec_())