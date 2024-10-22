import sys

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QVBoxLayout, QWidget, QScrollArea, QMainWindow

from app.IHM.widgets.info_collection.info_collection import InfoLectureVolume
from app.IHM.widgets.item_lecture_volume import ItemLectureVolume


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.scroll = QScrollArea()             # Scroll Area which contains the widgets, set as the centralWidget
        self.widget = QWidget()                 # Widget that contains the collection of Vertical Box
        self.vbox = QVBoxLayout()
        # The Vertical Box that contains the Horizontal Boxes of  labels and buttons
        self.vbox.addWidget(InfoLectureVolume())
        for i in range(1,5000):
            object = ItemLectureVolume()
            self.vbox.addWidget(object)

        self.widget.setLayout(self.vbox)

        #Scroll Area Properties
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.widget)

        self.setCentralWidget(self.scroll)

        self.setGeometry(600, 100, 1000, 900)
        self.setWindowTitle('Scroll Area Demonstration')
        self.show()


app = QtWidgets.QApplication(sys.argv)
main = MainWindow()
sys.exit(app.exec())