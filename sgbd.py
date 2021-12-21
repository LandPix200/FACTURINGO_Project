import sys

from PyQt5.QtWidgets import QApplication, QTableWidgetItem, QDialog
import gestionBD
from sgbdWindow import Ui_Dialog

liste_nom = []


class Doc(Ui_Dialog, QDialog):
    def __init__(self, parent=None):
        super(Doc, self).__init__(parent)
        self.setupUi(self)
        self.showMaximized()
        self.remplir_table_client()
        self.remplir_table_articles()

        self.btn_save.clicked.connect(self.saveStock)

    def saveStock(self):
        texts = []
        for i in range(self.table_stock.rowCount()):
            if not self.table_stock.item(i, 0) is None:
                try:
                    des = self.table_stock.item(i, 0).text()
                    qtte = self.table_stock.item(i, 1).text()
                    prix = self.table_stock.item(i, 2).text()
                    text = f"{des}:{prix}:{qtte}\n"
                    texts.append(text)
                except AttributeError:
                    continue
        with open("data/articles.bdf", 'w') as art_file:
            art_file.writelines(texts)

    def remplir_table_articles(self):
        try:
            for i in range(self.table_stock.rowCount()):
                if self.table_stock.item(i, 0) is None:
                    des = QTableWidgetItem(gestionBD.list_article[i])
                    prix = QTableWidgetItem(gestionBD.list_prix[i])
                    qtte = QTableWidgetItem(gestionBD.qtte_article[i])
                    self.table_stock.setItem(i, 0, des)
                    self.table_stock.setItem(i, 1, qtte)
                    self.table_stock.setItem(i, 2, prix)
        except IndexError:
            pass

    def remplir_table_client(self):
        try:
            for i in range(self.table_stock.rowCount()):
                if self.table_stock.item(i, 0) is None:
                    nom = QTableWidgetItem(gestionBD.list_nom[i])
                    tel = QTableWidgetItem(gestionBD.list_tel[i])
                    mail = QTableWidgetItem(gestionBD.list_email[i])
                    self.table_client.setItem(i, 0, nom)
                    self.table_client.setItem(i, 1, tel)
                    self.table_client.setItem(i, 2, mail)
        except IndexError:
            pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    doc = Doc()
    doc.show()
    app.exec_()
