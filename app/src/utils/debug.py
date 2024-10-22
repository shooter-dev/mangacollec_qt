from PyQt5.QtWidgets import QWidget


def widget_taille(widget: QWidget):
    print("#-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print(f"#  QWidget: {widget.objectName()} | Size: W: {widget.width()} h: {widget.height()}")
    print("#-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
