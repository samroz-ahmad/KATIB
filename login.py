from instructormain import *

class LoginWindow (QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.w=None #Does not open anything yet

        self.setWindowTitle ("KATIB Login")
        self.setFixedSize (500,200)
        loglayout=QVBoxLayout()
        idlayout= QHBoxLayout()
        pswlayout=QHBoxLayout()

        message_label =QLabel("Please enter your login details")
        id_label=QLabel("Username/ID: ")
        id_input=QLineEdit()
        psw_label=QLabel("Password: ")
        psw_input=QLineEdit()
        login_bt=QPushButton("login")

        id_label.setAlignment(Qt.AlignCenter)
        id_label.setFont(QFont('Arial', 10))
        psw_label.setAlignment(Qt.AlignCenter)
        psw_label.setFont(QFont('Arial', 10))

        login_bt.clicked.connect(self.show_main_window)

        idlayout.addWidget(id_label)
        idlayout.addWidget(id_input)

        pswlayout.addWidget(psw_label)
        pswlayout.addWidget(psw_input)

        loglayout.addLayout(idlayout)
        loglayout.addLayout(pswlayout)
        loglayout.addWidget(login_bt)

        widget = QWidget()
        widget.setLayout(loglayout)
        self.setCentralWidget(widget)

    def show_main_window(self,checked):
        if self.w is None:
            self.w= InstructorMain()
            self.w.show()
        else:
            self.w.close()
            self.w = None
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FirstWindow()
    window.show()
    sys.exit(app.exec_())