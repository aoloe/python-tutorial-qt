from PySide2.QtWidgets import QApplication
from PySide2.QtWidgets import QDialog, QMessageBox, QVBoxLayout
from PySide2.QtWidgets import QPushButton, QLineEdit

class Dialog(QDialog):
    def __init__(self, parent = None):
        super(Dialog, self).__init__()

        self.text_field = QLineEdit()
        self.alert_button = QPushButton('Alert')
        self.quit_button = QPushButton('Quit')

        layout = QVBoxLayout()
        layout.addWidget(self.text_field)
        layout.addWidget(self.alert_button)
        layout.addWidget(self.quit_button)
        self.setLayout(layout)

        self.alert_button.clicked.connect(self.alert)
        self.quit_button.clicked.connect(quit)

    def alert(self):
        alert = QMessageBox()
        alert.setText(self.text_field.text())
        alert.exec_()

if __name__ == '__main__':
    app = QApplication([])
    dialog = Dialog()
    dialog.show()
    app.exec_()
