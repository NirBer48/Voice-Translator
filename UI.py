import sys
from Translator import Translator
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (
    QApplication,
    QGridLayout,
    QPushButton,
    QWidget,
    QComboBox
)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.Translator = Translator()
        self.setWindowTitle("Languages Voice Translator")

        layout = QGridLayout()
        self.setFixedSize(800, 600)

        dropDownLanguagesLeft = QComboBox()
        dropDownLanguagesLeft.setFixedSize(100,50)
        dropDownLanguagesLeft.addItems(list(self.Translator.languages.keys()))
        dropDownLanguagesRight = QComboBox()
        dropDownLanguagesRight.setFixedSize(100,50)
        dropDownLanguagesRight.addItems(list(self.Translator.languages.keys()))
        font = QFont('Arial', 12) 
        dropDownLanguagesLeft.setFont(font) 
        dropDownLanguagesRight.setFont(font) 
        layout.addWidget(dropDownLanguagesLeft, 0, 0)
        layout.addWidget(dropDownLanguagesRight, 0, 1)

        listenLeft = QPushButton("speak", self)
        listenRight = QPushButton("speak", self)
        listenLeft.setFixedSize(100, 100)
        listenRight.setFixedSize(100, 100)
        listenLeft.setFont(font)
        listenRight.setFont(font)
        listenLeft.setStyleSheet("border-radius : 50; border : 2px solid black")
        listenRight.setStyleSheet("border-radius : 50; border : 2px solid black")
        listenLeft.clicked.connect(lambda: self.listen_and_speak(str(dropDownLanguagesLeft.currentText()), str(dropDownLanguagesRight.currentText())))
        listenRight.clicked.connect(lambda: self.listen_and_speak(str(dropDownLanguagesRight.currentText()), str(dropDownLanguagesLeft.currentText())))
        layout.addWidget(listenLeft, 1, 0)
        layout.addWidget(listenRight, 1, 1)
        self.setLayout(layout)

    def listen_and_speak(self, fromLanguage, toLanguage):
        text = self.Translator.get_speech(fromLanguage)
        self.Translator.change_voice(toLanguage)
        self.Translator.speak_text(text, toLanguage)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())