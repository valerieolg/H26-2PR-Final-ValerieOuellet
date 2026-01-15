import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel

class Infos:
    def __init__(self):
        self.message = ""

    def generer_message(self):
        self.message = ("Que veut dire le polymorphisme en python?\n"
            "Le polymorphisme c'est quand plusieurs objets différents peuvent utiliser la même méthode.\n\n"
            "Qu’est-ce qu’un fichier csv, à quoi il sert. Quel autre moyen vu en classe peut faire la même chose ?\n"
            "un fichier csv permet de créer une base de données à partir d'un code python. On a aussi vu les bases de données sqlite.\n\n"
            "Quelle est la différence entre tuple, dictionnaire, liste en python?\n"
            "un truple est comme une liste de données mais les données ne sont pas modifiables alors que la liste de donnée contient des données modifiables.\n"
            "Le dictionnaire est comme une liste d'objets mais au lieu d'avoir un index numérique, il a des variables non modifiables.")

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Questions sur la POO")
        self.setGeometry(50, 50, 1150, 360)

        ##### Créer un objet Infos #####
        self.infos = Infos()
        self.infos.generer_message()

        ###### Créer le QLabel #######
        self.label = QLabel(self)
        self.label.setText(self.infos.message)
        self.label.setGeometry(20, 20, 1150, 360)
        self.label.setStyleSheet("background: darkblue; border: 2px solid red; color: yellow; font: broadway; font-size:16px;")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())