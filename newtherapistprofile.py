from statistics import quantiles
from libraries import *

class TherapistProfileWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.w = None

        self.setWindowTitle ("KATIB Therapist Profile")
        self.setFixedSize (800,800)
        patient_layout = QVBoxLayout()
        name_layout = QHBoxLayout()
        age_layout = QHBoxLayout()
        affiliation_layout = QHBoxLayout()
        g_layout = QHBoxLayout()
        addr_layout = QHBoxLayout()
        btns_layout = QHBoxLayout()

        name_label = QLabel("Name: ")
        self.name_input = QTextEdit()
        name_layout.addWidget(name_label)
        name_layout.addWidget(self.name_input)

        age_label = QLabel("Speciality: ")
        self.age_input = QTextEdit()
        age_layout.addWidget(age_label)
        age_layout.addWidget(self.age_input)

        affiliation_label = QLabel("Affiliation: ")
        self.affiliation_input = QTextEdit()
        affiliation_layout.addWidget(affiliation_label)
        affiliation_layout.addWidget(self.affiliation_input)

        g_label = QLabel("Age: ")
        self.g_input = QTextEdit()
        g_layout.addWidget(g_label)
        g_layout.addWidget(self.g_input)

        address_label = QLabel("Address: ")
        self.address_input = QTextEdit()
        addr_layout.addWidget(address_label)
        addr_layout.addWidget(self.address_input)

        cancel_btn = QPushButton("Cancel")
        save_profile_btn = QPushButton("Save Profile")
        btns_layout.addWidget(cancel_btn)
        btns_layout.addWidget(save_profile_btn)

        patient_layout.addLayout(name_layout)
        patient_layout.addLayout(age_layout)
        patient_layout.addLayout(affiliation_layout)
        patient_layout.addLayout(g_layout)
        patient_layout.addLayout(addr_layout)
        patient_layout.addLayout(btns_layout)

        save_profile_btn.clicked.connect(self.save_window)

        
        widget = QWidget()
        widget.setLayout(patient_layout)
        self.setCentralWidget(widget)

    def save_window(self):
        namei = self.name_input.toPlainText()
        agei = self.age_input.toPlainText()
        affi = self.affiliation_input.toPlainText()
        gi = self.g_input.toPlainText()
        addri = self.address_input.toPlainText()

        if len(namei and agei and affi and gi and addri) == 0:
            msg=QMessageBox()
            msg.setIcon (QMessageBox.Information)
            msg.setText("Please complete your details")
            msg.setWindowTitle("KATIB")
            msg.setStandardButtons(QMessageBox.Ok)
            retval = msg.exec_()

        elif len(namei or agei or affi or gi or addri) == 0:
            msg2=QMessageBox()
            msg2.setIcon (QMessageBox.Information)
            msg2.setText("Please complete your details")
            msg2.setWindowTitle("KATIB")
            msg2.setStandardButtons(QMessageBox.Ok)
            retval = msg2.exec_()

        else:
            msg3=QMessageBox()
            msg3.setIcon (QMessageBox.Information)
            msg3.setText("Therapist Profile has been created")
            msg3.setWindowTitle("KATIB")
            msg3.setStandardButtons(QMessageBox.Ok)
            print(namei)
            print(agei)
            retval = msg3.exec_()





        
