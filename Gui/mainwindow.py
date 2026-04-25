from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton
from PyQt6.QtCore import Qt

import sys



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cleaner TF2")
        self.setMinimumSize(300,300)

        self.setStyleSheet('''
        QMainWindow{
               background-color: #696969;            
         }
''')



app = QApplication(sys.argv)

window = MainWindow()
window.show()


def StartApp():
    app.exec()


if __name__ == "__main__":
    StartApp()