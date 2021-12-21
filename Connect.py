import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import QDialog, QApplication

from dialogConnect import Ui_Dialog

admin = "landry"
mdp = "ssss"


class Connect_dialog(Ui_Dialog, QDialog):
    def __init__(self):
        super(Connect_dialog, self).__init__(parent=None)
        self.setupUi(self)
        self.connectActions()
        self.hideState()
        self.connection = False

    def connectActions(self):
        self.check_mpd_view.stateChanged.connect(self.clickCheck)
        self.btn_connect.clicked.connect(self.connect)
        self.btn_reset.clicked.connect(self.close)
        self.motDePasseLineEdit.textChanged.connect(self.hideState)
        self.nomDeLAdministrateurLineEdit.textChanged.connect(self.hideState)

    def hideState(self):
        self.label_status.hide()

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        if self.connection:
            a0.accept()

    def connect(self):
        if self.nomDeLAdministrateurLineEdit.text() == admin and self.motDePasseLineEdit.text() == mdp:
            self.connection = True
            self.close()
        else:
            self.label_status.show()

    def clickCheck(self):
        if self.check_mpd_view.checkState() != 2:
            self.motDePasseLineEdit.setEchoMode(2)
        else:
            self.motDePasseLineEdit.setEchoMode(0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    connect = Connect_dialog()
    connect.show()
    app.exec_()
