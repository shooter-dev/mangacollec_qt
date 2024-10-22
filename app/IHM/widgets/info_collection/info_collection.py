from PyQt5.QtWidgets import QWidget, QVBoxLayout

from app.IHM.widgets.info_collection.info_collection_ui import InfoCollectionoUI


class InfoCollection(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = InfoCollectionoUI()
        self.ui.setup_ui(self, QVBoxLayout)

    # @property
    # def tome_lus(self) -> int:
    #     return int(self.ui.value_tome_lus_label.text())
    #
    # @tome_lus.setter
    # def tome_lus(self, value: int):
    #     if value <= int(self.ui.value_tome_a_lire_label.text()):
    #         self.ui.value_tome_lus_label.setText(str(value))
    #
    #     self.__change_envt_value()
    #
    # @property
    # def tome_a_lire_en_possession(self) -> int:
    #     return int(self.ui.value_tome_a_lire_label.text())
    #
    # @tome_a_lire_en_possession.setter
    # def tome_a_lire_en_possession(self, value: int):
    #     if value >= int(self.ui.value_tome_lus_label.text()):
    #         self.ui.value_tome_a_lire_label.setText(str(value))
    #
    #     self.__change_envt_value()
    #
    # def __change_envt_value(self):
    #     value_bar: int = int((self.tome_lus / self.tome_a_lire_en_possession) * 100)
    #     self.ui.lecture_progress_bar.setValue(value_bar)