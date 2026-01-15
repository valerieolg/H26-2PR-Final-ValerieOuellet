# Importer les modules nécessaires :
# - sys pour le fonctionnement d'une application (ouvrir et ffermer l'app)
# - PyQt6 Qwidgets pour créer l'interface de l'application (le GUi) les boutons et les line edits

import sys
from PyQt6.QtWidgets import QWidget, QGridLayout, QLabel, QApplication, QLineEdit, QPushButton

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Comment doubler un nombre sans utiliser sa tête")
        self.setGeometry(50, 50, 350, 200)

        self.grid = QGridLayout()
        self.setLayout(self.grid)

        ######################################################################
        # Je crée mes Labels et mon lineEdit
        ######################################################################
        self.qlabel1 = QLabel()
        self.qlabel1.setText("Entrer la valeur de N :")
        self.grid.addWidget(self.qlabel1,0,0)

        self.qLine1 = QLineEdit()
        self.qLine1.setGeometry(50, 100, 200, 50)
        self.grid.addWidget(self.qLine1, 0, 1)

        self.qlabel2 = QLabel()
        self.qlabel2.setText("Voici le double :")
        self.grid.addWidget(self.qlabel2,1,0)

        self.resultat = QLabel("")
        self.resultat.setStyleSheet("border: 1px solid gray; padding: 1px;")
        self.grid.addWidget(self.resultat, 1, 1)

        ######################################################
        # Création des boutons
        ######################################################

        self.b1 = QPushButton("Valider l'opération")
        self.b2 = QPushButton("Sauvegarder")
        self.b3 = QPushButton("Charger")

        self.grid.addWidget(self.b1, 2, 0, 1, 2)
        self.grid.addWidget(self.b2, 3, 0)
        self.grid.addWidget(self.b3, 3, 1)

        self.b1.clicked.connect(self.valider)
        self.b2.clicked.connect(self.sauvegarder)
        self.b3.clicked.connect(self.charger)

########################################################
    # Création des méthodes pour les boutons
    ###################################################

    def valider(self):
        n = self.qLine1.text()
        try:
            nombre = int(n)
        except ValueError:
            self.resultat.setText("Erreur : entrer un nombre entier")
            return
        n2 = nombre * 2
        self.resultat.setText(str(n2))

    def sauvegarder(self):
        n2 = self.resultat.text()
        with open("resultats.txt", "w") as f:
            f.write(n2)

    def charger(self):
        with open("resultats.txt", "r") as f:
            valeur = f.read().strip()
            self.resultat.setText(valeur)

    ###########################################


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())