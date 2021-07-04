import sys
# ---> foram adiciondas as classes QPushButton e QTooltip
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip

# criação da classe principal

class Janela(QMainWindow):
    def __init__(self):
        super().__init__()

        self.topo = 100
        self.esquerda = 100
        self.largura = 800
        self.altura = 600
        self.titulo = "Primeira Janela"
      
    # ---> Criar primeiro botão

        botao1 = QPushButton('Botão 1', self)
        botao1.move(250, 250) # determina a posição do elemento dentro da janela
        botao1.resize(50,50) # tamanho do botão
        botao1.setStyleSheet('QPushButton {background-color:#0FB329; font-size:10px}') # estilização do elemento
        botao1.clicked.connect(self.bota01_click) # Conectar ao metodo do click

    # ---> Criar segundo botão

        botao2 = QPushButton('Botão 2', self)
        botao2.move(350, 250) # determina a posição do elemento dentro da janela
        botao2.resize(50,50) # tamanho do botão
        botao2.setStyleSheet('QPushButton {background-color:#0FB329; font-size:10px}') # estilização do elemento
        botao2.clicked.connect(self.bota02_click) # Conectar ao metodo do click

        
        self.CarregarJanela()

    def  CarregarJanela(self):
        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)
        self.setWindowTitle(self.titulo)
        self.show()

    # ---> Método para responder ao click do botão
    def bota01_click(self):
       print("Botão 1 foi clicado") 
    
    def bota02_click(self):
       print("Botão 2 foi clicado") 

# criação da aplicação

aplicação = QApplication(sys.argv)

j = Janela()
sys.exit(aplicação.exec_())