from PyQt6.QtWidgets import QMainWindow
from CentralWidget import CentralWidget


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.central_widget = CentralWidget(parent)

        self.setCentralWidget(self.central_widget)

        self.setWindowTitle("Einführung in QCharts")

        self.central_widget.setMinimumWidth(300) #Breite des Fensters verändern
