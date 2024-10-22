from PyQt5.QtWidgets import QComboBox


class ComboBox(QComboBox):
    def __init__(self, parent=None):
        QComboBox.__init__(parent)

    