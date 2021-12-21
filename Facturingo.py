import shutil
import sys
from datetime import date
from pathlib import Path

import openpyxl
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem

import window
from Connect import Connect_dialog
from gestionBD import list_article, list_prix
from sgbd import Doc

sample = "data/sample.xlsx"


def openDataBase():
    win = Connect_dialog()
    win.exec_()
    if win.connection:
        win_sgbd = Doc()
        win_sgbd.exec_()


class Conta(QMainWindow, window.Ui_MainWindow):
    def __init__(self, parent=None):
        super(Conta, self).__init__(parent)
        self.setupUi(self)
        self.showMaximized()
        self.is_save = False
        self.is_new = True
        self.updateWindowTitle("Nouvel Achat")

        self.articleComboBox.addItems(list_article)
        self.connect_actions()

        self.hideAlertNom()
        self.hideAlertTel()
        self.hideAlertEmail()

    def connect_actions(self):
        self.actionQuitter.triggered.connect(self.quitter)
        self.btn_save.clicked.connect(self.enregistrer)
        self.actionEnregistrer_3.triggered.connect(self.enregistrer)
        self.actionOuvrir.triggered.connect(self.openFile)
        self.actionExporter_en_facture.triggered.connect(self.export)
        self.actionArri_re.triggered.connect(self.undo)
        self.actionAvancer.triggered.connect(self.redo)
        self.actionCopier.triggered.connect(self.copy)
        self.actionCouper.triggered.connect(self.cut)
        self.actionColler.triggered.connect(self.paste)
        self.btn_reset_clt_values.clicked.connect(self.reset_clt)
        self.articleComboBox.currentIndexChanged.connect(self.change_achat)
        self.quantitSpinBox.valueChanged.connect(self.prixTotal)
        self.btn_ajouter_achat.clicked.connect(self.add_achat)
        self.actionNouveau.triggered.connect(self.newFile)
        self.btn_rein.clicked.connect(self.resetTableAchat)
        self.btn_export.clicked.connect(self.exportFacture)
        self.btn_open_database.clicked.connect(openDataBase)
        self.emailLineEdit.textChanged.connect(self.hideAlertEmail)
        self.telSpinBox.valueChanged.connect(self.hideAlertTel)
        self.nomLineEdit.textChanged.connect(self.hideAlertNom)

    def hideAlertEmail(self):
        self.lb_alert_email.hide()

    def hideAlertNom(self):
        self.lb_alert_nom.hide()

    def hideAlertTel(self):
        self.lb_alert_num.hide()

    def exportFacture(self):
        filename = self.nomLineEdit.text() + "_" + str(date.today())
        myFile = f"factures/{filename}.xlsx"
        shutil.copyfile(sample, myFile)

        self.insertExcel(myFile)

    def insertExcel(self, filename):
        # On créer un "classeur"
        classeur = openpyxl.load_workbook(filename)
        # On ajoute une feuille au classeur
        feuille = classeur.active

        feuille["F3"] = self.nomLineEdit.text()
        feuille["F4"] = self.bPSpinBox.value().__str__()
        feuille["F5"] = self.telSpinBox.value().__str__()
        feuille["F6"] = self.emailLineEdit.text()
        feuille["E25"] = self.modeDePayementComboBox.currentText()

        for i in range(0, self.table_achats.rowCount()):
            if not self.table_achats.item(i, 0) is None:
                try:
                    feuille[f"B{15 + i}"] = self.table_achats.item(i, 0).text()
                    feuille[f"C{15 + i}"] = int(self.table_achats.item(i, 1).text())
                    feuille[f"D{15 + i}"] = int(self.table_achats.item(i, 2).text().split(" ")[0])
                    feuille[f"E{15 + i}"] = int(self.table_achats.item(i, 3).text().split(" ")[0])
                    feuille[f"F{15 + i}"] = self.table_achats.item(i, 4).text()
                except AttributeError:
                    pass

        classeur.save(filename)
        classeur.close()

    def resetTableAchat(self):
        self.table_achats.clear()
        self.table_achats.setHorizontalHeaderLabels(['Désignation', 'Quantité', "Prix", "Prix Total", "Observation"])

    def newFile(self):
        if not self.is_save:
            self.saveAlert()

        else:
            self.reset_clt()
            self.reset_achat()
            self.updateWindowTitle("Nouvel Achat")
            self.is_new = True

    def saveAlert(self):
        QMessageBox.warning(self, "Sauvegarder votre travail", "Attention vous avez oublié de sauvegarder"
                                                               "\nvotre travail", QMessageBox.Ok)

    def updateWindowTitle(self, newTitle: str):
        self.setWindowTitle("FACTURINGO")
        self.setWindowTitle(self.windowTitle() + " --- " + newTitle)

    def add_achat(self):

        article = QTableWidgetItem(self.articleComboBox.currentText())
        quantity = QTableWidgetItem(str(self.quantitSpinBox.value()))
        prix = QTableWidgetItem(str(self.prixSpinBox.value()) + " FCFA")
        prix_total = QTableWidgetItem(str(self.prixTotalSpinBox.value()) + " FCFA")

        observation = QTableWidgetItem(str(self.obs_edit.text()))

        for i in range(0, self.table_achats.rowCount()):
            if self.table_achats.item(i, 0) is None:
                self.table_achats.setItem(i, 0, article)
                self.table_achats.setItem(i, 1, quantity)
                self.table_achats.setItem(i, 2, prix)
                self.table_achats.setItem(i, 3, prix_total)
                self.table_achats.setItem(i, 4, observation)
                break

        self.reset_achat()

    def reset_achat(self):
        self.articleComboBox.setCurrentIndex(0)
        self.quantitSpinBox.setValue(1)
        self.prixSpinBox.setValue(0)
        self.prixTotalSpinBox.setValue(0)
        self.obs_edit.setText("")

    def prixTotal(self):
        try:
            self.prixTotalSpinBox.setValue((self.prixSpinBox.value() * self.quantitSpinBox.value()))
        except OverflowError:
            self.setStatusTip("LES GROSSES SOMMES SONT INCONNUES ICI DESOLE !!")

    def change_achat(self):
        try:
            try:
                self.prixSpinBox.setValue(int(list_prix[self.articleComboBox.currentIndex()]))
            except ValueError:
                self.articleComboBox.setStatusTip(
                    f"Attention L'article {self.articleComboBox.currentText()} n'a pas de prix dans"
                    f"la base de donnée !")
        except IndexError:
            pass
        self.prixTotal()

    def undo(self):
        try:

            self.focusWidget().undo()
        except AttributeError:
            pass

    def redo(self):
        try:
            self.focusWidget().redo()
        except AttributeError:
            pass

    def copy(self):
        try:
            self.focusWidget().copy()
        except AttributeError:
            pass

    def cut(self):
        try:
            self.focusWidget().cut()
        except AttributeError:
            pass

    def paste(self):
        try:
            self.focusWidget().paste()
        except AttributeError:
            pass

    def reset_clt(self):
        self.nomLineEdit.clear()
        self.bPSpinBox.setSpecialValueText("---")
        self.telSpinBox.setValue(6)
        self.emailLineEdit.clear()
        self.modeDePayementComboBox.setCurrentIndex(0)

    def export(self):
        pass

    def quitter(self):
        self.close()

    def closeEvent(self, event):
        message = "Etes vous sur de vouloir quitter ?"
        reponse = QMessageBox.question(self, "Confirmation", message,
                                       QMessageBox.Yes, QMessageBox.No)
        if reponse == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    @property
    def infoClientOK(self):
        if self.nomLineEdit.text() == "" or self.telSpinBox.value().bit_length() != 30 and self.telSpinBox.value() != 6 \
                or not self.emailLineEdit.text().__contains__("@") and self.emailLineEdit.text() != "":
            if self.nomLineEdit.text() == "":
                self.lb_alert_nom.show()
            if not self.telSpinBox.value().bit_length() == 30 and not self.telSpinBox.value() == 6:
                self.lb_alert_num.show()
            if not self.emailLineEdit.text().__contains__("@") and not self.emailLineEdit.text() == "":
                self.lb_alert_email.show()
            return False
        else:
            return True

    def enregistrer(self):
        if not self.infoClientOK:
            self.setStatusTip("Veuillez vérifier les informations client.")
        else:
            nom_clt = self.nomLineEdit.text()
            bp_clt = self.bPSpinBox.value()
            tel_clt = self.telSpinBox.value()
            email_clt = self.emailLineEdit.text()
            mode_pay = self.modeDePayementComboBox.currentText()

            save_client_bd = f"{nom_clt}/{tel_clt}/{email_clt}\n"
            try:
                with open(f"data/clients.bdf", 'a') as bd_client:
                    bd_client.write(save_client_bd).__str__()

            except FileNotFoundError:
                QMessageBox.information(self, "Base de données non trouvée",
                                        "Veuiller Verifier si il existe le fichier \n"
                                        "'client.bdf' dans le dossier data ")

            save_txt = f"{nom_clt}\n" \
                       f"{bp_clt}\n" \
                       f"{tel_clt}\n" \
                       f"{email_clt}\n" \
                       f"{mode_pay}\n"

            Path(f"Sauvegardes/{nom_clt}.txt")
            try:
                with open(f"Sauvegardes/{nom_clt}_{date.today()}.ftg", 'w') as save_file:
                    save_file.write(save_txt).__str__()
            except FileNotFoundError:
                with open(f"Sauvegardes/{nom_clt}_{date.today()}.txt", 'x') as save_file:
                    save_file.write(save_txt).__str__()

            with open(f"Sauvegardes/{nom_clt}_{date.today()}.ftg", 'a') as save_file:
                for i in range(0, self.table_achats.rowCount()):
                    try:
                        line = [self.table_achats.item(i, 0).text(), "*", self.table_achats.item(i, 1).text(), "*",
                                self.table_achats.item(i, 2).text(), "*", self.table_achats.item(i, 3).text(), "\n"]
                        save_file.writelines(line)
                    except AttributeError:
                        pass

            self.is_save = True

    def openFile(self):
        if self.is_save:
            (filename, filtre) = QFileDialog.getOpenFileName(self, "Ouvrir fichier Facturingo",
                                                             filter="Enregistrements facturingo (*.ftg)")
            if filename:
                with open(file="% s" % filename) as fichier:
                    text = fichier.read(-1)

                open_text = text.splitlines(False)

                self.nomLineEdit.setText(open_text[0])
                self.bPSpinBox.setValue(int(open_text[1]))
                self.telSpinBox.setValue(int(open_text[2]))
                self.emailLineEdit.setText(str(open_text[3]))
                self.modeDePayementComboBox.setCurrentIndex(0)
                self.resetTableAchat()

                for i in range(5, 30):
                    try:
                        line = open_text[i].split("*")
                        achat = QTableWidgetItem(line[0])
                        quantity = QTableWidgetItem(line[1])
                        prix = QTableWidgetItem(line[2])
                        prix_total = QTableWidgetItem(line[3])
                        self.table_achats.setItem(i - 5, 0, achat)
                        self.table_achats.setItem(i - 5, 1, quantity)
                        self.table_achats.setItem(i - 5, 2, prix)
                        self.table_achats.setItem(i - 5, 3, prix_total)
                    except IndexError:
                        pass

                goodName = str(filename).split("/")[-1].split(".")[-2].split("_")[-2]
                self.updateWindowTitle(goodName)

        else:
            self.saveAlert()

    def effacer(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    appli = Conta()
    appli.show()
    app.exec_()
