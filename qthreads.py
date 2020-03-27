
from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QVBoxLayout, QLabel
import sys
from PyQt5.QtCore import Qt, QThread, pyqtSignal
import time

class Thread(QThread):
    updateSignal = pyqtSignal()
    def __init__(self,time):
        super(Thread,self).__init__()
        self.time = time

    def run(self):
        while True:
            time.sleep(self.time)
            self.updateSignal.emit()


class Main(QDialog):
    def __init__(self):
        super(Main,self).__init__()
        self.setGeometry(500, 200, 300, 100)

        #crear layout
        vbox = QVBoxLayout(self)
        #crear Label
        label = QLabel("QThreads")
        label.setAlignment(Qt.AlignCenter)
        boton = QPushButton("Hilo Principal")
        boton.clicked.connect(self.task1)
        vbox.addWidget(label)
        vbox.addWidget(boton)

        #Definir nuevo hilo
        t = 1 # repite task2 cada t segundos
        self.thread = Thread(t)
        self.thread.updateSignal.connect(self.task2)
        self.thread.start()
        self.show()

    def task1(self):
        print("Hola desde el Thread principal")

    def task2(self):
        print("Hola desde nuevo Thread")

App = QApplication(sys.argv)
window = Main()
sys.exit(App.exec_())