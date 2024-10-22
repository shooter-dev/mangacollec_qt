from PyQt5.QtWidgets import QWidget, QVBoxLayout

from app.IHM.widgets.info_lecture_volume.info_lecture_volume_ui import InfoLectureVolumeUI


class InfoLectureVolume(QWidget):
    __tome_lu_hor_possession: int = 0
    __tome_total_possession: int = 0
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui: InfoLectureVolumeUI = InfoLectureVolumeUI()
        self.ui.setup_ui(self, QVBoxLayout)

    @property
    def tome_lus(self) -> int:
        return int(self.ui.value_tome_lus_label.text())

    @tome_lus.setter
    def tome_lus(self, value: int):
        if value <= int(self.ui.value_tome_a_lire_label.text()):
            self.ui.value_tome_lus_label.setText(str(value))

        self.__change_envt_value()

    @property
    def tome_a_lire_en_possession(self) -> int:
        return int(self.ui.value_tome_a_lire_label.text())

    @tome_a_lire_en_possession.setter
    def tome_a_lire_en_possession(self, value: int):
        if value >= int(self.ui.value_tome_lus_label.text()):
            self.ui.value_tome_a_lire_label.setText(str(value))

        self.__change_envt_value()

    @property
    def tome_a_lire_hor_possession(self) -> int:
        return self.__tome_lu_hor_possession

    @tome_a_lire_hor_possession.setter
    def tome_a_lire_hor_possession(self, value: int):
        self.__tome_lu_hor_possession = value

        self.__change_envt_value()

    @property
    def tome_total_possession(self) -> int:
        return self.__tome_total_possession

    @tome_total_possession.setter
    def tome_total_possession(self, value: int):
        self.__tome_total_possession = value

        self.__change_envt_value()

    def __change_envt_value(self):
        if self.__tome_lu_hor_possession != 0 | self.__tome_total_possession != 0 | self.tome_lus != 0:
            # pourcentage = 100 * ( tome_lu / ( tome_lu_hor_mangatheque + tome_pas_encor_lu ) )
            value_bar: int = round((self.tome_lus / (self.__tome_lu_hor_possession + self.__tome_total_possession) ) * 100)
            self.ui.lecture_progress_bar.setValue(value_bar)