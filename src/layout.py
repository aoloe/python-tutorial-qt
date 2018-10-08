from PySide2.QtWidgets import QApplication
from PySide2.QtWidgets import QDialog, QVBoxLayout, QPushButton

app = QApplication([])
dialog = QDialog()

layout = QVBoxLayout()
layout.addWidget(QPushButton('Top'))
layout.addWidget(QPushButton('Bottom'))
dialog.setLayout(layout)
dialog.show()
app.exec_()
