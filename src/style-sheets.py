from PySide2 import QtCore, QtWidgets, QtGui

app = QtWidgets.QApplication([])
app.setStyleSheet("QPushButton { background-color: 10ex; }")
button = QtWidgets.QPushButton('Hello World')
button.show()
app.exec_()
