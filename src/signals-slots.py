from PySide2.QtWidgets import QApplication
from PySide2.QtWidgets import QDialog, QVBoxLayout
from PySide2.QtWidgets import QPushButton, QLineEdit

app = QApplication([])
dialog = QDialog()

layout = QVBoxLayout()
layout.addWidget(QLineEdit())
layout.addWidget(QPushButton('Alert'))
layout.addWidget(QPushButton('Quit'))
dialog.setLayout(layout)
dialog.show()
app.exec_()
button = QPushButton('Click')

def on_button_clicked():
    alert = QtWidgets.QMessageBox()
    alert.setText('You clicked the button!')
    alert.exec_()

button.clicked.connect(on_button_clicked)
button.show()
app.exec_()
