import sys
from Translator import Translator

from PyQt5.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QPushButton,
    QWidget,
    QComboBox
)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.leftTranslator = Translator()
        self.rightTranslator = Translator()
        self.setWindowTitle("Languages Voice Translator")

        layout = QHBoxLayout()
        self.setFixedSize(1200, 800)
        self.dropDownLanguages = QComboBox()
        self.dropDownLanguages.addItems(list(self.leftTranslator.languages.keys()))
        # Add widgets to the layout
        layout.addWidget(self.dropDownLanguages)
        layout.addWidget(QPushButton("Left-Most"))
        layout.addWidget(QPushButton("Center"), 1)
        layout.addWidget(QPushButton("Right-Most"), 2)
        # Set the layout on the application's window
        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())