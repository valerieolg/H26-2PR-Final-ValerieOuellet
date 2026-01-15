# Importer les modules nécessaires :
# - os pour récupérer le nom de l'utilisateur
# - sys pour le fonctionnement d'une application (ouvrir et ffermer l'app)
# - PyQt6 Qwidgets pour créer l'interface de l'application (le GUi). Je les importe tous mais ceux utilisés seront QApplication, QLabel, QWidget

import os
import sys
from PyQt6.QtWidgets import *

class Window(QWidget):
    def créerwindow(self,win):
        win.setWindowTitle("Comment doubler un nombre sans utiliser sa tête")
        win.setGeometry(50, 50, 350, 200)
        self.frame = QFrame(win)
        self.frame.setGeometry(10, 10, 300, 200)

        self.grid = QGridLayout()
        self.frame.setLayout(self.grid)

        self.b1 = self.grid.addWidget(QPushButton("Valider l'opération", self.frame))
        self.b2 = self.grid.addWidget(QPushButton("Sauvegarder", self.frame))
        self.b3 = self.grid.addWidget(QPushButton("Charger", self.frame))

        ######################################################################
        # Je crée mes Labels et mes lineEdits
        ######################################################################
        qlabel1 = QLabel(win)
        qlabel1.setText("Entrer la valeur de N :")
        self.grid.addWidget(qlabel1,0,0)

        qLine1 = QLineEdit(win)
        qLine1.setGeometry(50, 100, 200, 50)
        self.grid.addWidget(qLine1, 0, 1)
        self.liste.append(qLine1)

        qlabel2 = QLabel(win)
        qlabel2.setText("Voici le double :")
        self.grid.addWidget(qlabel2,1,0)

        qLine2 = QLineEdit(win)
        qLine2.setGeometry(50, 100, 200, 50)
        self.grid.addWidget(qLine2, 1, 1)
        self.liste.append(qLine1)

        ######################################################

        def action(self):
            n = int(self.lineEdit.text())
            n2 = n * 2
            self.lineEdit2.setText(str(n2))

        ######################################################
        # Création des boutons
        ######################################################

        def b1_clicked():
            print(n2)

        def b2_clicked():
            print("Sauvegarde réussie!")

        def b3_clicked():
            print("Résultat chargé!")

        win.show()
        sys.exit(app.exec())
    ###########################################
    liste = []
    def charger(win):
        user = os.getlogin()
        f = open("C:users/" + user + "/resultats.txt", "r")
        f.readline()
        f.close()
    def sauvegarder(win):
        f = open("resultats.txt", "w")
        for l in liste:
            f.write(l.text()+"\n")
        f.close()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = QWidget()
    myWindow = Window()
    myWindow.buildWindow(win)
    win.show()
    app.exec_()