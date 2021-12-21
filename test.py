import sys

from PyQt5.QtWidgets import QApplication

from Connect import Connect_dialog

app = QApplication(sys.argv)
yo = Connect_dialog()
yo.show()
app.exec_()

if yo.connection:
    print("Connection OK")
else:
    print("EUIL !!!")




