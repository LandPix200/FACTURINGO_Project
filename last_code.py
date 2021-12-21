import shutil
import sqlite3
import sys
from pathlib import Path

import openpyxl as openpyxl
from PyQt5.QtWidgets import QApplication, QMainWindow

import window

sample = "data/sample.xlsx"
conn = sqlite3.connect("Database/based.db")

client = conn.cursor()

client.execute("""
    CREATE TABLE IF NOT EXISTS CLIENT(
        nom TEXT,
        bp TEXT,
        tel TEXT,
        fax TEXT,
        lieu TEXT
        );


""")

des = conn.cursor()
des.execute("""
    CREATE TABLE IF NOT EXISTS PRODUIT(
        designation TEXT,
        quantite TEXT,
        pu TEXT,
        montant TEXT,
        moderef TEXT,
        netapayer TEXT
        );

""")


# cursor.execute("""
#     CREATE TABLE IF NOT EXISTS FACTURE(
#         numero INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE
#         );
#
# """)


def quitter():
    quit(0)


class Conta(QMainWindow, window.Ui_MainWindow):
    def __init__(self, parent=None):
        super(Conta, self).__init__(parent)
        self.setupUi(self)
        self.connect_actions()

    def connect_actions(self):
        self.actionQuitter.triggered.connect(quitter)
        self.btn_enregistrer.clicked.connect(self.enregistrer)
        self.btn_effacer.clicked.connect(self.effacer)

    def enregistrer(self):
        global row, v

        netap = str(int(self.pUSpinBox.value()) * int(self.quantitSpinBox.value())) + " FCFA"

        dict_clt = {
            "nom": self.nomLineEdit.text(),
            "bp": self.bPSpinBox.text(),
            "tel": self.telSpinBox.text(),
            "fax": self.faxLineEdit.text(),
            "lieu": self.lieuLineEdit.text()
        }

        dict_prod = {
            "des": self.dSignationLineEdit.text(),
            "qtt": self.quantitSpinBox.text(),
            "pu": self.pUSpinBox.text(),
            "mnt": self.montantSpinBox.text(),
            "mode_ref": self.modeDeRGlementComboBox.currentText(),
            "netap": netap
        }

        client.execute("""
        INSERT INTO CLIENT(nom, bp, tel, fax, lieu)
        VALUES(:nom, :bp, :tel, :fax, :lieu);
        """, dict_clt)

        des.execute("""
        INSERT INTO PRODUIT(designation, quantite, pu, montant, moderef, netapayer)
        VALUES(:des, :qtt, :pu, :mnt, :mode_ref, :netap);
        """, dict_prod)

        # cursor.execute("""
        # INSERT INT
        # """)

        client.execute("""
        SELECT * FROM CLIENT;
        """)

        des.execute("""
               SELECT * FROM PRODUIT;
               """)
        for row in client:
            pass

        for v in des:
            pass

        # On copie le fichier sample dans un fichier dans le doosier facture et on nomme ce dossier avec le nom du
        # client
        file = Path(f"factures/{str(row[0])}.xlsx")
        if not file.is_file():
            add_num()
            shutil.copyfile(sample, f"factures/{str(row[0])}.xlsx")
            ecrire_exel_clt(f"factures/{str(row[0])}.xlsx", row)

        self.ecrire_exel_des(f"factures/{str(row[0])}.xlsx", v)

        self.dSignationLineEdit.clear()
        self.pUSpinBox.setProperty("value", 0)
        self.quantitSpinBox.setProperty("value", 0)
        self.montantSpinBox.setProperty("value", 0)

    # Fonction qui ecrit dans le fichier les differentes designations et consor

    def effacer(self):
        self.nomLineEdit.clear()
        self.bPSpinBox.setProperty("value", 0)
        self.telSpinBox.setProperty("value", 6)
        self.faxLineEdit.clear()
        self.lieuLineEdit.clear()
        self.dSignationLineEdit.clear()
        self.pUSpinBox.setProperty("value", 0)
        self.quantitSpinBox.setProperty("value", 0)
        self.montantSpinBox.setProperty("value", 0)

    def main(self):
        self.show()

    def ecrire_exel_des(self, path, liste):
        netap = str(int(self.pUSpinBox.value()) * int(self.quantitSpinBox.value())) + " FCFA"

        # On créer un "classeur"
        classeur = openpyxl.load_workbook(path)
        # On ajoute une feuille au classeur
        feuille = classeur.active

        feuille['B12'].value = liste[0]
        feuille['C12'].value = liste[1]
        feuille['D12'].value = liste[2]
        feuille['E12'].value = netap
        feuille['E30'].value = liste[4]

        classeur.save(path)
        classeur.close()


# Fonction qui ecrit dans le fichier les adresses du clt mais uniquement si ce fichier n'existe pas encore
def ecrire_exel_clt(path, liste):
    # On créer un "classeur"
    classeur = openpyxl.load_workbook(path)
    # On ajoute une feuille au classeur
    feuille = classeur.active

    for i in range(len(liste)):
        feuille[f"E{i + 4}"].value = liste[i]

    with open("data/num.txt", 'r') as num:
        feuille['C9'].value = num.read(-1)

    classeur.save(path)
    classeur.close()


def add_num():
    with open("data/num.txt", 'r') as f_r:
        nbre = f_r.read(-1)
    with open("data/num.txt", 'w') as f_w:
        f_w.write(str(int(nbre) + 1))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    imageViewer = Conta()
    imageViewer.main()
    app.exec_()
    add_num()
