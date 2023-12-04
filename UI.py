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
        font = QFont('Arial', 15) 
        dropDownLanguagesLeft.setFont(font) 
        dropDownLanguagesRight.setFont(font) 
        # Add widgets to the layout
        layout.addWidget(dropDownLanguagesLeft, 0, 0)
        layout.addWidget(dropDownLanguagesRight, 0, 1)
        listenLeft = QPushButton("speak")
        listenRight = QPushButton("speak")
        listenLeft.setGeometry(200, 150, 100, 100)
        listenRight.setGeometry(200, 150, 100, 100)
        listenLeft.setStyleSheet("border-radius : 50; border : 2px solid black")
        listenRight.setStyleSheet("border-radius : 50; border : 2px solid black")
        # adding action to a button
        listenLeft.clicked.connect(lambda: self.listen_and_speak(str(dropDownLanguagesLeft.currentText()), str(dropDownLanguagesRight.currentText())))
        listenRight.clicked.connect(lambda: self.listen_and_speak(str(dropDownLanguagesRight.currentText()), str(dropDownLanguagesLeft.currentText())))
        layout.addWidget(listenLeft, 1, 0)
        layout.addWidget(listenRight, 1, 1)
        # Set the layout on the application's window
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