from PyQt5 import  uic,QtWidgets
import sqlite3
import bd


def funcao_principal():
    codigo = peixaria.lineEdit.text()
    descricao = peixaria.lineEdit_2.text()
    preco = peixaria.lineEdit_3.text()
    
    if peixaria.radioButton_3.isChecked() :
        print("Categoria Peixe_fresco selecionada")
    elif peixaria.radioButton.isChecked() :
        print("Categoria Peixe_congelado selecionada")
    else :
        print("Categoria Peixe_salgado selecionada")


    print("Código:",codigo)
    print("Descricao:",descricao)
    print("Preco",preco)
    


    
    
    

app=QtWidgets.QApplication([])
peixaria=uic.loadUi("peixaria.ui")
peixaria.pushButton.clicked.connect(funcao_principal)

peixaria.show()
app.exec()