import sys
from PyQt5 import QtCore, QtGui, QtWidgets

from tela import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()

        self.ui.zeroButton.clicked.connect(lambda: pressionado("0"))
        self.ui.umButton.clicked.connect(lambda: pressionado("1"))
        self.ui.doisButton.clicked.connect(lambda: pressionado("2"))
        self.ui.tresButton.clicked.connect(lambda: pressionado("3"))
        self.ui.quatroButton.clicked.connect(lambda: pressionado("4"))
        self.ui.cincoButton.clicked.connect(lambda: pressionado("5"))
        self.ui.seisButton.clicked.connect(lambda: pressionado("6"))
        self.ui.seteButton.clicked.connect(lambda: pressionado("7"))
        self.ui.oitoButton.clicked.connect(lambda: pressionado("8"))
        self.ui.noveButton.clicked.connect(lambda: pressionado("9"))
        self.ui.pontoButton.clicked.connect(lambda: pressionado("."))
        self.ui.maisButton.clicked.connect(lambda: pressionado("+"))
        self.ui.menosButton.clicked.connect(lambda: pressionado("-"))
        self.ui.divisionButton.clicked.connect(lambda: pressionado("/"))
        self.ui.multiplicacaoButton.clicked.connect(lambda: pressionado("*"))
        self.ui.igualButton.clicked.connect(lambda: resultado())
        self.ui.clearButton.clicked.connect(lambda: clearOutput())
        self.ui.backspaceButton.clicked.connect(lambda: backspace())

        def resultado():
            saida = self.ui.outputLabel.text()
            try:
                resposta = eval(saida)
                self.ui.outputLabel.setText(f"{resposta:.1f}")
            except:
                self.ui.outputLabel.setText("ERRO")

        def backspace():
            saida = self.ui.outputLabel.text()
            self.ui.outputLabel.setText(saida[:-1])
            if not len(saida[:-1]):
                clearOutput()

        def clearOutput():
            self.ui.outputLabel.setText("0")

        self.operacoes = ['+', '-', '*', '/', '.']

        def pressionado(tecla):
            saida = self.ui.outputLabel.text()
            if saida == "0":
                saida = ""
            if tecla in self.operacoes and saida[-1] in self.operacoes:
                saida = saida[:-1]
            saida += tecla
            self.ui.outputLabel.setText(saida)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())