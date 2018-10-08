from PySide2 import QtCore, QtWidgets, QtGui

app = QtWidgets.QApplication([])
app.setStyle('Fusion')
palette = QtGui.QPalette()
palette.setColor(QtGui.QPalette.ButtonText, QtCore.Qt.red)
app.setPalette(palette)
button = QtWidgets.QPushButton('Hello World')
button.show()
app.exec_()
