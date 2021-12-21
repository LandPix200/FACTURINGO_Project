import typing
from collections import namedtuple

from PyQt5.QtCore import QAbstractTableModel, Qt, QVariant, QModelIndex

Achat = namedtuple('Achat', ("marchardise", "Prix_unitaire", "Quantité", "Prix_total"))


class ModelTableAchat(QAbstractTableModel):
    def __init__(self, achats):
        super(ModelTableAchat, self).__init__()
        self.titresColones = ("Nom de la merchardise", "Prix unitaire", "Quantité", "Prix total")
        self.achats = achats

    def headerData(self, section: int, orientation: Qt.Orientation, role: int = ...) -> typing.Any:
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self.titresColones[section]
        return QVariant

    def columnCount(self, parent: QModelIndex = ...) -> int:
        return len(self.titresColones)

    def rowCount(self, parent: QModelIndex = ...) -> int:
        return len(self.achats)

    def data(self, index: QModelIndex, role: int = ...) -> typing.Any:
        if role == Qt.DisplayRole and index.isValid():
            return self.achats[index.row()][index.column()]
        return QVariant
