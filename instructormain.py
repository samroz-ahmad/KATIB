from libraries import *

class InstructorMain (QMainWindow):
    def __init__(self, parent=None):
        super(InstructorMain,self).__init__(parent)
        self.title = 'KATIB'
        self.width = 300
        self.height = 200
        self.setWindowTitle(self.title)
        self.setFixedSize (500,500)

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

        #Content of Tasks tab//Will call instructortasks.py
        self.tasktab.layout=QVBoxLayout(self)
        self.ctlabel = QLabel("Create a task: ")
        self.taskentry = QTextEdit()
        self.createbt = QPushButton ("Create")
        self.tasktab.layout.addWidget(self.ctlabel)
        self.tasktab.layout.addWidget(self.taskentry)
        self.tasktab.layout.addWidget(self.createbt)

        self.createbt.clicked.connect(self.tasktext)
        self.tasktab.setLayout(self.tasktab.layout)

        #Contents of Review Tab//Will call intructorreview.py
        self.reviewtab.layout=QVBoxLayout(self)
        self.displayr = QLabel("This is the review tab")
        self.reviewtab.layout.addWidget(self.displayr)
        self.reviewtab.setLayout(self.reviewtab.layout)

        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

    def tasktext(self):
        createdtask = self.taskentry.toPlainText()
        if len(createdtask) == 0:
            msg=QMessageBox()
            msg.setIcon (QMessageBox.Information)
            msg.setText("Please write something")
            msg.setWindowTitle("Katib")
            msg.setStandardButtons(QMessageBox.Ok)
            retval = msg.exec_()

        else:
            msg2=QMessageBox()
            msg2.setIcon (QMessageBox.Information)
            msg2.setText("Your task has been submitted")
            msg2.setWindowTitle("KATIB")
            msg2.setStandardButtons(QMessageBox.Ok)
            print(createdtask)
            retval = msg2.exec_()