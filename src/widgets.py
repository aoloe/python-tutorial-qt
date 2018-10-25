import os
from PySide2.QtWidgets import QApplication
from PySide2.QtWidgets import QDialog, QMessageBox
from PySide2.QtCore import QFile, Slot
from PySide2.QtUiTools import QUiLoader

class Dialog(QDialog):
    def __init__(self, parent = None):
        super(Dialog, self).__init__(parent)

    def setup(self):
        for s in ['fusion', 'macintosh', 'windows', 'windowsvista']:
            self.comboBox.addItem(s)
        self.comboBox.currentIndexChanged.connect(self.setStyle)
        for r in range(0, 4):
            self.tableWidget.insertRow(0)
            self.tableWidget.insertColumn(0)
    def setStyle(self) :
        app.setStyle(self.comboBox.currentText())

if __name__ == '__main__':
    app = QApplication([])

    loader = QUiLoader()
    loader.registerCustomWidget(Dialog)

    base_dir = os.path.dirname(os.path.realpath(__file__))
    ui_file = QFile('widgets.ui')
    ui_file = QFile(os.path.join(base_dir, 'widgets.ui'))
    #dialog = loader.load(os.path.join(base_dir, 'widgets.ui'))
    dialog = loader.load(ui_file)
    dialog.setup()
    dialog.show()

    app.exec_()
