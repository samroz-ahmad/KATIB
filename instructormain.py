from locale import windows_locale
from libraries import *
from drawingboard import *

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
        self.window_open = 0
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

        #Content of Tasks tabs
        self.tasktab.layout=QVBoxLayout(self)
        self.ctlabel = QLabel("Create a task: ")
        self.namelabel = QLabel("Task Name: ")
        self.nameline = QLineEdit()
        self.taskentry = QTextEdit()
        self.createbt = QPushButton ("Create")
        self.drawtaskbt = QPushButton ("Draw your task")

        self.createbt.setStyleSheet("background-color: black; color: white; text-align: centre")

        self.tasktab.layout.addWidget(self.namelabel)
        self.tasktab.layout.addWidget(self.nameline)
        self.tasktab.layout.addWidget(self.ctlabel)
        self.tasktab.layout.addWidget(self.taskentry)
        self.tasktab.layout.addWidget(self.drawtaskbt)
        self.tasktab.layout.addWidget(self.createbt)

        self.createbt.clicked.connect(self.tasktext)
        self.drawtaskbt.clicked.connect(self.drawtask)

        self.tasktab.setLayout(self.tasktab.layout)
        
        #Contents of Review Tab
        self.reviewtab.layout=QVBoxLayout(self)
        self.reviewtab.setLayout(self.reviewtab.layout)

        names = ['Azaz', 'Samroze', 'Zunair', 'Moiz']
        evaluate_buttons = []
        pending_buttons = []
        assign_buttons = []

        for i in range(len(names)):        
            row_layout= QHBoxLayout()
            namelabel = QLabel(names[i])
            assign_buttons.append(QPushButton("Assign Tasks"))
            evaluate_buttons.append(QPushButton("Evaluate Tasks"))
            pending_buttons.append(QPushButton("Pending Tasks"))

            row_layout.addWidget(namelabel)
            row_layout.addWidget(assign_buttons[i])
            row_layout.addWidget(evaluate_buttons[i])
            row_layout.addWidget(pending_buttons[i])
            self.reviewtab.layout.addLayout(row_layout)
        
        assign_buttons[0].clicked.connect(self.assign_task)

        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

    def drawtask(self, checked):
        if self.w is None:
            self.w= DrawingSurface()
            self.w.show()

        else:
            self.w.close()
            self.w = None
        self.close()

    def assign_task(self,checked):  
        if (self.window_open %2 == 0):
            self.window_open +=1
            print(self.window_open)
            print("CLICKED")
            tasklist = ['Write A', 'Write B', 'Write C', 'Write D', 'Write E']
            assignDlg = QDialog()
            assignDlg.layout = QVBoxLayout()
            assigned_tasks = []

            for i in range(len(tasklist)):
                assigned_tasks.append(QCheckBox(tasklist[i]))
                assigned_tasks[i].stateChanged.connect(lambda:self.checked_box(assigned_tasks))
                assignDlg.layout.addWidget(assigned_tasks[i])

            assignDlg.setLayout(assignDlg.layout)
            assignDlg.closeEvent = self.CloseEvent
            assignDlg.show()
            assignDlg.exec_()

    def checked_box(self,tasks):
        for i in range(len(tasks)):
            print(tasks[i])
            print(tasks[i].isChecked())     

    def CloseEvent(self, event):
        self.window_open+=1

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