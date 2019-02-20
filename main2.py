import sys
# Импортируем наш интерфейс из файла
from test2 import *
from PyQt5 import QtCore, QtGui, QtWidgets

class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Здесь прописываем событие нажатия на кнопку
        # self.ui.pushButton.clicked.connect(self.MyFunction)

    # Пока пустая функция которая выполняется
    # при нажатии на кнопку
    def MyFunction(self):
        self.ui.textEdit_2.setText("")
        strings = self.ui.textEdit.toPlainText()
        # arr = strings.split('\n')
        result = ''
        quotes[0] = strings
        result = compare_texts(quotes)
        self.ui.textEdit_2.setText(result)

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
