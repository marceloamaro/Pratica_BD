from PyQt5 import  uic,QtWidgets

def funcao_principal():
    linha1 = peixaria.lineEdit.text()
    linha2 = peixaria.lineEdit_2.text()
    linha3 = peixaria.lineEdit_3.text()
    
    if peixaria.radioButton_3.isChecked() :
        print("Categoria Peixe_fresco selecionada")
    elif peixaria.radioButton.isChecked() :
        print("Categoria Peixe_congelado selecionada")
    else :
        print("Categoria Peixe_salgado selecionada")

    print("Código:",linha1)
    print("Descricao:",linha2)
    print("Preco",linha3)
    

app=QtWidgets.QApplication([])
peixaria=uic.loadUi("peixaria.ui")
peixaria.pushButton.clicked.connect(funcao_principal)

peixaria.show()
app.exec()