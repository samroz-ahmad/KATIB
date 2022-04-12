from login import *
from patientprofile import *

class FirstWindow (QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.w=None

        self.setWindowTitle("KATIB")
        self.setFixedSize (500,500)
        layout=QVBoxLayout()
        buttonlayout=QHBoxLayout()

        flabel = QLabel("Welcome to KATIB!")
        profile_btn = QPushButton("Create Patient Profile")
        login_btn = QPushButton("Login as Therapist")

        flabel.setAlignment(Qt.AlignCenter)
        flabel.setFont(QFont('Arial', 10))

        profile_btn.clicked.connect(self.show_profile_window)
        login_btn.clicked.connect(self.show_login_window)

        buttonlayout.addWidget(profile_btn)
        buttonlayout.addWidget(login_btn)

        layout.addWidget(flabel)
        layout.addLayout(buttonlayout)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def show_login_window(self,checked):
        if self.w is None:
            self.w= LoginWindow()
            self.w.show()
        else:
            self.w.close()
            self.w = None
        self.close()

    def show_profile_window(self,checked):
        if self.w is None:
            self.w= PatientProfileWindow()
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
    