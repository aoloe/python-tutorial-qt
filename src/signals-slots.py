from PySide2.QtWidgets import QApplication
from PySide2.QtWidgets import QDialog, QMessageBox, QVBoxLayout
from PySide2.QtWidgets import QPushButton, QLineEdit

app = QApplication([])
dialog = QDialog()

def on_alert_clicked():
    global text_field
    alert = QMessageBox()
    alert.setText(text_field.text())
    alert.exec_()

layout = QVBoxLayout()
text_field = QLineEdit()
alert_button = QPushButton('Alert')
quit_button = QPushButton('Quit')
layout.addWidget(text_field)
layout.addWidget(alert_button)
layout.addWidget(quit_button)
dialog.setLayout(layout)

alert_button.clicked.connect(on_alert_clicked)
quit_button.clicked.connect(quit)

dialog.show()
app.exec_()
