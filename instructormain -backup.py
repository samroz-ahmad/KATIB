import sys
from tkinter import Widget
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, \
    QPushButton, QVBoxLayout, QFileDialog, QLabel, QTextEdit, QLineEdit,\
         QHBoxLayout, QTabWidget

class InstructorMain (QMainWindow):
    def __init__(self, parent=None):
        super(InstructorMain,self).__init__(parent)
        self.title = 'KATIB'
        self.width = 300
        self.height = 200
        self.setWindowTitle(self.title)
        self.setFixedSize (800,800)

        self.table_widget = MyTableWidget(self)
        self.setCentralWidget(self.table_widget)
        self.show()
        
class MyTableWidget(QWidget):
    def __init__(self, parent) -> None:
        super(QWidget, self).__init__(parent)
        self.layout=QVBoxLayout(self)

        #Creating 2 tabs
        self.tabs=QTabWidget()
        self.tasktab=QWidget()
        self.reviewtab=QWidget()
        self.tabs.resize(300,200)

        #Adding tabs to the main tab widget
        self.tabs.addTab(self.tasktab,"Tasks")
        self.tabs.addTab(self.reviewtab,"Review")

        #Content of Tasks tab
        self.tasktab.layout=QVBoxLayout(self)
        self.displayt = QLabel("This is the Tasks tab")
        self.tasktab.layout.addWidget(self.displayt)
        self.tasktab.setLayout(self.tasktab.layout)

        #Contents of Review Tab
        self.reviewtab.layout=QVBoxLayout(self)
        self.displayr = QLabel("This is the review tab")
        self.reviewtab.layout.addWidget(self.displayr)
        self.reviewtab.setLayout(self.reviewtab.layout)

        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)




