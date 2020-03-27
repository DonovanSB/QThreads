
from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QVBoxLayout, QLabel
import sys
from PyQt5.QtCore import Qt, QThread, pyqtSignal
import time
import schedule

class Thread(QThread):
    updateSignal = pyqtSignal()
    def __init__(self,time):
        super(Thread,self).__init__()
        self.time = time

    def run(self):
        schedule.every(self.time).seconds.do(self.task)
        while True:
            schedule.run_pending()
            time.sleep(0.1)

    def task(self):
        print("Hola desde el nuevo Thread")
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
        t = 5 # repite task cada t segundos
        self.thread = Thread(t)
        self.thread.updateSignal.connect(self.task2) # comunicación entre Threads
        self.thread.start()
        self.show()

    def task1(self):
        print("Hola desde el Thread principal")

    def task2(self):
        print("Comunicación entre Threads")

App = QApplication(sys.argv)
window = Main()
sys.exit(App.exec_())