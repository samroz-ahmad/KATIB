from libraries import *

class PatientProfileWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.w = None

        self.setWindowTitle ("KATIB Patient Profile")
        self.setFixedSize (500,200)
        patient_layout = QVBoxLayout()
        name_layout = QHBoxLayout()
        age_layout = QHBoxLayout()
        btns_layout = QHBoxLayout()

        name_label = QLabel("Please enter the patient's name: ")
        name_input = QLineEdit()
        name_layout.addWidget(name_label)
        name_layout.addWidget(name_input)

        age_label = QLabel("Please enter the patient's age: ")
        age_input = QLineEdit()
        age_layout.addWidget(age_label)
        age_layout.addWidget(age_input)

        cancel_btn = QPushButton("Cancel")
        save_profile_btn = QPushButton("Save Patient Profile")
        btns_layout.addWidget(cancel_btn)
        btns_layout.addWidget(save_profile_btn)

        patient_layout.addLayout(name_layout)
        patient_layout.addLayout(age_layout)
        patient_layout.addLayout(btns_layout)

        save_profile_btn.clicked.connect(self.save_window)

        
        widget = QWidget()
        widget.setLayout(patient_layout)
        self.setCentralWidget(widget)

    def save_window(self):
        namei = self.name_input.toPlainText()
        agei = self.age_input.toPlainText()
        if len(namei & agei) == 0:
            msg=QMessageBox()
            msg.setIcon (QMessageBox.Information)
            msg.setText("Please complete patient details")
            msg.setWindowTitle("Katib")
            msg.setStandardButtons(QMessageBox.Ok)
            retval = msg.exec_()

        elif len(namei | agei) == 0:
            msg2=QMessageBox()
            msg2.setIcon (QMessageBox.Information)
            msg2.setText("Please complete patient details")
            msg2.setWindowTitle("Katib")
            msg2.setStandardButtons(QMessageBox.Ok)
            retval = msg2.exec_()

        else:
            msg3=QMessageBox()
            msg3.setIcon (QMessageBox.Information)
            msg3.setText("Patient Profile has been created")
            msg3.setWindowTitle("KATIB")
            msg3.setStandardButtons(QMessageBox.Ok)
            print(namei)
            print(agei)
            retval = msg3.exec_()





        
